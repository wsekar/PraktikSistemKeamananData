# Implementation of Affine Cipher in Python
# a = kunci1
# b = kunci2
# m = panjang karakter(26)

# Algoritma Euclidean yang diperluas untuk menemukan invers modular
def egcd(a, b):  # fungsi untuk menentukan nilai gcd
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b  # gcd adalah b
    return gcd, x, y  # mengembalikan nilai gcd, x, dan y


def modinv(a, m):  # fungsi untuk menemukan nilai Modular Multiplicative Inverse (MMI)
    gcd, x, y = egcd(a, m)
    if gcd != 1:  # jika gcd tidak bernilai 1 maka
        return None  # tidak ada kembalian modulo
    else:
        return x % m  # mengembalikan nilai dari x yang di modulo


def affine_encrypt(text, key):  # fungsi enkripsi dengan parameter text dan key
    # berikut adalah fungsi enkripsi affine cipher
    '''
    C = (a*P + b) % 26 
    '''
    # mengembalikan cipher text
    # fungsi join untuk mengubah array list menjadi string
    # method chr berfungsi untuk mengembalikan nilai ascii, kemudian mencari karakter dari nilai ascii tersebut
    # ord berfungsi untuk mengubah sebuah karakter menjadi nilai ascii
    # nilai ascii dari variabel t dikurangi dengan nilai ascii dari A
    # key index [0] dikali dengan hasil pengurangan sebelumnya kemudian ditambahkan dengan key index[1]
    # hasil dari operasi perhitungan diatas kemudian di modulo 26 dan ditambahkan dengan nilai ascii dari A
    # fungsi text.upper().replace adalah untuk mengganti text yang diinputkan dengan huruf kapital semua
    return ''.join([chr(((key[0]*(ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


def affine_decrypt(cipher, key):  # fungsi enkripsi dengan parameter cipher dan key
    # berikut adalah fungsi dekripsi affine cipher
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    # mengembalikan plain text
    # fungsi join untuk mengubah array list menjadi string
    # method chr berfungsi untuk mengembalikan nilai ascii, kemudian mencari karakter dari nilai ascii tersebut
    # ord berfungsi untuk mengubah sebuah karakter menjadi nilai ascii
    # fungsi modinv untuk menemukan nilai mmi
    # key index[0] di modulo 26 kemudian dikali dengan hasil pengurangan nilai ascii variabel c dengan nilai ascii A dan dikurangi dengan key index [1]
    # nilai ascii dari variabel t dikurangi dengan nilai ascii dari A
    # hasil perhitungan tersebut kemudian di modulo 26 dan selanjutnya ditambah lagi dengan nilai ascii A
    return ''.join([chr(((modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                         % 26) + ord('A')) for c in cipher])

# fungsi main untuk menjalankan fungsi-fungsi yang telah dibuat sebelumnya


def main():
    # deklarasi text dan key
    text = 'KOTA'
    key = [5, 10]
    # kunci1 = 3, kunci2 = 9

    # memanggil fungsi enkripsi
    affine_encrypted_text = affine_encrypt(text, key)

    # menampilkan fungsi enkripsi
    print('Encrypted Text: {}'.format(affine_encrypted_text))

    # memanggil dan menampilkan fungsi dekripsi
    print('Decrypted Text: {}'.format
          (affine_decrypt(affine_encrypted_text, key)))


if __name__ == '__main__':
    main()
