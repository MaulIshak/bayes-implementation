import csv
import os
import sys
import io

# Set stdout encoding to UTF-8 to handle special characters
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# =============================================================================
# LOAD DATA
# =============================================================================

def load_data(dataset_dir="dataset"):
    gejala = {}
    with open(os.path.join(dataset_dir, 'gejala.csv'), mode='r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            nilai_str = row['nilai_probabilitas'].replace(',', '.')
            gejala[row['kode_gejala']] = {
                'nama': row['nama_gejala'],
                'probabilitas': float(nilai_str)
            }

    penyakit = {}
    with open(os.path.join(dataset_dir, 'penyakit.csv'), mode='r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            penyakit[row['kode_penyakit']] = {
                'nama': row['nama_penyakit'],
                'gejala': []
            }

    with open(os.path.join(dataset_dir, 'kombinasi_penyakit_gejala.csv'), mode='r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            penyakit[row['kode_penyakit']]['gejala'].append(row['kode_gejala'])

    return gejala, penyakit


# =============================================================================
# TEOREMA BAYES - PER PENYAKIT
#   - Bayes dihitung untuk setiap penyakit secara terpisah,
#     menggunakan gejala pasien yang COCOK dengan rule penyakit tersebut.
#   - Menghasilkan skor kepercayaan (confidence) per penyakit yang
#     bisa dibandingkan, sehingga sistem pakar bisa memberi kesimpulan bermakna.
# =============================================================================

def hitung_bayes_per_penyakit(gejala_cocok: list, gejala_dict: dict) -> dict | None:
    """
    Menghitung Teorema Bayes sesuai langkah-langkah pada paper,
    untuk satu penyakit berdasarkan gejala pasien yang cocok dengan rule-nya.

    Parameter:
        gejala_cocok : list kode gejala yang cocok antara input pasien dan rule penyakit
        gejala_dict  : dictionary data gejala dari CSV
    """
    if not gejala_cocok:
        return None

    # Langkah 1: Ambil P(E|Hi) - nilai probabilitas setiap gejala yang cocok
    p_e_given_hi = {g: gejala_dict[g]['probabilitas'] for g in gejala_cocok}

    # Langkah 2: Hitung semesta Sigma
    sigma = sum(p_e_given_hi.values())
    if sigma == 0:
        return None

    # Langkah 3: Hitung P(Hi) - prior, tanpa memandang evidence apapun
    p_hi = {g: val / sigma for g, val in p_e_given_hi.items()}

    # Langkah 4: Hitung probabilitas evidence P(E)
    p_e = sum(p_hi[g] * p_e_given_hi[g] for g in gejala_cocok)

    # Langkah 5: Hitung nilai Bayes setiap hipotesis P(Hi|E)
    p_hi_given_e = {}
    for g in gejala_cocok:
        p_hi_given_e[g] = (p_e_given_hi[g] * p_hi[g]) / p_e if p_e > 0 else 0

    # Langkah 6: Total nilai Bayes
    sigma_bayes = sum(p_hi_given_e.values())

    # Langkah 7: Persentase kepercayaan (confidence)
    #
    # Catatan: Berbeda dengan paper yang menjumlah seluruh gejala (hasilnya ~100%),
    # di sini kita menggunakan rasio gejala yang terpenuhi terhadap total gejala rule.
    # Ini membuat skor antar penyakit bisa dibandingkan secara bermakna.
    rasio_terpenuhi = len(gejala_cocok)  # berapa gejala rule yang terpenuhi
    persentase = sigma_bayes * 100

    return {
        'p_e_given_hi': p_e_given_hi,
        'sigma':        sigma,
        'p_hi':         p_hi,
        'p_e':          p_e,
        'p_hi_given_e': p_hi_given_e,
        'sigma_bayes':  sigma_bayes,
        'persentase':   persentase,
    }


# =============================================================================
# DIAGNOSIS: GABUNGAN RULE-BASED + BAYES
# =============================================================================

def diagnosa(gejala_pasien: list, gejala_dict: dict, penyakit_dict: dict) -> list:
    """
    Mengidentifikasi penyakit dari gejala pasien menggunakan:
      1. Rule-based matching (IF-THEN) - mana rule yang terpicu
      2. Teorema Bayes per penyakit   - skor kepercayaan tiap kandidat
    Mengembalikan list hasil, diurutkan dari skor tertinggi.
    """
    selected = set(gejala_pasien)
    hasil = []

    for kode, data in penyakit_dict.items():
        rule_set  = set(data['gejala'])
        cocok     = list(rule_set & selected)
        tidak_ada = list(rule_set - selected)

        if not cocok:
            continue  # Tidak ada satu pun gejala rule yang terpenuhi → lewati

        bayes = hitung_bayes_per_penyakit(cocok, gejala_dict)
        if not bayes:
            continue

        # Skor akhir: nilai Bayes dikali rasio kelengkapan rule
        rasio_rule   = len(cocok) / len(rule_set)
        skor_akhir   = bayes['persentase'] * rasio_rule

        hasil.append({
            'kode':           kode,
            'nama':           data['nama'],
            'gejala_rule':    list(rule_set),
            'gejala_cocok':   cocok,
            'gejala_kurang':  tidak_ada,
            'jumlah_cocok':   len(cocok),
            'total_rule':     len(rule_set),
            'rasio_rule':     rasio_rule * 100,
            'bayes':          bayes,
            'skor_akhir':     skor_akhir,
        })

    hasil.sort(key=lambda x: x['skor_akhir'], reverse=True)
    return hasil


# =============================================================================
# TAMPILAN OUTPUT
# =============================================================================

SEP  = "=" * 60
SEP2 = "-" * 60

def cetak_detail_bayes(hasil_penyakit: dict, gejala_dict: dict):
    p      = hasil_penyakit
    bayes  = p['bayes']
    nama_p = f"{p['nama']} ({p['kode']})"

    print(f"\n{'-'*60}")
    print(f"  Perhitungan Bayes untuk: {nama_p}")
    print(f"{'-'*60}")

    # Langkah 1
    print(f"\n  Langkah 1 - Gejala cocok & nilai P(E|Hi):")
    for i, g in enumerate(p['gejala_cocok'], 1):
        nama_g = gejala_dict[g]['nama']
        val    = bayes['p_e_given_hi'][g]
        print(f"    H{i} ({g}) : {nama_g[:45]:<45} = {val:.4f}")

    # Langkah 2
    print(f"\n  Langkah 2 - Semesta (Sigma P(E|Hi))")
    print(f"    Sigma = {' + '.join(f'{v:.4f}' for v in bayes['p_e_given_hi'].values())}")
    print(f"    Sigma = {bayes['sigma']:.4f}")

    # Langkah 3
    print(f"\n  Langkah 3 - P(Hi) = P(E|Hi) / Sigma")
    for i, g in enumerate(p['gejala_cocok'], 1):
        print(f"    P(H{i}) = {bayes['p_e_given_hi'][g]:.4f} / {bayes['sigma']:.4f} = {bayes['p_hi'][g]:.6f}")

    # Langkah 4
    print(f"\n  Langkah 4 - P(E) = Sigma P(Hi) * P(E|Hi)")
    terms = [f"({bayes['p_hi'][g]:.6f} * {bayes['p_e_given_hi'][g]:.4f})"
             for g in p['gejala_cocok']]
    print(f"    P(E) = {' + '.join(terms)}")
    print(f"    P(E) = {bayes['p_e']:.6f}")

    # Langkah 5
    print(f"\n  Langkah 5 - P(Hi|E) = P(E|Hi) * P(Hi) / P(E)")
    for i, g in enumerate(p['gejala_cocok'], 1):
        v = bayes['p_hi_given_e'][g]
        print(f"    P(H{i}|E) = ({bayes['p_e_given_hi'][g]:.4f} * {bayes['p_hi'][g]:.6f}) / {bayes['p_e']:.6f} = {v:.6f}")

    # Langkah 6
    print(f"\n  Langkah 6 - Sigma Bayes = {bayes['sigma_bayes']:.6f}")

    # Langkah 7
    print(f"  Langkah 7 - Persentase = {bayes['sigma_bayes']:.6f} * 100% = {bayes['persentase']:.4f}%")

    # Info kelengkapan rule
    print(f"\n  Kelengkapan rule : {p['jumlah_cocok']}/{p['total_rule']} gejala terpenuhi ({p['rasio_rule']:.1f}%)")
    if p['gejala_kurang']:
        kurang_str = ', '.join(f"{g} ({gejala_dict[g]['nama'][:25]})" for g in p['gejala_kurang'])
        print(f"  Gejala belum ada : {kurang_str}")
    print(f"\n  > Skor Akhir = Bayes% * Rasio Rule = {bayes['persentase']:.4f}% * {p['rasio_rule']/100:.4f} = {p['skor_akhir']:.4f}")


def jalankan_diagnosa(gejala_pasien: list, gejala_dict: dict, penyakit_dict: dict):
    print(f"\n{SEP}")
    print(" SISTEM PAKAR IDENTIFIKASI PENYAKIT TELINGA")
    print(" Metode: Teorema Bayes")
    print(f"{SEP}")

    # Tampilkan gejala input pasien
    print(f"\nGejala yang dilaporkan pasien ({len(gejala_pasien)} gejala):")
    for g in gejala_pasien:
        print(f"  [{g}] {gejala_dict[g]['nama']} - P = {gejala_dict[g]['probabilitas']:.4f}")

    print(f"\n{SEP}")
    print(" HASIL PERHITUNGAN TEOREMA BAYES PER PENYAKIT")
    print(f"{SEP}")

    hasil = diagnosa(gejala_pasien, gejala_dict, penyakit_dict)

    if not hasil:
        print("\n  Tidak ada penyakit yang teridentifikasi berdasarkan gejala yang dipilih.")
        return

    # Detail per penyakit
    for p in hasil:
        cetak_detail_bayes(p, gejala_dict)

    # Ringkasan
    print(f"\n{SEP}")
    print(" RINGKASAN SKOR SEMUA KANDIDAT PENYAKIT")
    print(f"{SEP}")
    print(f"  {'No':<4} {'Penyakit':<22} {'Kode':<6} {'Bayes%':>8} {'Rule%':>7} {'Skor Akhir':>11}")
    print(f"  {SEP2}")
    for i, p in enumerate(hasil, 1):
        print(f"  {i:<4} {p['nama']:<22} {p['kode']:<6} "
              f"{p['bayes']['persentase']:>7.2f}% "
              f"{p['rasio_rule']:>6.1f}% "
              f"{p['skor_akhir']:>10.4f}")

    # Kesimpulan
    terbaik = hasil[0]
    print(f"\n{SEP}")
    print(" KESIMPULAN SISTEM PAKAR")
    print(f"{SEP}")
    print(f"\n  Berdasarkan {len(gejala_pasien)} gejala yang dilaporkan, sistem")
    print(f"  mengidentifikasi pasien kemungkinan besar menderita:\n")
    print(f"  +==================================================+")
    print(f"  |  {terbaik['nama']:<47} |")
    print(f"  |  Kode Penyakit : {terbaik['kode']:<31} |")
    print(f"  |  Skor Akhir    : {terbaik['skor_akhir']:<31.4f} |")
    print(f"  |  Kelengkapan   : {terbaik['jumlah_cocok']}/{terbaik['total_rule']} gejala rule ({terbaik['rasio_rule']:.1f}%){" ":8} |")
    print(f"  +==================================================+")

    if terbaik['rasio_rule'] < 100:
        print(f"\n  !!! Catatan: Rule untuk {terbaik['nama']} belum sepenuhnya terpenuhi.")
        kurang = ', '.join(f"{g}" for g in terbaik['gejala_kurang'])
        print(f"    Gejala yang belum terkonfirmasi: {kurang}")
        print(f"    Disarankan konsultasi lebih lanjut dengan dokter THT.")
    else:
        print(f"\n  ✓ Semua gejala rule untuk {terbaik['nama']} terpenuhi.")
        print(f"    Identifikasi bersifat definitif berdasarkan basis pengetahuan.")

    print()


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    dataset_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset')

    gejala_dict, penyakit_dict = load_data(dataset_path)

    # ── Contoh kasus dari paper ──────────────────────────────────────────────
    contoh_gejala = ["G01", "G03", "G04", "G06", "G09", "G12", "G15"]
    jalankan_diagnosa(contoh_gejala, gejala_dict, penyakit_dict)