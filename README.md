Berikut adalah template `README.md` untuk tugas Anda:

---

# DES Encryption & Decryption with Socket Programming

## Deskripsi Proyek
Proyek ini mengimplementasikan algoritma enkripsi dan dekripsi DES untuk komunikasi terenkripsi antar dua pengguna menggunakan socket programming. Program ini dikembangkan sebagai Tugas 2 Keamanan Informasi yang bertujuan untuk mengirimkan pesan terenkripsi dari satu pengguna (*client*) ke pengguna lain (*server*), di mana penerima dapat mendekripsi pesan yang diterima.

## Fitur
1. **Enkripsi DES**: Mengenkripsi teks lebih dari 64-bit menggunakan metode pemecahan teks menjadi blok-blok 64-bit.
2. **Socket Programming**: Mengirimkan string terenkripsi antar dua pengguna tanpa penyimpanan file.
3. **Dekripsi DES**: Menerima dan mendekripsi pesan yang diterima pada sisi *server*.
4. **Penggunaan Kunci yang Sama**: Kunci enkripsi yang sudah disepakati (hardcode) antara *client* dan *server*.
   
## Cara Menggunakan
1. **Instalasi Dependensi**:
   Pastikan `pycryptodome` terpasang dengan menjalankan:
   ```bash
   pip install pycryptodome
   ```

2. **Menjalankan Server**:
   Buka terminal atau command prompt, kemudian jalankan perintah berikut untuk memulai server:
   ```bash
   python Server.py
   ```
   Server akan menunggu koneksi dari *client*.

3. **Menjalankan Client**:
   Buka terminal baru dan jalankan perintah berikut untuk mengirimkan pesan dari *client* ke *server*:
   ```bash
   python Client.py
   ```
   Masukkan teks yang ingin dienkripsi dan dikirim ke *server*.

4. **Penggunaan Kunci**:
   Program menggunakan kunci hardcode `AABB0918` untuk enkripsi dan dekripsi pada *client* dan *server*.

## Pembagian Kerja
### Aryasatya Wiryawan (NRP 5025221256)
- Implementasi algoritma enkripsi dan dekripsi DES yang mendukung panjang teks lebih dari 64-bit.
- Mengembangkan program *client* untuk mengenkripsi pesan dan mengirimkan pesan terenkripsi ke *server*.
- Membuat dokumentasi program pada `README.md`.

## Contoh Hasil
1. **Pesan dari Client**:
   ```
   Masukkan teks: Halo, ini pesan terenkripsi!
   Pesan terenkripsi telah dikirim.
   ```

2. **Pesan pada Server**:
   ```
   Menunggu koneksi...
   Koneksi dari: ('localhost', 12345)
   Pesan terenkripsi diterima: <cipher text in hex>
   Pesan asli setelah dekripsi: Halo, ini pesan terenkripsi!
   ```

## Struktur Program
- `Client.py`: Program *client* yang mengenkripsi pesan dan mengirimnya ke *server*.
- `Server.py`: Program *server* yang menerima pesan terenkripsi dan mendekripsinya.


## Dependencies
- Python 3.x
- Library `pycryptodome` untuk enkripsi DES