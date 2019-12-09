# amcc-desktop-sabila

Project pelatihan python dan github amcc desktop

## Bagaimana cara clone repository ?
1. buka halaman https://github.com/sabillaaa/amcc-desktop-sabila
2. klik tombol 'clone or download'
3. pilih ssh dan copy alamatnya , git@github.com:sabillaaa/amcc-desktop-sabila.git
4. setelah dicopy alamatnya maka masuk ke git bash kamu
5. pilih folder untuk menyimpannya dengan cara 'cd (nama foldernya)'
6. lalu masukkan 'git clone git@github.com:sabillaaa/amcc-desktop-sabila.git'

## Bagaimana cara commit dan push ?
1. setelah melakukan perubahan, jangan lupa untuk 'git status' buat melihat apa yang kita lakukan tadi
2. setelah itu lakukan penyimpanan dengan cara 'git commit -am "nama pesannya"' terlebih dahulu
3. lakukan 'git status' untuk memastikan perubahan yang sudah ter commit
4. setelah muncul tulisan 'nothing commit' maka lalukan 'git push'
5. jika tidak bisa maka 'git add .' dulu
6. lakukan 'git commit -am "nama pesannya"'
7. pastikan sudah ter commit, lalu 'git push'

## Kenapa pilih clone lewat ssh dari pada https ?
karena kalau lewat https itu nanti diminta untuk login lagi ke github, namun jika menggunakan ssh tidak

## Alasan menggunakan bahasa python
Efektifitas Python cukup terbukti dengan banyaknya jumlah pengguna Bahasa ini. Berbagai survei memasukkan Python dalam top-3 sebagai bahasa dengan penggunaan terbanyak, bersaing dengan Java dan PHP. Python dapat digunakan dalam mengakomodasi berbagai gaya pemrograman, termasuk structured, prosedural, berorientasi-objek, maupun fungsional. Python juga dapat berjalan pada berbagai sistem operasi yang tersedia. Beberapa pemanfaatan bahasa Python di antaranya:

1. Web development (server-side),
2. Software development,
3. Mathematics & data science,
4. Machine learning,
5. System scripting.

## Memulai dengan Python
Pastikan anda sudah mengisntal Python, dengan cara tulis "python --version" pada cmd/ git bash anda

## Bagaimana jika python belum ter-instal ?
Maka ikuti tautan berikut ini : https://www.dicoding.com/academies/86/tutorials/4738?from=4736 (Dengan syarat harus daftar akun dicoding terlebih dahulu)

## Hello World dengan python
Masuk ke direktori folder repository ini dengan cara:
```bash
cd /path/nama-direktori
```
catatan : path disini merupakan nama-nama direktori diatas direktori repositori ini, seperti misalnya Document
1. buat sebuah file baru dengan nama main.py, caranya seperti berikut
```
nano main.py
```
2. Masukkan code berikut di dalam main.py
```python
>>>print('Hello world')
Output : Hello world
```
3. Jalankan file tersebut dengan cara
```bash
python main.py
```

## Python Interpreter
1. Python interpreter merupakan program yang dibaca & dieksekusi pada sebuah sesi pada command line. Untuk masuk ke python interpreter, caranya sebagai berikut :
    -Buka CMD (windows) / Terminal (Linux/MacOS) >> Ketikkan 'Python'

```Python
PS C:\Users\Lenovo\Documents\Python\amcc-desktop-sabila>python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
>>>

```
## Menggunakan Modul
Modul merupakan set program yang sudah disediakan oleh python yang tinggal pakai, contohnya adalah seperti ini :

```Python
>>> import datetime
>>> datetime.datetime.now()
Output : datetime.datetime(2019, 12, 1, 21, 39, 43, 673959)

Untuk menampilkan tanggal dan jam pada saat ini. lalu selanjutnya, kita akan menggunakan modul 'random' untuk mengacak karakter alfabet seperti contoh code dibawah ini :
```
```Python
>>> import random
>>> import string
>>> def randomword(length):
...     letters = string.ascii_lowercase
...     return ''.join(random.choice(letters) for i in range(length))
...
>>> randomword(10)
Output : 'ogrpxncyyt'
```
Lalu kita bakal buat program untuk mengacak nama dari seluruh pelatih desktopbprogramming amcc dengan contoh kode berikut ini :
```Python
>>> def random_name():
...     name = ('david', 'sabil', 'peby', 'agung', 'yanuar')
...     return ''.join(random.choice(name) for i in range(1))
...
>>> random_name()
Output : 'yanuar'
```
## Menggunakan variabel
Variabel adalah tempat menyimpan data pada kode program, lalu bagaimana menggunakan variabel dan menampilkan isi variabel pada python?

