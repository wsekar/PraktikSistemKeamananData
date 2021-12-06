import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
# menggenerate kunci publik dan kunci private
key = RSA.generate(1024, random_generator)

publickey = key.publickey()  # ekspor kunci publik untuk ditukarkan

# ENKRIPSI
encryptor = PKCS1_OAEP.new(publickey)  # menggunakan instansi dari PKCS1_OAEP
encrypted = encryptor.encrypt(
    b'Wibiati Sekar K., V3920061, D3 Teknik Informatika, wibiatisekark@student.uns.ac.id')  # pesan untuk dienkripsi

print('Hasil Enkripsi:', encrypted)  # menampilkan hasil enkripsi

# Update file .txt
f = open('enkripsi.txt', 'w')  # buka file txt, 'w' adalah write
f.write(str(encrypted))  # menambahkan hasil enkripsi
f.close()

f = open('enkripsi.txt', 'r')  # 'r' adalah read
message = f.read()

# Dekripsi
decryptor = PKCS1_OAEP.new(key)
# melakukan dekripsi dari pesan yang dienkripsi
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print('Hasil Dekripsi:', decrypted)  # menampilkan hasil desssskripsi

f = open('dekripsi.txt', 'w')  # buka file txt, 'w' adalah write
f.write(str(decrypted))  # menambahkan hasil dekripsi
f.close()
