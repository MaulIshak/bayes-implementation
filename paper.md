# Sistem Pakar untuk Identifikasi Penyakit Telinga dengan Menggunakan Metode Teorema Bayes

**Jurnal Teknik dan Informatika** | Volume 6 | Nomor 1 | Januari 2019 | ISSN 2089-5490

---

**Yofi Yance Elya Sitepu**
Program Studi Teknik Informatika, STMIK Pelita Nusantara Medan, Indonesia
yofiyance123@gmail.com

**Erwin Panggabean**
Program Studi Teknik Informatika, STMIK Pelita Nusantara Medan, Indonesia
erwinpangabean@gmail.com

---

## Abstrak

Telinga merupakan organ yang esensial dan vital serta merupakan cerminan kesehatan dan kehidupan. Telinga juga sangat kompleks dan sensitif, bervariasi pada keadaan iklim/cuaca, usia dan juga bergantung pada faktor gaya hidup seseorang. Kerusakan pada organ-organ tersebut diidentifikasi dan diobati oleh dokter spesialis yang disebut otolaringologis. Untuk dapat menegakkan identifikasi suatu kelainan pada penyakit telinga diperlukan kemampuan dan keterampilan melakukan identifikasi dan pemeriksaan organ-organ tersebut. Sistem ini dapat digunakan sebagai alat bantu bagi para dokter maupun paramedis dibidangnya dalam identifikasi dan memberikan saran pengobatan terhadap pasien yang menderita penyakit telinga.

Penelitian ini mencoba untuk membangun suatu sistem pakar yang dapat melakukan identifikasi terhadap penyakit telinga pada manusia dengan melihat ciri-ciri gejala fisik yang ada pada seorang pasien. Proses identifikasi dilakukan dengan menjawab tiap pertanyaan yang berkaitan dengan gejala yang ada pada pasien. Setiap jawaban dengan masing-masing nilai dan dari jawaban tersebut dapat diambil kesimpulan berdasarkan aturan (kaidah) dan rumusan perhitungan tiap nilai. Proses penalaran hingga mencapai kesimpulan ini menggunakan metode teorema bayes dan jenis penyakit yang diderita pasien dipergunakan untuk menentukan solusi atau saran pengobatan.

**Kata kunci:** Sistem Pakar Identifikasi Telinga, Teorema Bayes

---

## I. Pendahuluan

Telinga merupakan salah satu organ tubuh manusia yang berfungsi sebagai indera pendengaran dan penjaga keseimbangan. Sebagai organ pendengaran, telinga memiliki reseptor khusus yang berfungsi untuk mengenali getaran suara. Namun telinga hanya memiliki batasan frekuensi untuk dapat didengar, yaitu antara 20 Hz – 20.000 Hz. Penyakit telinga merupakan salah satu indra pada manusia selain kulit, lidah, mata dan hidung. Selain itu telinga sangat sensitif sehingga gampang terkena penyakit.

Namun dalam banyak kasus, pasien menemui dokter sebelumnya. Dokter umum dapat menangani masalah telinga yang gejalanya merupakan kondisi kesehatan masalah lainnya seperti flu atau pilek. Setelah penyebab utamanya diobati, sakit telinga juga akan hilang. Jika tetap tidak hilang atau bertambah parah, pasien akan dirujuk ke THT.

Di Indonesia, tenaga medis yang ahli (pakar) pada penyakit ini masih terbatas, baik dari segi jumlah dan waktu kerja. Seorang pakar tidak mungkin bekerja terus menerus setiap hari tanpa istirahat. Untuk itu penulis membuat aplikasi sistem pakar dalam bidang kesehatan sebagai alat bantu manusia untuk mengidentifikasi penyakit telinga dalam waktu relatif cepat disaat seorang dokter tidak ada.

Dalam penelitian ini diharapkan dapat memberikan solusi terhadap permasalahan yang dihadapi yaitu untuk mengidentifikasi penyakit telinga dengan menggunakan metode teorema bayes. Teorema bayes adalah teorema yang digunakan dalam statistika untuk menghitung peluang suatu hipotesis.

---

## II. Sistem Pakar

