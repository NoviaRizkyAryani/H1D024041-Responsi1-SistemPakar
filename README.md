# KosMatch: Rekomendasi Tipe Kos Berdasarkan Gaya Hidup Mahasiswa

**KosMatch** adalah sistem pakar (Expert System) berbasis web yang dirancang untuk membantu mahasiswa menemukan tipe hunian kos yang paling sesuai dengan kepribadian, kebutuhan, dan gaya hidup mereka. KosMatch menggunakan metode **Forward Chaining** untuk melakukan inferensi berdasarkan 16 variabel preferensi mahasiswa.

---
* **Nama:** Novia Rizky Aryani
* **NIM:** H1D024041
* **Shift KRS:** Shift H
* **Shift Baru:** Shift D
---

### Inference Engine: Forward Chaining
Sistem bekerja dengan mengumpulkan fakta (Working Memory) dari input pengguna, lalu mencocokkannya dengan aturan (Production Rules) untuk mengakumulasi skor pada 5 kategori hunian utama:
* **Kos Sultan:** Prioritas fasilitas premium dan kenyamanan tanpa batas.
* **Kos Hemat:** Fokus pada efisiensi budget dan kedekatan lokasi.
* **Kos Nongkrong:** Dirancang untuk kepribadian ekstrovert yang mencari komunitas.
* **Kos Privat:** Untuk mereka yang membutuhkan ketenangan dan ruang hobi (gaming/nugas).
* **Kos Tertib:** Mengutamakan keamanan, aturan yang jelas, dan disiplin.

---

## Teknologi yang Digunakan
* **Backend:** Python 3.9+ dengan Framework **Flask**.
* **Frontend:** HTML5, **Tailwind CSS** (Ghibli Custom Theme).
* **Deployment:** **Vercel** (Serverless Functions).

---

## Variabel Keputusan (16 Kriteria)
Sistem melakukan analisis mendalam terhadap kriteria-kriteria berikut:
1.  **Alokasi Budget** (Hemat, Menengah, Premium).
2.  **Mode Transportasi** (Jalan Kaki vs Kendaraan Pribadi).
3.  **Kebutuhan Interaksi Sosial** (Introvert vs Ekstrovert).
4.  **Tipe Kamar Mandi** (Luar vs Dalam).
5.  **Fasilitas Pendingin** (Kipas vs AC).
6.  **Intensitas Memasak** (Dapur Mandiri vs Beli Luar).
7.  **Akses Keluar Masuk** (Bebas 24 Jam vs Ada Jam Malam).
8.  **Keamanan Gedung** (Biasa vs Wajib CCTV).
9.  **Kunjungan Teman** (Sering vs Jarang).
10. **Tingkat Ketenangan** (Hening vs Toleransi Bising).
11. **Jumlah Barang** (Minimalis vs Banyak).
12. **Layanan Kebersihan** (Mandiri vs Cleaning Service).
13. **Kualitas Internet** (Kuota HP vs WiFi Kencang).
14. **Fasilitas Parkir** (Cukup Motor vs Mobil/Luas).
15. **Urusan Cuci Pakaian** (Cuci Sendiri vs Laundry).
16. **Pencahayaan & Udara** (Jendela Besar vs Minim Cahaya).

---

## Cara Menjalankan Secara Lokal
- Clone repositori ini ke komputer Anda.
- Instal dependensi Flask: pip install flask
- Jalankan aplikasi: python api/index.py
- Akses melalui browser pada alamat: http://127.0.0.1:5000

---

## Struktur Folder
```text
KosMatch/
├── api/
│   ├── templates/
│   │   └── index.html    # UI Utama 
│   └── index.py          # Logika Expert System (Forward Chaining)
├── requirements.txt      # Daftar Library (Flask)
└── vercel.json           # Konfigurasi Deployment Vercel
