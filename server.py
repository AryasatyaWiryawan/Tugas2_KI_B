import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# Fungsi dekripsi DES untuk teks panjang
def des_decrypt(cipher_text, key):
    des = DES.new(key, DES.MODE_ECB)
    pt_padded = des.decrypt(cipher_text)
    pt = unpad(pt_padded, DES.block_size)  # Hapus padding setelah dekripsi
    return pt.decode()

# Kunci yang sama dengan client
key = b'AABB0918'

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Menunggu koneksi...")

# Menerima koneksi
connection, address = server_socket.accept()
print("Koneksi dari:", address)

# Terima teks terenkripsi
cipher_text = connection.recv(1024)
print("Pesan terenkripsi diterima:", cipher_text.hex())

# Dekripsi pesan
plaintext = des_decrypt(cipher_text, key)
print("Pesan asli setelah dekripsi:", plaintext)

connection.close()