Secara umum, sistem pakar (_expert system_) adalah sistem yang berusaha mengadopsi pengetahuan manusia ke komputer, agar komputer dapat menyelesaikan masalah seperti yang biasa dilakukan oleh para ahli. Sistem pakar yang baik dirancang agar dapat menyelesaikan suatu permasalahan tertentu dengan meniru kerja dari para ahli. Dengan sistem pakar ini, orang awam pun dapat menyelesaikan masalah yang cukup rumit yang sebenarnya hanya dapat diselesaikan dengan bantuan para ahli. Bagi para ahli, sistem pakar ini juga akan membantu aktivitasnya sebagai asisten yang sangat berpengalaman.

### A. Teorema Bayes

Teorema Bayes merupakan sebuah pelacakan dalam mencari solusi dengan pendekatan _artificial intelligent_. Ada berbagai metode yang dapat diterapkan untuk mengatasi masalah ketidakpastian saat proses pelacakan terjadi. Adanya ketidakpastian pada proses pelacakan dapat terjadi karena adanya perubahan pengetahuan yang ada di dalam sistem.

Untuk itu diperlukan adanya suatu metode untuk mengatasi permasalahan tersebut. Dalam penelitian ini telah diterapkan suatu metode untuk mengatasi ketidakpastian dengan teorema bayes pada kasus pelacakan untuk mendiagnosa suatu penyakit. Algoritma menggunakan teorema Bayes dan mengasumsikan semua atribut independen atau tidak saling ketergantungan yang diberikan oleh nilai pada variabel kelas. Definisi lain mengatakan Teorema Bayes merupakan pengklasifikasian dengan metode untuk mengatasi sistem pelacakan yang dikemukakan oleh ilmuwan Inggris Thomas Bayes, yaitu memprediksi mengatasi permasalahan di masa depan berdasarkan pengalaman di masa sebelumnya.

Teorema Bayes didasarkan pada asumsi penyederhanaan bahwa nilai atribut secara kondisional saling bebas jika diberikan nilai output. Dengan kata lain, diberikan nilai output pelacakan mengamati secara bersama adalah produk dari pelacakan individu.

#### 2.3.1 Persamaan Metode

Persamaan dari teorema Bayes adalah:

$$P(H \mid E) = \frac{P(E \mid H) \times P(H)}{P(E)} \quad \cdots (1)$$

**Keterangan:**

- `P(H|E)` : Probabilitas hipotesis H benar jika diberikan evidence E
- `P(E|H)` : Probabilitas munculnya evidence E, jika diketahui hipotesis H benar
- `P(H)` : Probabilitas hipotesis H (menurut hasil sebelumnya) tanpa memandang evidence apapun
- `P(E)` : Probabilitas evidence E

Secara umum teorema bayes dengan E kejadian dan hipotesis H dapat dituliskan dalam bentuk:

$$P(H_i \mid E) = \frac{P(E \mid H_i) \cdot P(H_i)}{\sum P(E \mid H_i) \cdot P(H_i)} = \frac{P(E \mid H_i) \cdot P(H_i)}{P(E)} \quad \cdots (2)$$

Jika telah dilakukan pengujian terhadap hipotesis kemudian muncul lebih dari satu evidence, maka persamaannya akan menjadi:

$$P(H \mid E, e) = P(H \mid E) \cdot \frac{P(e \mid E, H)}{P(e, E)} \quad \cdots (3)$$

**Keterangan:**

- `e` : Evidence lama
- `E` : Evidence baru
- `P(H|E,e)` : Probabilitas hipotesis H benar jika muncul evidence baru dari evidence lama e
- `P(H|E)` : Probabilitas hipotesis H benar jika diberikan evidence E
- `P(e|E,H)` : Kaitan antara e dan E jika hipotesis H benar
- `P(e|E)` : Kaitan antara e dan E tanpa memandang hipotesis apapun

**Contoh kasus:**

Berikut adalah contoh perhitungan manual penyakit Perikondritis jika diketahui 3 gejala sebagai berikut:

Probabilitas gejala-gejala **tanpa** memperhatikan penyakit yang terjadi:

1. Kerusakan pada kartilago : 0,7
2. Cedera pada telinga : 0,6

Probabilitas gejala-gejala **dengan** memperhatikan penyakit yang terjadi:

