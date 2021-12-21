#import library
import os
from Crypto import Cipher
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES


def getKey(keysize):  # fungsi untuk membuat kunci
    key = os.urandom(keysize)  # buat kunci secara random
    return key  # mengembalikan nilai key yang dibuat


def getIV(blocksize):  # fungsi untuk membuat blok
    iv = os.urandom(blocksize)  # buat blok secara random
    return iv  # mengembalikan nilai blok


# fungsi enkripsi dengan parameter filename, key, dan iv
def encrypt_image(filename, key, iv):
    BLOCKSIZE = 16  # membuat ukuran blok sepanjang 16
    # variabel encrypted_filename untuk menampung nama file yang dienkripsi dan disimpan
    encrypted_filename = "encrypted_" + filename

    with open(filename, "rb") as file1:  # membuka file sebagai file1
        data = file1.read()  # membaca file1

        # pada chiper akan melakukan method dari proses AES dengan key dan blocksize yang telah ditentukan
        cipher = AES.new(key, AES.MODE_CBC, iv)
        # proses enkripsi yang digunakan chipertext dan data/file gambar tadi
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))

        with open(encrypted_filename, "wb") as file2:  # membuka file tadi sebagai file2
            # file2 akan dituliskan pada parameter ciphertext di mana ini menampung proses enkripsi sebelumnya
            file2.write(ciphertext)

    return encrypted_filename  # mengembalikan file yang dienkripsi


# fungsi dekripsi dengan parameter filename, key, dan iv
def decrypt_image(filename, key, iv):
    BLOCKSIZE = 16  # membuat ukuran blok sepanjang 16
    # variabel decrypted_filename untuk menampung nama file yang didnkripsi dan disimpan
    decrypted_filename = "decrypted_" + filename

    with open(filename, "rb") as file1:  # membuka file sebagai file1
        data = file1.read()  # membaca file1

        # pada chiper akan melakukan method dari proses AES dengan key dan blocksize yang telah ditentukan
        cipher2 = AES.new(key, AES.MODE_CBC, iv)
        # proses dekripsi yang digunakan chiper2 dan data/file gambar tadi
        decrypt_data = unpad(cipher2.decrypt(data), BLOCKSIZE)

        with open(decrypted_filename, "wb") as file2:  # membuka file tadi sebagai file2
            file2.write(decrypt_data)
    return decrypted_filename  # mengembalikan file yang didekripsi


KEYSIZE = 16  # panjang key yang digunakan yaitu 16
BLOCKSIZE = 16  # panjang blok yang digunakan yaitu 16
filename = "dreamies_hotsa.jpg"  # nama file yang akan dienkripsi

key = getKey(KEYSIZE)  # variabel key untuk menampung nilai KEYSIZE
iv = getIV(BLOCKSIZE)  # variabel iv untu menampung nilai BLOCKSIZE

# variabel encrypted_filename menampung hasil dari fungsi encrypt_image
encrypted_filename = encrypt_image(filename, key, iv)
decrypted_filename = decrypt_image(
    encrypted_filename, key, iv)  # variabel decrypted_filename menampung hasil dari fungsi decrypt_image
