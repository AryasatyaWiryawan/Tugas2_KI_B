import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

# Fungsi enkripsi DES untuk teks panjang
def des_encrypt(pt, key):
    des = DES.new(key, DES.MODE_ECB)
    pt = pt.encode()  # Konversi ke bytes
    pt_padded = pad(pt, DES.block_size)  # Pad input ke ukuran blok DES
    cipher_text = des.encrypt(pt_padded)
    return cipher_text

# Kunci (hardcode 8 karakter / 64-bit)
key = b'AABB0918'

# Inisialisasi socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Masukkan plaintext
plaintext = input("Masukkan teks: ")
cipher_text = des_encrypt(plaintext, key)

# Kirim teks terenkripsi
client_socket.send(cipher_text)
print("Pesan terenkripsi telah dikirim.")
client_socket.close()