1. Kerusakan pada kartilago : 0,5
2. Cedera pada telinga : 0,5

---

### B. Penyakit Telinga

Telinga adalah organ yang berfungsi untuk mendengar dan menyeimbangkan tubuh. Telinga dibagi menjadi tiga bagian: bagian luar, tengah dan dalam. Telinga luar, yang meliputi daun telinga (tulang rawan kulit yang terlihat), menerima suara, yang kemudian masuk melalui sebuah tabung kecil lalu ke membran timpani atau gendang telinga yang menandai awal dari bagian telinga tengah.

**Tabel 1. Tabel Penyakit Telinga**

| NO  | Penyakit          | Kode Penyakit |
| --- | ----------------- | ------------- |
| 1   | Othematoma        | P01           |
| 2   | Neuroma Akustikus | P02           |
| 3   | Meniere           | P03           |
| 4   | Perikondritis     | P04           |
| 5   | Infeksi Telinga   | P05           |
| 6   | Tuli              | P06           |

**Tabel 2. Tabel Data Gejala Penyakit Telinga**

| Kode Gejala | Nama-nama Gejala                                                             | Nilai Probabilitas |
| ----------- | ---------------------------------------------------------------------------- | ------------------ |
| G01         | Daun Telinga Terlihat Bengkak, Merah dan Kebiruan                            | 0,1                |
| G02         | Daun Telinga Hangat atau Panas pada saat Diraba                              | 0,4                |
| G03         | Daun Telinga Terasa Nyeri                                                    | 0,6                |
| G04         | Hilangnya Pendengaran Secara Bertahap/Mendadak                               | 0,4                |
| G05         | Hilangnya Keseimbangan                                                       | 0,1                |
| G06         | Telinga Berdengung                                                           | 0,3                |
| G07         | Mengalami Pusing Berputar Secara Tiba-tiba                                   | 0,4                |
| G08         | Telinga Terasa Penuh                                                         | 0,1                |
| G09         | Demam Tinggi                                                                 | 0,6                |
| G10         | Gatal Pada Telinga                                                           | 0,2                |
| G11         | Bengkak Pada Telinga                                                         | 0,1                |
| G12         | Telinga Berair                                                               | 0,8                |
| G13         | Pendengaran Terganggu                                                        | 0,5                |
| G14         | Kesulitan Menentukan Sumber Suara                                            | 0,5                |
| G15         | Berkata-kata, mendengar musik dan menonton TV dengan volume yang lebih keras | 0,4                |

**Tabel 3. Kombinasi Penyakit dengan Gejala**

| Kode Gejala | P01 | P02 | P03 | P04 | P05 | P06 |
| ----------- | :-: | :-: | :-: | :-: | :-: | :-: |
| G01         |  ✓  |     |     |  ✓  |  ✓  |     |
| G02         |  ✓  |     |     |     |     |     |
| G03         |  ✓  |     |     |  ✓  |     |     |
| G04         |     |  ✓  |  ✓  |     |     |     |
| G05         |     |  ✓  |     |     |     |     |
| G06         |     |  ✓  |  ✓  |     |     |     |
| G07         |     |     |  ✓  |     |     |     |
| G08         |     |     |  ✓  |     |     |     |
| G09         |     |     |     |  ✓  |  ✓  |     |
| G10         |     |     |     |  ✓  |  ✓  |     |
| G11         |     |     |     |     |  ✓  |     |
| G12         |     |     |     |     |  ✓  |     |
| G13         |     |     |     |     |     |  ✓  |
| G14         |     |     |     |     |     |  ✓  |
| G15         |     |     |     |     |     |  ✓  |

_Rulebase_ bertujuan untuk mengatur keterkaitan antara penyakit dengan gejala yang dialami seseorang. _Rulebase_ ini akan digunakan untuk menentukan proses pencarian atau menentukan kesimpulan yang didapat. Aturan tersebut biasanya berbentuk IF-THEN.

Kaidah dalam basis pengetahuan adalah sebagai berikut:

