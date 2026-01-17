# Implementasi Algoritma CYK untuk Validasi Tata Bahasa Bali

> **Penyelesaian Kasus 2 - Teori Bahasa dan Otomata (TBO)** > Program Studi Informatika, Fakultas MIPA, Universitas Udayana  
> Semester 3 - Tahun Akademik 2025/2026

## 📋 Deskripsi Proyek

Repository ini berisi kode sumber (*source code*) untuk implementasi algoritma **Cocke-Younger-Kasami (CYK)**. Proyek ini bertujuan untuk memvalidasi struktur kalimat Bahasa Bali berdasarkan aturan tata bahasa bebas konteks (*Context-Free Grammar* / CFG) yang telah dikonversi menjadi Bentuk Normal Chomsky (*Chomsky Normal Form* / CNF).

Fokus utama validasi adalah pada struktur kalimat berbasis **Frasa Kerja (Verb Phrase)**, baik Transitif maupun Intransitif, dengan pola dasar seperti:
- Predikat - Subjek (P-S)
- Predikat - Subjek - Objek (P-S-O)
- Predikat - Objek - Subjek (P-O-S)
- Dan variasi dengan kata keterangan (Keterangan/Pelengkap).

## 👥 Anggota Kelompok 4

| No | Nama | NIM |
| :--- | :--- | :--- |
| 1 | Mochammad Riky Hidavat | 2408561090 |
| 2 | Kadek Pasek Divandra Kusuma | 2408561069 |
| 3 | I Kadek Candra Gunawan | 2408561057 |
| 4 | Made Mahatmika Adriananda Kusuma | 2408561045 |
| 5 | I Gede Arya Kesha Narendra Subirman | 2408561048 |

**Dosen Pengampu:** Dr. Anak Agung Istri Ngurah Eka Karyawati, S.Si., M.Eng.

## 🛠️ Fitur & Metodologi

1.  **Parsing CYK (Bottom-Up):** Menggunakan tabel triangular untuk menentukan apakah kalimat input dapat diturunkan dari *Start Symbol* (K).
2.  **CFG ke CNF:** Seluruh aturan produksi telah dikonversi ke format CNF (A → BC atau A → a).
3.  **Leksikon Bahasa Bali:** Mendukung validasi kata benda, kata kerja, kata keterangan, dan pelengkap dalam Bahasa Bali sesuai dataset.
4.  **Handling Case Insensitive:** Input pengguna akan diproses dalam huruf kecil (*lowercase*) untuk meminimalisir kesalahan input.

## 📂 Struktur File

- `main.py` : Script utama program (berisi logika algoritma CYK dan antarmuka input).
- `requirements.txt` : Daftar pustaka Python yang dibutuhkan.
- `README.md` : Dokumentasi proyek.
- `dataset/` : Folder berisi data uji (opsional).

## ⚙️ Prasyarat (Requirements)

Pastikan Anda telah menginstal **Python 3.x** di komputer Anda.
Tidak ada *library* eksternal berat yang dibutuhkan karena program dibangun menggunakan *standard library* Python.

Jika ada library tambahan (misal `pandas` untuk visualisasi tabel), install dengan:

```bash
pip install -r requirements.txt
