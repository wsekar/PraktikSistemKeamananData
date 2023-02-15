# mengimport library string
import string
# membuat fungsi untuk membuat key dan matrix
def key_matrix_generation(key):
    # variabel atoz didefinisikan dengan pemanggilan module string yang di dalamnya terdapat ascii uppercase
    # fungsi replace untuk mengubah string, di mana ini akan mengubah huruf j menjadi huruf i
    atoz = string.ascii_uppercase.replace('J', 'I')
    # membuat key yaitu MADIUN
    key = 'MADIUN'
    # menampilkan key dengan fungsi print
    print("Key : " + key)
    # membuat matrix dengan ukuran 5 x 5
    key_matrix = ['' for i in range(5)]
    # variabel i untuk plaintext
    # variabel j untuk ciphertext
    i = 0
    j = 0

    for c in key:
        if c in atoz:
            key_matrix[i] += c

            atoz = atoz.replace(c, '.')
            j += 1
            if j > 4:
                i += 1
                j = 0
    for c in atoz:
        if c != '.':
            key_matrix[i] += c

            j += 1
            if j > 4:
                i += 1
                j = 0
    return key_matrix

# memanggil matrix yang telah dibuat dalam fungsi key_matrix_generation dengan key MADIUN
key_matrix = key_matrix_generation('MADIUN')
# menampilkan matrix
print(key_matrix)

# ciphertext yang akan didekripsi
ciphertext = "YAEAUQEYCLDQLDBMYEKW"
# variabel untuk menampung nilai string array yang berpasangan dari plaintext dan ciphertext
plaintextpairs = []
ciphertextpairs = []

i = 0
# perulangan while akan terus berjalan selama kondisi bernilai benar
# jika nilai i kurang dari jumlah panjang plaintext maka
while i < len(ciphertext):
    a = ciphertext[i]
    b = ciphertext[i+1]

    ciphertextpairs.append(a+b)
    i += 2
#menampilkan ciphertext dengan array
print(ciphertextpairs)

#dekripsi jikaa berada di baris yang sama
#hasilnya digeser 1 ke kiri
for pair in ciphertextpairs:
    applied_rule = False
    for row in key_matrix:
        if pair[0] in row and pair[1] in row:
            j0 = row.find(pair[0])
            j1 = row.find(pair[1])

            plaintextpair = row[(j0 + 4) % 5] + row[(j1+4) % 5]
            plaintextpairs.append(plaintextpair)
            applied_rule = True

    if applied_rule:
        continue
#dekripsi jikaa berada di column yang sama
#hasilnya di geser 1 ke atas
    for j in range(5):
        col = "".join([key_matrix[i][j] for i in range(5)])
        if pair[0] in col and pair[1] in col:
            i0 = col.find(pair[0])
            i1 = col.find(pair[1])

            plaintextpair = col[(i0 + 4) % 5] + col[(i1+4) % 5]
            plaintextpairs.append(plaintextpair)
            applied_rule = True

    if applied_rule:
        continue

    i0 = i1 = j0 = j1 = 0

#dekripsi jika berada di baris dan kolom yang berbeda
#hasilnya adalah berada secara vertikal
    for i in range(5):
        row = key_matrix[i]
        if pair[0] in row:
            i0 = i
            j0 = row.find(pair[0])

        if pair[1] in row:
            i1 = i
            j1 = row.find(pair[1])

    plaintextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
    plaintextpairs.append(plaintextpair)

#menampilkan plaintext hasil dekripsi
print(plaintextpairs)

#menampilkan plaintext dan ciphertext tanpa string dan pair
print("ciphertext : " + ciphertext)
print("plaintext : " + "".join(plaintextpairs))