```
Rule 1 : IF G01 AND G02 AND G03           THEN P01 (Othematoma)
Rule 2 : IF G04 AND G05 AND G06           THEN P02 (Neuroma Akustikus)
Rule 3 : IF G04 AND G06 AND G07 AND G08  THEN P03 (Meniere)
Rule 4 : IF G01 AND G03 AND G09 AND G10  THEN P04 (Perikondritis)
Rule 5 : IF G01 AND G09 AND G10 AND G11 AND G12  THEN P05 (Infeksi Telinga)
Rule 6 : IF G13 AND G14 AND G15          THEN P06 (Tuli)
```

---

## III. Hasil dan Analisis

### A. Use Case Diagram

Diagram _use case_ menyajikan interaksi antara _use case_ dan aktor. Dimana, aktor dapat berupa orang, peralatan, atau sistem lain yang berinteraksi dengan sistem yang sedang dibangun. _Use case_ menggambarkan fungsionalitas sistem atau persyaratan-persyaratan yang harus dipenuhi sistem dari pandangan pemakai.

_[Gambar 3. Use Case Diagram Sistem Pakar]_

### B. Contoh Kasus

Hasil kasus dan contoh kasusnya identifikasi penyakit telinga adalah sebagai berikut:

| Kode | Gejala                                                                  | Nilai |
| ---- | ----------------------------------------------------------------------- | ----- |
| G01  | Daun telinga terlihat bengkak, merah dan kebiruan                       | 0,1   |
| G03  | Daun telinga terasa nyeri                                               | 0,6   |
| G04  | Hilangnya pendengaran secara bertahap/mendadak                          | 0,4   |
| G06  | Telinga berdengung                                                      | 0,3   |
| G09  | Demam Tinggi                                                            | 0,6   |
| G12  | Telinga berair                                                          | 0,8   |
| G15  | Berkata-kata, mendengar musik dan menonton TV dengan volume lebih keras | 0,4   |

#### Perhitungan Manual — Untuk Penyakit Tuli (P06)

**Langkah 1: Menentukan nilai P(E|Hi) dari setiap gejala**

```
G01 = 0,1  →  P(E|H1)
G03 = 0,6  →  P(E|H2)
G04 = 0,4  →  P(E|H3)
G06 = 0,3  →  P(E|H4)
G09 = 0,6  →  P(E|H5)
G12 = 0,8  →  P(E|H6)
G15 = 0,4  →  P(E|H7)
```

**Langkah 2: Menghitung semesta (Σ)**

```
Σ = G01 + G03 + G04 + G06 + G09 + G12 + G15
  = 0,1 + 0,6 + 0,4 + 0,3 + 0,6 + 0,8 + 0,4
  = 3,2
```

**Langkah 3: Menghitung P(Hi) — probabilitas hipotesis H tanpa memandang evidence**

```
P(H1) = 0,1 / 3,2 = 0,03125
P(H2) = 0,6 / 3,2 = 0,1875
P(H3) = 0,4 / 3,2 = 0,125
P(H4) = 0,3 / 3,2 = 0,09375
P(H5) = 0,6 / 3,2 = 0,1875
P(H6) = 0,8 / 3,2 = 0,25
P(H7) = 0,4 / 3,2 = 0,125
```

**Langkah 4: Menghitung probabilitas evidence E — P(E)**

```
P(E) = Σ P(Hi) × P(E|Hi)
     = (0,03125 × 0,1) + (0,1875 × 0,6) + (0,125 × 0,4)
       + (0,09375 × 0,3) + (0,1875 × 0,6) + (0,25 × 0,8)
       + (0,125 × 0,4)
     = 0,003125 + 0,1125 + 0,05 + 0,028125 + 0,1125 + 0,2 + 0,05
     = 0,55625
```

**Langkah 5: Menghitung nilai Bayes setiap hipotesis — P(Hi|E)**

```
P(H1|E) = (0,1 × 0,03125)  / 0,55625 = 0,005617978
P(H2|E) = (0,6 × 0,1875)   / 0,55625 = 0,202247191
P(H3|E) = (0,4 × 0,125)    / 0,55625 = 0,08988764
P(H4|E) = (0,3 × 0,09375)  / 0,55625 = 0,050561798
P(H5|E) = (0,6 × 0,1875)   / 0,55625 = 0,202257191
P(H6|E) = (0,8 × 0,25)     / 0,55625 = 0,359550562
P(H7|E) = (0,4 × 0,125)    / 0,55625 = 0,08988764
```

