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
print('Hello world')
```
3. Jalankan file tersebut dengan cara
```bash
python main.py
```
4. Hasil output harusnya sesuai dengan inputannya, yaitu:
```
Hello world
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
datetime.datetime(2019, 12, 1, 21, 39, 43, 673959)

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
'ogrpxncyyt'
```
Lalu kita bakal buat program untuk mengacak nama dari seluruh pelatih desktopbprogramming amcc dengan contoh kode berikut ini :
```Python
>>> def random_name():
...     name = ('david', 'sabil', 'peby', 'agung', 'yanuar')
...     return ''.join(random.choice(name) for i in range(1))
...
>>> random_name()
'yanuar'
```
## Menggunakan variabel
Variabel adalah tempat menyimpan data pada kode program, lalu bagaimana menggunkan variabel dan menampilkan isi variabel pada python?

```Python
>>> import datetime
>>> print ('Waktu sekarang',datetime.datetime.now())
Waktu sekarang 2019-12-08 21:07:22.632088
```

```Python
>>>"""Variabel"""
>>> date = datetime.datetime.now()
>>> print(date)
2019-12-08 21:07:22.6380744
```

```python
>>> """Mengabungkan integer & string"""
'Mengabungkan integer & string'
>>> number = 10
>>> string = 'Sabil'
>>> print(number, string)
10 Sabil
```
