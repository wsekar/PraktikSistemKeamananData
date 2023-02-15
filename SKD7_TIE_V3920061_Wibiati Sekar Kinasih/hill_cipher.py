import math  # import modul math
import string  # import modul string
import sys  # import modul sys

import numpy as np #import modul numpy
from sympy import Matrix #import modul matrix 

# membuat daftar menu
def menu():
    while True:
        print("---- Hill Cipher ----\n")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Quit\n")
        try:
            # memilih menu yang dipilih dengan memasukkan angka pilihan menu
            choice = int(input("Pilih: "))
            #menu yang dapat dipilih mulai dari angka 1 sampai 3
            if 1 <= choice <= 3: 
                return choice #mengembalikan nilai choice
            else: #jika salah maka akan diminta kembali untuk memasukkan angka antara 1-3
                print("\nMasukkan angka 1, 2, atau 3\n")
        except ValueError:
            print("\nMasukkan angka 1, 2, atau 3\n")
        input("Tekan Enter untuk melanjutkan\n")

# membuat fungsi untuk untuk mengubah alphabet ke angka dan angka ke alphabet.
# angka yang dimaksud merupakan nomor alphabet (0-25)
def get_alphabet():
    #variabel alphabet untuk menampung angka yang diubah dari alphabet
    alphabet = {}
    #perulangan for digunakan untuk melakukan iterasi dari sebuah nilai sequence (list, string, dll)
    for character in string.ascii_uppercase: #perulangan karakter dalam library string untuk menggunakan ascii uppercase
        alphabet[character] = string.ascii_uppercase.index(character) #alphabet diubah menjadi nilai ascii uppercase berdasarkan index urutannya

    #variabel reverse_alphabet untuk menampung alphabet yang diubah dari angka
    reverse_alphabet = {}
    for key, value in alphabet.items():
        reverse_alphabet[value] = key

    return alphabet, reverse_alphabet #mengembalikan nilai alphabet dan reverse_alphabet

#membuat fungsi untuk menampung text yang diinputkan
#pengecekan apakah yang diinputkan merupakan alphabet
def get_text_input(message, alphabet):
    while True:
        text = input(message) # untuk menginputkan text
        text = text.upper() #membuat text menjadi huruf kapital
        if all(keys in alphabet for keys in text): #key dalam alphabet untuk key dalam text
            return text #mengembalikan nilai text
        else: #jika salah, maka memunculkan pemberitahuan bahwa hanya dapat menginputkan alphabet a-z atau A-Z
            print(
                "\nText yang diinputkan hanya berupa karakter alphabet[A-Z] atau [a-z]")

#fungsi untuk mengecek apakah panjang key adalah persegi
def is_square(key):
    #panjang key(matrix) akan disimpan pada variabel key_length
    key_length = len(key)
    if 2 <= key_length == int(math.sqrt(key_length)) ** 2:
        return True
    else:
        return False

#fungsi untuk membuat matrix k untuk key
def get_key_matrix(key, alphabet):
    #key akan disimpan dalam variabel k dengan tipe data list
    k = list(key)
    #variabel m untuk menampung perhitungan yang dihasilkan oleh akar kuadrat dari panjang variabel k
    m = int(math.sqrt(len(k)))
    for (i, character) in enumerate(k):
        k[i] = alphabet[character]
    return np.reshape(k, (m, m))


# melengkapi plaintext jika panjang alphabetnya ganjil
def get_text_matrix(text, m, alphabet):
    matrix = list(text) #variable matrix menampung data text dengan tipe data list
    remainder = len(text) % m #variabel remainder menampung data panjang text yang dimodulo dengan m. 
    for (i, character) in enumerate(matrix):
        matrix[i] = alphabet[character]
    if remainder != 0: #pengecekan jika remainder tidak sama dengan 0,
        for i in range(m - remainder): 
            #alphabet yang ditambahkan merupakan urutan ke-25 yaitu 'Z'
            matrix.append(25)
    return np.reshape(matrix, (int(len(matrix) / m), m)).transpose()

# enkripsi plaintext dan mengembalikan nilai ciphertext matrix
def encrypt(key, plaintext, alphabet):
    m = key.shape[0]
    m_grams = plaintext.shape[1]

    #enkripsi plaintext dengan kunci yang disediakan k, hitung matriks c dari ciphertext
    ciphertext = np.zeros((m, m_grams)).astype(int) #mengembalikan array baru dengan tipe data integer
    for i in range(m_grams):
        ciphertext[:, i] = np.reshape( #mengubah bentuk array
            np.dot(key, plaintext[:, i]) % len(alphabet), m)
    return ciphertext