**Langkah 6: Menghitung total nilai Bayes**

```
Σ Bayes = (0,1 × 0,005617978) + (0,6 × 0,202247191) + (0,4 × 0,08988764)
        + (0,3 × 0,050561798) + (0,6 × 0,202257191) + (0,8 × 0,359550562)
        + (0,4 × 0,08988764)
        = 1,00000996
```

**Langkah 7: Menghitung persentase**

```
Persentase = 1,00000996 × 100% = 100,000996%
```

---

## IV. Tahap Implementasi Sistem

Implementasi sistem berfungsi untuk mempresentasikan hasil yang telah dirancang dengan aplikasi _desktop_ untuk menguji aplikasi yang dirancang apakah berjalan dengan baik atau ada kendala. Hasil perancangan aplikasi sistem pakar identifikasi penyakit telinga yang telah dikerjakan adalah sebagai berikut:

1. **Form Menu Utama** — Tampilan antarmuka utama aplikasi
2. **Form Jenis Penyakit** — Form untuk mengelola data jenis penyakit telinga
3. **Form Gejala Penyakit** — Form untuk mengelola data gejala beserta nilai probabilitas
4. **Form Basis Aturan** — Form untuk mengelola _rule_ IF-THEN
5. **Form Konsultasi** — Form diagnosa penyakit berdasarkan gejala yang dipilih user
6. **Form Laporan** — Tampilan laporan hasil konsultasi
7. **Form Login** — Halaman autentikasi pengguna

Dengan menggunakan sistem yang telah dibuat, untuk diagnosa penyakit telinga, user dapat memilih gejala penyakit dengan mencentang gejala yang dirasakan sesuai dengan yang disediakan sistem. Jika gejala yang dimasukkan sesuai dengan rule yang ada maka sistem akan mengidentifikasi dan memberitahukan jenis penyakitnya. Jika gejala tidak sesuai maka sistem akan memberitahukan bahwa penyakit yang dipilih tidak ditemukan.

---

## Kesimpulan

Berdasarkan dari hasil analisis data pada bab-bab sebelumnya dapat ditarik kesimpulan bahwa:

1. Dengan menggunakan Sistem pakar identifikasi penyakit telinga, dapat membantu pihak masyarakat untuk dapat mengetahui penyakit telinga berdasarkan gejala yang dialami.
2. Dengan perancangan Sistem pakar identifikasi penyakit telinga, pihak masyarakat akan terbantu untuk mengetahui penyakit yang diderita, sehingga masyarakat yang mengalami penyakit telinga tersebut dapat melakukan tindakan secara dini untuk mengobati penyakit telinga yang dialami.
3. Sistem pakar identifikasi penyakit telinga dengan metode teorema bayes dapat mengatasi permasalahan dalam menentukan jenis penyakit telinga berdasarkan gejala yang dialami.
4. Metode teorema bayes dapat menjadi solusi pemecahan masalah identifikasi penyakit telinga.

---

## Referensi

1. T. Sutojo, "Kecerdasan Buatan", 2011.
2. Kecerdasan buatan atau kecerdasan yang ditambah kepada suatu sistem yang bisa di atur.
3. Edy Winarno ST, M.Eng, Ali Zaki, "SmitDev Community", Vol. 8, 2010.
4. R. Ismail, N. A & Akhmad D, "Pembuatan Sistem Informasi Penjualan Pada Ade Jaya Ponsel dengan menggunakan Visual Basic", Ilmiah DASI Vol. 14 (4), 2013, 41.
5. Lisnawita, Lucky Lhaura Van FC, Evi Lindra, "Sistem Pakar Diagnosa Penyakit THT", VOL. 1, NO. 2, November 2016.
6. Sri Winiarti, "Pemanfaatan Teorema Bayes Dalam Penyakit THT", Vol 2, No. 2, Juli 2008.
7. Jurnal Coding Sistem Komputer, "Diagnosa Penyakit Telinga Hidung Dan Tenggorokan (THT) Pada Anak Dengan Menggunakan Sistem Pakar Berbasis Mobile Android", Universitas Tanjungpura, Volume 02, No. 2, 2014, hal 8–14.