```Python
>>> import datetime
>>> print ('Waktu sekarang',datetime.datetime.now())
Output : Waktu sekarang 2019-12-08 21:07:22.632088
```

```Python
>>> date = datetime.datetime.now()
>>> print(date)
Output : 2019-12-08 21:07:22.638074
```
#### Mengabungkan integer & string
```python
>>> number = 10
>>> string = 'Sabil'
>>> print(number, string)
Output : 10 Sabil
```
#### Simple Type
```python
>>> x = 15
>>> y = '15'
>>> z = 15.1
>>> sum1 = x+x
>>> sum2 = y+y
>>> sum3 = z+z
>>> print(x,y,z)
Output : 15 15 15.1
>>> print(type(x),type(y),type(z))
Output : <class 'int'> <class 'str'> <class 'float'>
```

## Menggunakan List
List adalah tipe data yang paling serbaguna yang tersedia dalam bahasa Python, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Hal penting tentang daftar adalah item dalam list tidak boleh sama jenisnya. lalu bagaimana menggunakan list dan menampilkan isi list pada python?
```python
>>> print(list(range(1,10)))
Output : [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(list(range(1,10,2)))
Output : [1, 3, 5, 7, 9]
```

#### Menjumlahkan nilai didalam list
```python
>>> student_grades = [4,12.1,6,9]
>>> mysum = sum(student_grades)
>>> print(mysum)
Output : 31.1
```

#### Panjang nilai didalam list
```python
>>> length = len(student_grades)
>>> print(length)
Output : 4
>>> mean = mysum/length
>>> print(mean)
Output : 7.775
```

#### Mencari jumlah nilai dalam list
```python
>>> student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
>>> print(student_grades.count(10.0))
Output : 3
>>> student = {'sabil':8.0, 'yanuar':7.0,'peby':9.0}
>>> print(student.values())
Output : dict_values([8.0, 7.0, 9.0])
>>> print(student.keys())
Output : dict_keys(['sabil', 'yanuar', 'peby'])
```

Secara umum, pernyataan pada bahasa pemrograman akan dieksekusi secara berurutan. Pernyataan pertama dalam sebuah fungsi dijalankan pertama, diikuti oleh yang kedua, dan seterusnya. Tetapi akan ada situasi dimana Anda harus menulis banyak kode, dimana kode tersebut sangat banyak. Jika dilakukan secara manual maka Anda hanya akan membuang-buang tenaga dengan menulis beratus-ratus bahkan beribu-ribu kode. Untuk itu Anda perlu menggunakan pengulangan di dalam bahasa pemrograman Python.

Di dalam bahasa pemrograman Python pengulangan dibagi menjadi 3 bagian, yaitu :
- While Loop
- For Loop
- Nested Loop

### While Loop
Pengulangan While Loop di dalam bahasa pemrograman Python dieksesusi statement berkali-kali selama kondisi bernilai benar atau `True`.

Dibawah ini adalah contoh penggunaan pengulangan While Loop.


```python
#Contoh penggunaan While Loop

count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print ("Good bye!")
```

### For Loop
Pengulangan `for` pada Python memiliki kemampuan untuk mengulangi item dari urutan apapun, seperti `list` atau `string`.

Dibawah ini adalah contoh penggunaan pengulangan For Loop.

```python
#Contoh pengulangan for sederhana
angka = [1,2,3,4,5]
for x in angka:
    print(x)
```
```python
#Contoh pengulangan for
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print "Saya suka makan", makanan
```
    
### Nested Loop
Bahasa pemrograman Python memungkinkan penggunaan satu lingkaran di dalam loop lain. Bagian berikut menunjukkan beberapa contoh untuk menggambarkan konsep tersebut. 

Dibawah ini adalah contoh penggunaan Nested Loop.

```python
#Contoh penggunaan Nested Loop

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print i, " is prime"
    i = i + 1

print "Good bye!"
```