# mengubah matrix menjadi text, sesuai dengan nomor alphabet
def matrix_to_text(matrix, order, alphabet):
    if order == 't':
        text_array = np.ravel(matrix, order='F')
    else:
        text_array = np.ravel(matrix)
    text = ""
    for i in range(len(text_array)):
        text = text + alphabet[text_array[i]]
    return text

# pengecekan apakah kuncinya dapat dibalik(inverse) sehingga mengembalikan kebalikan dari matrix
def get_inverse(matrix, alphabet):
    alphabet_len = len(alphabet) #menampung data panjang alphabet (26)
    #menghitung nilai modular multiplicative invers (mmi)
    #fungsi math.gcd untuk mengembalikan gcd(FPB)
    #fungsi np.linalg.det untuk menghitung determinan dari matrix
    if math.gcd(int(round(np.linalg.det(matrix))), alphabet_len) == 1:
        matrix = Matrix(matrix)
        return np.matrix(matrix.inv_mod(alphabet_len))
    else:
        return None #tidak mengembalikan nilai apapun

# fungsi dekripsi dan mengembalikan matrix dari plaintext
def decrypt(k_inverse, c, alphabet):
    return encrypt(k_inverse, c, alphabet) 

def main():
    while True:
        #memilih fungsi apa yang ingin dijalankan
        choice = menu()

        # memanggil fungsi get_alphabet yang di dalamnya terdapat variabel alphabet (alphabet to number) dan reverse_alphabet (number to alphabet) 
        alphabet, reverse_alphabet = get_alphabet()

        #menjalankan fungsi yang dipilih
        #jika pilihan 1
        if choice == 1:
            # memasukkan plaintext dan key yang akan dienkripsi
            plaintext = get_text_input(
                "\nMasukkan text yang akan dienkripsi: ", alphabet)
            key = get_text_input("Masukkan kunci ([a-z] atau [A-Z]): ", alphabet) #kunci yang dimasukkan adalah berupa alphabet

            if is_square(key):
                #memanggil fungsi get_key_matrix untuk menampilkan key matrix k
                k = get_key_matrix(key, alphabet)
                print("\nKey Matrix:\n", k)

                #Memanggil fungsi get_text_matrix untuk menampilkan plaintext dalam bentuk nomor alphabetnya
                p = get_text_matrix(plaintext, k.shape[0], alphabet)
                print("Plaintext Matrix:\n", p)

                #tekan enter untuk melanjutkan proses enkripsi
                input("\nTekan Enter untuk melanjutkan proses enkripsi")
                # Enkripsi plaintext
                c = encrypt(k, p, alphabet)

                #Mengubah ciphertext matrix ke dalam bentuk alphabet
                ciphertext = matrix_to_text(c, "t", reverse_alphabet)

                print("\nText telah dienkripsi\n")
                print("Ciphertext: ", ciphertext)
                print("Ciphertext Matrix:\n", c, "\n")
            else:
                print("\nPanjang matrix harus berbentuk persegi dan >=2\n")

        elif choice == 2:
            #memasukkan ciphertext dan key yang akan didekripsi
            ciphertext = get_text_input(
                "\nMasukkan ciphertext yang akan didekripsi: ", alphabet)
            key = get_text_input("Masukkan kunci ([a-z] atau [A-Z]): ", alphabet) #kunci yang dimasukkan adalah berupa alphabet

            if is_square(key):
                #memanggil fungsi get_key_matrix untuk menampilkan key matrix k
                k = get_key_matrix(key, alphabet)

                # pengecekan apakah kuncinya dapat dibalik(inverse) sehingga mengembalikan kebalikan dari matrix
                k_inverse = get_inverse(k, alphabet)

                if k_inverse is not None:
                    #mendapatakan matrix dari ciphertext
                    c = get_text_matrix(
                        ciphertext, k_inverse.shape[0], alphabet)

                    print("\nKey Matrix:\n", k)
                    print("Ciphertext Matrix:\n", c)

                    input("\nTekan Enter untuk melanjutkan proses dekripsi.")

                    # dekripsi ciphertext
                    p = decrypt(k_inverse, c, alphabet)

                    #mengubah plaintext matrix ke dalam bentuk alphabet
                    plaintext = matrix_to_text(p, "t", reverse_alphabet)

                    print("\nText telah dienkripsi\n")
                    print("Plaintext: ", plaintext)
                    print("Plaintext Matrix:\n", p, "\n")
                else:
                    print("\nMatrix tidak dapat dibalik(inverse)\n")
            else:
                print("\nPanjang matrix harus berbentuk persegi dan >=2\n")

        elif choice == 3:
            sys.exit(0)
        input("Tekan Enter untuk melanjutkan\n")

if __name__ == '__main__':
    main()
