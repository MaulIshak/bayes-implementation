import csv
import os

def load_data(dataset_dir="dataset"):
    # Load Gejala
    gejala = {}
    with open(os.path.join(dataset_dir, 'gejala.csv'), mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Mengubah koma menjadi titik untuk konversi float jika formatnya lokal
            nilai_str = row['nilai_probabilitas'].replace(',', '.')
            gejala[row['kode_gejala']] = {
                'nama': row['nama_gejala'],
                'probabilitas': float(nilai_str)
            }
            
    # Load Penyakit
    penyakit = {}
    with open(os.path.join(dataset_dir, 'penyakit.csv'), mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            penyakit[row['kode_penyakit']] = {
                'nama': row['nama_penyakit'],
                'gejala': []
            }
            
    # Load Kombinasi Penyakit Gejala (Rulebase)
    with open(os.path.join(dataset_dir, 'kombinasi_penyakit_gejala.csv'), mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            penyakit[row['kode_penyakit']]['gejala'].append(row['kode_gejala'])
            
    return gejala, penyakit


def calculate_bayes_paper(selected_symptoms, gejala_dict):
    """
    Mengimplementasikan persis perhitungan Teorema Bayes sesuai acuan paper (Langkah 1 - 7).
    Di paper tersebut, setiap gejala yang dimasukkan diperlakukan sebagai suatu hipotesis (H_i) tersendiri
    dalam langkah perhitungan matematikanya.
    """
    hasil_langkah = {}
    
    # Langkah 1: Menentukan nilai P(E|Hi) dari setiap gejala
    p_e_given_hi = []
    for g in selected_symptoms:
        val = gejala_dict[g]['probabilitas']
        p_e_given_hi.append(val)
        
    hasil_langkah["p_e_given_hi"] = p_e_given_hi
        
    # Langkah 2: Menghitung semesta (Σ)
    sigma = sum(p_e_given_hi)
    hasil_langkah["sigma"] = sigma
    
    if sigma == 0:
        return None
    
    # Langkah 3: Menghitung P(Hi) -- probabilitas hipotesis H tanpa memandang evidence
    p_hi = [val / sigma for val in p_e_given_hi]
    hasil_langkah["p_hi"] = p_hi
    
    # Langkah 4: Menghitung probabilitas evidence E -- P(E)
    # P(E) = Sigma (P(Hi) x P(E|Hi))
    p_e = sum((p_h * p_e_h) for p_h, p_e_h in zip(p_hi, p_e_given_hi))
    hasil_langkah["p_e"] = p_e
    
    # Langkah 5: Menghitung nilai Bayes setiap hipotesis -- P(Hi|E)
    # P(H_i|E) = (P(E|Hi) * P(Hi)) / P(E)
    p_hi_given_e = []
    for p_e_h, p_h in zip(p_e_given_hi, p_hi):
        if p_e > 0:
            val = (p_e_h * p_h) / p_e
        else:
            val = 0
        p_hi_given_e.append(val)
    hasil_langkah["p_hi_given_e"] = p_hi_given_e
    
    # Langkah 6: Menghitung total nilai Bayes
    sigma_bayes = sum(p_hi_given_e)
    hasil_langkah["sigma_bayes"] = sigma_bayes
    
    # Langkah 7: Menghitung persentase
    persentase = sigma_bayes * 100
    hasil_langkah["persentase"] = persentase
    
    return hasil_langkah


def identify_penyakit(selected_symptoms, penyakit_dict):
    """
    Mengidentifikasi penyakit dari basis pengetahuan Rule (IF-THEN).
    "Jika gejala yang dimasukkan sesuai dengan rule yang ada maka sistem akan mengidentifikasi..."
    """
    selected_set = set(selected_symptoms)
    hasil_identifikasi = []
    
    for kode_p, p_data in penyakit_dict.items():
        rule_gejala = set(p_data['gejala'])
        
        # Mengecek persentase/porsi kecocokan dengan Rule
        intersect = rule_gejala.intersection(selected_set)
        
        if len(intersect) > 0:
            hasil_identifikasi.append({
                'kode': kode_p,
                'nama': p_data['nama'],
                'gejala_match': list(intersect),
                'total_gejala_rule': len(rule_gejala),
                'match_count': len(intersect)
            })
            
    # Mengurutkan memprioritaskan yang jumlah gejala rule-nya terpenuhi paling banyak
    hasil_identifikasi.sort(key=lambda x: x['match_count'], reverse=True)
    return hasil_identifikasi


if __name__ == "__main__":
    dataset_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset')
    
    try:
        gejala_dict, penyakit_dict = load_data(dataset_path)
        
        # Menggunakan contoh kasus yang ada pada paper Langkah 1 - 7:
        contoh_gejala = ["G01", "G03", "G04", "G06", "G09", "G12", "G15"]
        
        print("====== SISTEM PAKAR IDENTIFIKASI PENYAKIT TELINGA ======")
        print("Berdasarkan algoritma perhitungan dari Paper Rekomendasi\n")
        
        print(f"Gejala yang dipilih:")
        for i, g in enumerate(contoh_gejala, 1):
            nama_gejala = gejala_dict[g]['nama']
            nilai_prob = gejala_dict[g]['probabilitas']
            print(f"{g} : {nama_gejala} ({nilai_prob}) -> P(E|H{i})")
        print("-" * 50)
            
        print("\n=== TAHAP 1: IDENTIFIKASI PENYAKIT (RULE BASED) ===")
        penyakit_cocok = identify_penyakit(contoh_gejala, penyakit_dict)
        if penyakit_cocok:
            for p in penyakit_cocok:
                print(f"Found: {p['nama']} ({p['kode']}) - Cocok {p['match_count']}/{p['total_gejala_rule']} dari aturan (Gejala: {', '.join(p['gejala_match'])})")
        else:
            print("Penyakit yang dipilih tidak ditemukan (tidak sesuai dengan rule apapun).")
            
        print("\n=== TAHAP 2: PERHITUNGAN TEOREMA BAYES MANUAL ===")
        hasil = calculate_bayes_paper(contoh_gejala, gejala_dict)
        
        if hasil:
            print(f"Langkah 1: Sudah dideskripsikan pada daftar gejala di atas.")
            
            print(f"Langkah 2: Menghitung semesta (Σ)")
            print(f"Σ = {hasil['sigma']}")
            
            print("\nLangkah 3: Menghitung P(Hi)")
            for i, p_h in enumerate(hasil['p_hi'], 1):
                print(f"P(H{i}) = {p_h}")
                
            print(f"\nLangkah 4: Menghitung probabilitas evidence E -- P(E)")
            print(f"P(E) = {hasil['p_e']}")
            
            print("\nLangkah 5: Menghitung nilai Bayes setiap hipotesis -- P(Hi|E)")
            for i, p_h_e in enumerate(hasil['p_hi_given_e'], 1):
                print(f"P(H{i}|E) = {p_h_e}")
                
            print(f"\nLangkah 6: Menghitung total nilai Bayes (Σ Bayes)")
            print(f"Σ Bayes = {hasil['sigma_bayes']}")
            
            print(f"\nLangkah 7: Menghitung persentase")
            print(f"Persentase Bayes untuk sekumpulan gejala tersebut = {hasil['persentase']}%")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
