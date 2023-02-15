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

# membuat plaintext yang akan dienkripsi
plaintext = "WIBIATISEKARKINASIH"
# variabel untuk menampung nilai string array yang berpasangan dari plaintext dan ciphertext
plaintextpairs = []
ciphertextpairs = []

i = 0
# perulangan while akan terus berjalan selama kondisi bernilai benar
# jika nilai i kurang dari jumlah panjang plaintext maka
while i < len(plaintext):
    # variabel a untuk menampung plaintext dari huruf pertama dan b untuk huruf kedua
    a = plaintext[i]
    b = ''
    if (i+1) == len(plaintext):  # jika panjang plaintext adalah kelebihan/kekurangan 1 (ganjil)
        b = 'X'  # maka variabel b untuk membuat huruf tambahan yaitu 'X'
    else:
        b = plaintext[i+1]

    if a != b:  # pengecekan apakah a tidak sama dengan b, ini untuk membuat agar pasangan huruf tidak kembar
        #jika benar maka akan menjalankan fungsi di bawah ini
        plaintextpairs.append(a+b) #fungsi append adalah untuk menambahkan nilai array pada urutan terakhir.
        i += 2
    else:
        #jika salah maka akan menjalankan fungsi di bawah ini di mana nilai b digantikan dengan 'X'
        plaintextpairs.append(a+'X')
        i += 1

#menampilkan plainteks dengan array
print(plaintextpairs)

#perulangan for digunakan untuk melakukan iterasi dari sebuah nilai sequence(list, string, dll)
#untuk pasangan pada variabel plaintextpairs
for pair in plaintextpairs:
    applied_rule = False
    #untuk baris dalam variabel key_matrix
    for row in key_matrix:
        if pair[0] in row and pair[1] in row: #pengecekan apakah pasangan plaintext index 0 dan 1 berada di baris yang sama:
            #jika iya maka akan menjalankan script di bawah ini
            #fungsi row.find() untuk mendeteksi apakah dalam baris tersebut terdapat substring
            j0 = row.find(pair[0]) 
            j1 = row.find(pair[1]) 

            #membuat variabel ciphertextpair untuk menampung array dari pasangan index 0 dan index 1
            #menjalankan fungsi row karena untuk mengecek apakah pasangan berada pada baris yang sama
            #j0+1 maksudnya ciphertext digeser 1 ke kanan dari index tersebut, begitu pula untuk j1+1
            # %5 karena dalam matrix tersebut terdapat 5 baris
            ciphertextpair = row[(j0 + 1) % 5] + row[(j1+1) % 5]
            #menambahkan nilai array dari variabel ciphertextpair 
            ciphertextpairs.append(ciphertextpair)
            applied_rule = True

    if applied_rule:
        continue
    
    #j berada di range 5
    for j in range(5):
        #fungsi join untuk menyatukan banyak string ke dalam sebuah string
        col = "".join([key_matrix[i][j] for i in range(5)]) 
        if pair[0] in col and pair[1] in col:
            i0 = col.find(pair[0])
            i1 = col.find(pair[1])

            #membuat variabel ciphertextpair untuk menampung array dari pasangan index 0 dan index 1
            #menjalankan fungsi column karena untuk mengecek apakah pasangan berada pada column yang sama
            #i0+1 maksudnya ciphertext digeser 1 ke bawah dari index tersebut, begitu pula untuk i1+1
            # %5 karena dalam matrix tersebut terdapat 5 column
            ciphertextpair = col[(i0 + 1) % 5] + col[(i1+1) % 5]
            #menambahkan nilai array dari variabel ciphertextpair 
            ciphertextpairs.append(ciphertextpair)
            applied_rule = True

    if applied_rule:
        continue

    i0 = 0
    i1 = 0
    j0 = 0
    j1 = 0

    #i berada di range 5
    for i in range(5):
        #membuat baris dari matrix yang berisikan nilai dari plaintext
        row = key_matrix[i]
        #pengecekan jika pasangan plaintext berada di baris dan kolom yang berbeda
        #ciphertext ditentukan secara vertikal dari plaintextnya
        #i0 merupakan plaintext
        #j0 merupakan ciphertext
        if pair[0] in row:
            i0 = i
            j0 = row.find(pair[0])
        #i1 merupakan plaintext
        #j1 merupakan ciphertext
        if pair[1] in row:
            i1 = i
            j1 = row.find(pair[1])
    # variabel ciphertextpair didefinisikan untuk menampung data dari plaintext dan ciphertext
    # pasangan untuk plaintext i0 yaitu ciphertext j1, begitu pula sebaliknya.
    ciphertextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
    #menambahkan nilai array dari variabel ciphertextpair 
    ciphertextpairs.append(ciphertextpair)
#menampilkan ciphertext
print(ciphertextpairs)

#menampilkan plaintext dan ciphertext tanpa string dan pair
print("plaintext : " + plaintext)
print("ciphertext : " + "".join(ciphertextpairs))
