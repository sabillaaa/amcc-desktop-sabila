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

#### Membuat List Python

List adalah tipe data yang paling serbaguna yang tersedia dalam bahasa Python, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Hal penting tentang daftar adalah item dalam list tidak boleh sama jenisnya.

Membuat list sangat sederhana, tinggal memasukkan berbagai nilai yang dipisahkan koma di antara tanda kurung siku. Dibawah ini adalah contoh sederhana pembuatan list dalam bahasa Python.

```python
#Contoh sederhana pembuatan list pada bahasa pemrograman python
list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
```

#### Akses Nilai Dalam List Python

Untuk mengakses nilai dalam list python, gunakan tanda kurung siku untuk mengiris beserta indeks atau indeks untuk mendapatkan nilai yang tersedia pada indeks tersebut.

Berikut adalah contoh cara mengakses nilai di dalam list python :


```python
#Cara mengakses nilai di dalam list Python

list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
```

Setelah Anda mengeksekusi kode diatas, hasilnya akan seperti dibawah ini :

`list1[0]: fisika`
`list2[1:5]: [2, 3, 4, 5]`

#### Update Nilai Dalam List Python

Anda dapat memperbarui satu atau beberapa nilai di dalam list dengan memberikan potongan di sisi kiri operator penugasan, dan Anda dapat menambahkan nilai ke dalam list dengan metode append (). Sebagai contoh :


```python
list = ['fisika', 'kimia', 1993, 2017]
print ("Nilai ada pada index 2 : ", list[2])

list[2] = 2001
print ("Nilai baru ada pada index 2 : ", list[2])
```

#### Hapus Nilai Dalam List Python

Untuk menghapus nilai di dalam list python, Anda dapat menggunakan salah satu pernyataan del jika Anda tahu persis elemen yang Anda hapus. Anda dapat menggunakan metode remove() jika Anda tidak tahu persis item mana yang akan dihapus. Sebagai contoh :

```python
#Contoh cara menghapus nilai pada list python

list = ['fisika', 'kimia', 1993, 2017]

print (list)
del list[2]
print ("Setelah dihapus nilai pada index 2 : ", list)
```

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
#### Operasi Dasar Pada List Python

List Python merespons operator + dan * seperti string; Itu artinya penggabungan dan pengulangan di sini juga berlaku, kecuali hasilnya adalah list baru, bukan sebuah String.

Sebenarnya, list merespons semua operasi urutan umum yang kami gunakan pada String di bab sebelumnya. Dibawah ini adalah tabel daftar operasi dasar pada list python.

| Python Expression	| Hasil		| Penjelasan	| 
| --- | --- | --- |
| `len([1, 2, 3, 4])`		| `4`	| Length	| 
| `[1, 2, 3] + [4, 5, 6]`	| 	`[1, 2, 3, 4, 5, 6]`	| 	Concatenation	| 
| `['Halo!'] * 4`		| `['Halo!', 'Halo!', 'Halo!', 'Halo!']`	| 	Repetition	| 
| `2 in [1, 2, 3]`	| `	True`	| 	Membership	| 
| `for x in [1,2,3] : print (x,end = ' ')`	| 	`1 2 3`		| Iteration	| 

#### Indexing, Slicing dan Matrix Pada List Python

Karena list adalah urutan, pengindeksan dan pengiris bekerja dengan cara yang sama untuk list seperti yang mereka lakukan untuk String.

Dengan asumsi input berikut :

`L = ['C++'', 'Java', 'Python']`

 | Python Expression | 	Hasil | 	Penjelasan | 
 | --- | --- | --- | 
 | `L[2]`	 | `'Python'` | 	Offset mulai dari nol | 
 | `L[-2]` | 	`'Java'` | 	Negatif: hitung dari kanan | 
 | `[1:]`	 | `['Java', 'Python']` | 	Slicing mengambil bagian | 
 
#### Method dan Fungsi Build-in Pada List Python

Python menyertakan fungsi built-in sebagai berikut :

| Python Function | 	Penjelasan | 
| --- | --- |
| cmp(list1, list2)	# |  Tidak lagi tersedia dengan Python 3 | 
| len(list)	 | Memberikan total panjang list. | 
| max(list)	 | Mengembalikan item dari list dengan nilai maks. | 
| min(list)	 | Mengembalikan item dari list dengan nilai min. | 
| list(seq)	 | Mengubah tuple menjadi list. | 

Python menyertakan methods built-in sebagai berikut

 | Python Methods | 	Penjelasan | 
 | --- | --- | 
 | list.append(obj)	 | Menambahkan objek obj ke list | 
 | list.count(obj) | 	Jumlah pengembalian berapa kali obj terjadi dalam list | 
 | list.extend(seq) | 	Tambahkan isi seq ke list | 
 | list.index(obj) | 	Mengembalikan indeks terendah dalam list yang muncul obj | 
 | list.insert(index, obj)	 | Sisipkan objek obj ke dalam list di indeks offset | 
 | list.pop(obj = list[-1])	 | Menghapus dan mengembalikan objek atau obj terakhir dari list | 
 | list.remove(obj) | 	Removes object obj from list | 
 | list.reverse() | 	Membalik list objek di tempat | 
 | list.sort([func])	 | Urutkan objek list, gunakan compare func jika diberikan | 

## Loop
Secara umum, pernyataan pada bahasa pemrograman akan dieksekusi secara berurutan. Pernyataan pertama dalam sebuah fungsi dijalankan pertama, diikuti oleh yang kedua, dan seterusnya. Tetapi akan ada situasi dimana Anda harus menulis banyak kode, dimana kode tersebut sangat banyak. Jika dilakukan secara manual maka Anda hanya akan membuang-buang tenaga dengan menulis beratus-ratus bahkan beribu-ribu kode. Untuk itu Anda perlu menggunakan pengulangan di dalam bahasa pemrograman Python.

Di dalam bahasa pemrograman Python pengulangan dibagi menjadi 3 bagian, yaitu :
- While Loop
- For Loop
- Nested Loop

#### While Loop
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

#### For Loop
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
    
#### Nested Loop
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
## Number
Number adalah tipe data Python yang menyimpan nilai numerik. Number adalah tipe data yang tidak berubah. Ini berarti, mengubah nilai dari sejumlah tipe data akan menghasilkan objek yang baru dialokasikan.

Objek Number dibuat saat Anda memberikan nilai pada-nya. Sebagai contoh : `angkaPertama = 1`
`angkaKedua = 33 `

Python mendukung beberapa tipe data Number diantaranya :
- Int
- Float
- Complex

Berikut ini adalah beberapa contoh dari Tipe data Number pada Python :

| Int |	Float |	Complex |
| --- | --- | --- |
| 20 |	0.1 |	3.14j |
| 300 |	1.20 |	35.j |
| -13 |	-41.2 |	3.12e-12j |
| 020 |	32.23+e123 |	.873j |
| -0103 |	-92. |	-.123+0J |
| -0x212 |	-32.52e10 |	3e+123J |
| 0x56 |	60.2-E13 |	4.31e-4j |


#### Konversi Tipe Data Number Python
Pada Python Anda bisa mengkonversi tipe data dengan menggunakan fungsi. Dibawah ini adalah beberapa fungsi untuk mengkonversi tipe data number Python. 
- `int(x)`
untuk meng-konversi x menjadi plain integer.
- `long(x)`
untuk meng-konversi x menjadi long integer.
- `float(x)`
untuk meng-konversi x menjadi floating point number.
- `complex(x)`
untuk meng-konversi x menjadi complex number dengna real part x dan imaginary part zero.
- `complex(x, y)`
untuk meng-konversi x dan y menjadi complex number dengan real part x dan imaginary part y. x dan numeric expressions y. 


#### Fungsi Matematika Python
Pada bahasa pemrograman Python terdapat fungsi untuk melakukan perhitungan matematis, berikut adalah daftarnya :

| Nama |	Penggunaan |	Penjelasan |
| --- | --- | --- |
| Absolute |	`abs(x)` |	Nilai absolut dari x:(positive) jarak antara x and 0. |
| Ceiling |	`ceil(x)` |	Ceiling dari x: integer terkecil yang kurang dari x. |
| Cmp |	`cmp(x, y)` |	-1 if x < y, 0 if x == y, or 1 if x > y. Tidak berlaku lagi dengan Python 3. Sebaliknya gunakan return (x>y)-(x |
| Eksponen |	`exp(x)` |	Nilai eksponen dari x: ex |
| Fabs |	`fabs(x)` |	Nilai absolut dari x. |
| Floor |	`floor(x)` |	The floor of x: the largest integer not greater than x. |
| Floor |	`floor(x)` |	Nilai dasar dari x: internet terbesar tidak lebih besar dari x. |
| Log |	`log(x)` |	Logaritma dari x, untuk x > 0. |
| Log 10 |	`log10(x)` |	Basis 10 logaritma dari x, untuk x > 0. |
| Max |	`max(x1, x2,...)`	 | Argumen terbesar: Nilai terdekat dengan tak terhingga positif |
| Min |	`min(x1, x2,...)` |	Argumen terkecil: nilai yang paling mendekati tak berhingga negatif. |
| Modf |	`modf(x)` |	Bagian pecahan dan bilangan bulat dari x dalam tupel dua item. Kedua bagian memiliki tanda yang sama dengan x. Bagian integer dikembalikan sebagai float. |
| Pow |	`pow(x, y)` |	Nilai x ** y. |
| Round |	`round(x [,n])` |	X dibulatkan menjadi n digit dari titik desimal. Putaran Python jauh dari nol sebagai tie-breaker: round (0.5) adalah 1.0 dan round (-0.5) adalah -1.0. |
| Akar Kuadrat |	`sqrt(x)` |	Akar kuadrat x untuk x> 0. |


#### Fungsi Nomor Acak Python
Nomor acak digunakan untuk aplikasi permainan, simulasi, pengujian, keamanan, dan privasi. Python mencakup fungsi berikut yang umum digunakan. Berikut adalah daftarnya :

| Nama | 	Penggunaan | 	Penjelasan | 
| --- | --- | --- |
| Choice | 	`choice(seq)` | 	Item acak dari list, tuple, atau string. | 
| RandRange | 	`randrange ([start,] stop [,step])` | 	Elemen yang dipilih secara acak dari jangkauan (start, stop, step). | 
| Random | 	`random()` | 	A random float r, sehingga 0 kurang dari atau sama dengan r dan r kurang dari 1 | 
| Seed | 	`seed([x])` | 	Menetapkan nilai awal integer yang digunakan dalam menghasilkan bilangan acak. Panggil fungsi ini sebelum memanggil fungsi modul acak lainnya. Tidak ada pengembalian | 
| Shuffle | 	`shuffle(lst)` | 	Mengacak daftar dari daftar di tempat. Tidak ada pengembalian | 
| Floor	| `floor(x)`	 | The floor of x: the largest integer not greater than x. | 
| Uniform| 	`uniform(x, y)` | 	Sebuah float acak r, sedemikian rupa sehingga x kurang dari atau sama dengan r dan r kurang dari y. | 


#### Fungsi Trigonometri Python
Python mencakup fungsi berikut yang melakukan perhitungan trigonometri. Berikut adalah daftarnya :

| Nama |	Penggunaan	Penjelasan |
| --- | --- | --- |
| Acos |	`acos(x)` |	Kembalikan kosinus x, di radian. |
| Asin |	`asin(x)` |	Kembalikan busur sinus x, dalam radian. |
| Atan |	`atan(x)` |	Kembalikan busur singgung x, di radian. |
| Atan 2 |	`atan2(y, x)`	 | Kembali atan (y / x), di radian. |
| Kosinus |	`cos(x)` |	Kembalikan kosinus x radian. |
| Hypot	 | `hypot(x, y)` |	Kembalikan norma Euclidean, sqrt (x * x + y * y). |
| Sin |	`sin(x)` |	Kembalikan sinus dari x radian. |
| Tan |	`tan(x)` |	Kembalikan tangen x radian. |
| Derajat |	`degrees(x)` |	Mengonversi sudut x dari radian ke derajat. |
| Radian |	`radians(x)` |	Mengonversi sudut x dari derajat ke radian. |

#### Konstanta Matematika Python
Modul ini juga mendefinisikan dua konstanta matematika. Berikut adalah daftarnya :

| Nama |	Penggunaan	| Penjelasan| 
| --- | --- | --- |
| Pi	| `pi`	| Konstanta Pi matematika| 
| e	| `e`	| Konstanta e matematika| 

## String
String adalah jenis yang paling populer di bahasa pemrograman. Kita bisa membuatnya hanya dengan melampirkan karakter dalam tanda kutip. Python memperlakukan tanda kutip tunggal sama dengan tanda kutip ganda. Membuat string semudah memberi nilai pada sebuah variabel.

Dibawah ini adalah contoh sederhana dari sebuah string pada bahasa pemrograman Python.

```python
print("Hello World")
```

#### Mengakses Nilai dalam String

Python tidak menggunakan tipe karakter titik koma ; Ini diperlakukan sebagai string dengan panjang satu, sehingga juga dianggap sebagai substring.

Untuk mengakses substring, gunakan tanda kurung siku untuk mengiris beserta indeks atau indeks untuk mendapatkan substring Anda. Sebagai contoh : 

```python
name = 'John Doe' message = "John Doe belajar bahasa python di Belajarpython"
print ("name[0]: ", name[0])
print ("message[1:4]: ", message[1:4])
```

Bila kode diatas dieksekusi, maka akan menghasilkan hasil sebagai berikut :

`name[0]: J`
`message[1:4]: ohn `


#### Mengupdate String

Anda dapat "memperbarui" string yang ada dengan (kembali) menugaskan variabel ke string lain. Nilai baru dapat dikaitkan dengan nilai sebelumnya atau ke string yang sama sekali berbeda sama sekali. Sebagai contoh

```python
message = 'Hello World'
print ("Updated String :- ", message[:6] + 'Python')
```

Bila kode diatas dieksekusi, maka akan menghasilkan hasil sebagai berikut :

`Updated String :- Hello Python`

#### Escape Characters / Karakter Escape Python

Dibawah ini adalah tabel dari daftar karakter escape atau karakter non-printable yang dapat diwakili/ditulis dengan awalan notasi backslash.

| Notasi Backslash	 | Karakter Hexadecimal	 | Penjelasan |
| --- | --- | --- |
| \a | 	0x07 | 	Bell atau alert |
| \b | 	0x08 | 	Backspace |
| \cx | 	 | 	Control-x |
| \C-x	 |  | 	Control-x |
| \e | 	0x1b | 	Escape |
| \f | 	0x0c | 	Formfeed |
| \M-\C-x | 	 | 	Meta-Control-x |
| \n | 	0x0a | 	Newline |
| \nnn | 	 | 	Octal notation, dimana n berada di range 0.7 |
| \r | 	0x0d | 	Carriage return |
| \s | 	0x20 | 	Space |
| \t | 	0x09 | 	Tab |
| \v | 	0x0b | 	Vertical tab |
| \x | 	 | 	Character x |
| \xnn	 |   | 	Notasi Hexadecimal, dimana n berada di range 0.9, a.f, atau A.F |


#### Operator Spesial String Python

Asumsikan variabel string adalah 'Belajar' dan variabel b adalah 'Python', lalu dibawah ini adalah operator yang bisa dipakai pada kedua string di variabel tersebut. `a = "Belajar"` `b = "Python"`


Berikut adalah daftar operator spesial string pada Python : 

| Operator | 	Contoh	Penjelasan | 

| + | 	a + b  | akan menghasilkan BelajarPython	Concatenation - Menambahkan nilai pada kedua sisi operator | 
| * | 	a*2  | akan menghasilkan BelajarBelajar	Pengulangan - Membuat string baru, menggabungkan beberapa salinan dari string yang sama | 
| [] | 	a[1]  | akan menghasilkan e	Slice - Memberikan karakter dari indeks yang diberikan | 
| [ : ] | 	a[1:4]  | akan menghasilkan ela	Range Slice - Memberikan karakter dari kisaran yang diberikan | 
| in | 	B in a  | akan menghasilkan 1	Keanggotaan - Mengembalikan nilai true jika ada karakter dalam string yang diberikan | 
| not in | 	Z not in a  | akan menghasilkan 1	Keanggotaan - Mengembalikan nilai true jika karakter tidak ada dalam string yang diberikan | 
| r/R | 	print r'\n' prints \n dan print R'\n'prints \n	Raw String -  | Menekan arti aktual karakter Escape. Sintaks untuk string mentah sama persis dengan string biasa kecuali operator string mentah, huruf "r", yang mendahului tanda petik. "R" bisa berupa huruf kecil (r) atau huruf besar (R) dan harus ditempatkan tepat sebelum tanda kutip pertama. | 
| %	 |  | 	Format - Melakukan format String | 

#### Operator Format String Python

Salah satu fitur Python yang paling keren adalah format string operator %. Operator ini unik untuk string dan membuat paket memiliki fungsi dari keluarga printf C () C. 
berikut adalah contoh sederhananya : `print ("My name is %s and weight is %d kg!" % ('Zara', 21)) `


Berikut adalah daftar lengkap simbol yang bisa digunakan bersamaan dengan % : 

| Operator | 	Penjelasan | 
| --- | --- |
| %c | 	character | 
| %s | 	Konversi string melalui str () sebelum memformat | 
| %i | 	Dianggap sebagai bilangan bulat desimal | 
| %d | 	Dianggap sebagai bilangan bulat desimal | 
| %u | 	Unsigned decimal integer | 
| %o | 	Bilangan bulat oktal | 
| %x | 	Bilangan bulat heksadesimal (huruf kecil) | 
| %X | 	Bilangan bulat heksadesimal (huruf besar) | 
| %e | 	Notasi eksponensial (dengan huruf kecil 'e') | 
| %E | 	Notasi eksponensial (dengan huruf besar 'E') | 
| %f | 	Bilangan real floating point | 
| %g | 	Yang lebih pendek dari% f dan% e | 
| %G | 	Lebih pendek dari% f dan% E | 

#### Triple Quote Python

Python triple quotes digunakan dengan membiarkan string untuk ditulis dalam beberapa baris, termasuk kata kerja NEWLINEs, TABs, dan karakter khusus lainnya. 
Sintaks untuk triple quotes terdiri dari tiga tanda kutip tunggal atau ganda ditulis berturut-turut :
Berikut adalah contohnya : 

```python
kutipantiga = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (kutipantiga)
```

#### String Unicode Python

Pada Python 3, semua string diwakili dalam Unicode. Sedangkan pada Python 2 disimpan secara internal sebagai 8-bit ASCII, maka diperlukanlampiran 'u' untuk membuatnya menjadi Unicode. Tetapi hal ini tidak lagi diperlukan sekarang. :

Metode String Built-in

Python menyertakan metode built-in berikut untuk memanipulasi string 

| Metode | 	Penjelasan | 
| --- | --- |
| `capitalize()` | 	Meng-kapitalkan huruf pertama string | 
| `center(width, fillchar)` | 	Mengembalikan string yang dilapisi dengan fillchar dengan string asli yang dipusatkan pada total width kolom. | 
| `count(str, beg = 0,end = len(string))`	 | Menghitung berapa kali str yang terjadi dalam string atau dalam substring string jika memulai indeks beg dan end index end diberikan. | 
| `decode(encoding = 'UTF-8',errors = 'strict')`	 | Dekode string menggunakan codec yang terdaftar untuk pengkodean. Encoding default ke pengkodean string default. | 
| `encode(encoding = 'UTF-8',errors = 'strict')`	 | Mengembalikan versi string yang dikodekan string; Pada kesalahan, default adalah menaikkan ValueError kecuali jika kesalahan diberikan dengan 'ignore' atau 'replace'. | 
| `endswith(suffix, beg = 0, end = len(string))`	 | Menentukan apakah string atau substring string (jika memulai indeks memohon dan mengakhiri akhir indeks diberikan) berakhir dengan akhiran; Mengembalikan nilai true jika benar dan salah. | 
| `expandtabs(tabsize = 8)`	 | Memperluas tab dalam string ke banyak ruang; Default ke 8 spasi per tab jika tabsize tidak tersedia. | 
| `find(str, beg = 0 end = len(string))`	 | Tentukan jika str terjadi dalam string atau dalam substring string jika memulai indeks beg dan end index end diberikan return index jika ditemukan dan -1 sebaliknya. | 
| `index(str, beg = 0, end = len(string))`	 | Sama seperti find (), namun menimbulkan pengecualian jika str tidak ditemukan. | 
| `isalnum()`	 | Mengembalikan true jika string memiliki minimal 1 karakter dan semua karakternya alfanumerik dan false sebaliknya. | 
| `isalpha()`	 | Mengembalikan true jika string memiliki minimal 1 karakter dan semua karakter adalah abjad dan false sebaliknya. | 
| `isdigit()`	 | Mengembalikan true jika string hanya berisi digit dan false sebaliknya. | 
| `islower()`	 | Mengembalikan true jika string memiliki setidaknya 1 karakter casing dan semua karakter casing dalam huruf kecil dan false sebaliknya. | 
| `isnumeric()`	 | Mengembalikan true jika string unicode hanya berisi karakter numerik dan false sebaliknya. | 
| `isspace()`	 | Mengembalikan true jika string hanya berisi karakter spasi dan false sebaliknya. | 
| `istitle()` | 	Mengembalikan true jika string benar "titlecased" dan false sebaliknya. | 
| `isupper()`	 | Mengembalikan true jika string memiliki setidaknya satu karakter casing dan semua karakter casing ada dalam huruf besar dan false sebaliknya. | 
| `join(seq)` | 	Merges (concatenates) representasi string elemen dalam urutan seq menjadi string, dengan string pemisah. | 
| `len(string)`	 | Mengembalikan panjang string | 
| `ljust(width[, fillchar])`	 | Mengembalikan string berlapis ruang dengan string asli dibiarkan dibenarkan ke kolom lebar total. | 
| `lower()` | 	Mengonversi semua huruf besar dalam bentuk string menjadi huruf kecil. | 
| `lstrip()` | 	Menghapus semua spasi utama dalam string. | 
| `maketrans()` | 	Mengembalikan tabel terjemahan untuk digunakan dalam fungsi terjemahan. | 
| `max(str)` | 	Mengembalikan karakter alfabetik dari string str. | 
| `min(str)`	 | Mengembalikan min karakter abjad dari string str. | 
| `replace(old, new [, max])`	 | Menggantikan semua kemunculan lama dalam string dengan kejadian baru atau paling maksimal jika max diberikan. | 
| `rfind(str, beg = 0,end = len(string))`	 | Sama seperti find (), tapi cari mundur dalam string. | 
| `rindex( str, beg = 0, end = len(string))`	 | Sama seperti index (), tapi cari mundur dalam string. | 
| `rjust(width,[, fillchar])`	 | Mengembalikan string berlapis ruang dengan senar asli benar-dibenarkan untuk total kolom lebar. | 
| `rstrip()` | 	Menghapus semua spasi spasi string. | 
| `split(str="", num=string.count(str))`	 | Membagi string sesuai dengan pemisah str (ruang jika tidak disediakan) dan mengembalikan daftar substring; Terpecah menjadi paling banyak substring jika diberikan. | 
| `splitlines( num=string.count('\n')) `| 	Membagi string sama sekali (atau num) NEWLINEs dan mengembalikan daftar setiap baris dengan NEWLINEs dihapus. | 
| `startswith(str, beg=0,end=len(string)`		 | Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise. | 
| `strip([chars])`		 | Lakukan kedua lstrip () dan rstrip () pada string | 
| `swapcase()`	 | 	Kasus invers untuk semua huruf dalam string. | 
| `title()`		 | Mengembalikan versi string "titlecased", yaitu, semua kata diawali dengan huruf besar dan sisanya huruf kecil. | 
| `translate(table, deletechars="")	`	 | Menerjemahkan string sesuai dengan tabel terjemahan str (256 karakter), menghapus string del. | 
| `upper()`	 | 	Mengonversi huruf kecil dalam bentuk string ke huruf besar. | 
| `zfill (width)`	 | 	Mengembalikan string asli yang tertinggal dengan angka nol ke total karakter lebar; Dimaksudkan untuk angka, zfill () mempertahankan tanda apapun yang diberikan (kurang satu nol). | 
| `isdecimal()`	 | 	Mengembalikan nilai true jika string unicode hanya berisi karakter desimal dan false sebaliknya. | 

## Menggunakan Tuple
Sebuah tupel adalah urutan objek Python yang tidak berubah. Tupel adalah urutan, seperti daftar. Perbedaan utama antara tupel dan daftarnya adalah bahwa tupel tidak dapat diubah tidak seperti List Python. Tupel menggunakan tanda kurung, sedangkan List Python menggunakan tanda kurung siku.

Membuat tuple semudah memasukkan nilai-nilai yang dipisahkan koma. Secara opsional, Anda dapat memasukkan nilai-nilai yang dipisahkan koma ini di antara tanda kurung juga. Sebagai contoh : 

```python
#Contoh sederhana pembuatan tuple pada bahasa pemrograman python

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
```

Tupel kosong ditulis sebagai dua tanda kurung yang tidak berisi apa-apa, contohnya : tup1 = ();
Untuk menulis tupel yang berisi satu nilai, Anda harus memasukkan koma, meskipun hanya ada satu nilai, contohnya : tup1 = (50,)
Seperti indeks String, indeks tuple mulai dari 0, dan mereka dapat diiris, digabungkan, dan seterusnya

#### Akses Nilai Dalam Tuple Python

Untuk mengakses nilai dalam tupel, gunakan tanda kurung siku untuk mengiris beserta indeks atau indeks untuk mendapatkan nilai yang tersedia pada indeks tersebut. Sebagai contoh :

```python
#Cara mengakses nilai tuple

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
```

Setelah Anda mengeksekusi kode diatas, hasilnya akan seperti dibawah ini :

`tup1[0]: fisika`
`tup2[1:5]: (2, 3, 4, 5)`

#### Update Nilai Dalam Tuple Python

Tuple tidak berubah, yang berarti Anda tidak dapat memperbarui atau mengubah nilai elemen tupel. Anda dapat mengambil bagian dari tupel yang ada untuk membuat tupel baru seperti ditunjukkan oleh contoh berikut.


```python
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Aksi seperti dibawah ini tidak bisa dilakukan pada tuple python
# Karena memang nilai pada tuple python tidak bisa diubah
# tup1[0] = 100;

# Jadi, buatlah tuple baru sebagai berikut
tup3 = tup1 + tup2
print (tup3)
```

#### Hapus Nilai Dalam Tuple Python

Menghapus elemen tuple individual tidak mungkin dilakukan. Tentu saja, tidak ada yang salah dengan menggabungkan tupel lain dengan unsur-unsur yang tidak diinginkan dibuang.

Untuk secara eksplisit menghapus keseluruhan tuple, cukup gunakan del statement. Sebagai contoh


```python
tup = ('fisika', 'kimia', 1993, 2017);

print (tup)
del tup;
print "Setelah menghapus tuple : "
print tup
```


#### Operasi Dasar Pada Tuple Python

Tupel merespons operator + dan * sama seperti String; Mereka berarti penggabungan dan pengulangan di sini juga berlaku, kecuali hasilnya adalah tupel baru, bukan string.

Sebenarnya, Tuple merespons semua operasi urutan umum yang kami gunakan pada String di bab sebelumnya. Dibawah ini adalah tabel daftar operasi dasar pada Tuple python


| Python Expression	 | Hasil | 	Penjelasan | 
| --- | --- | --- | 
| len((1, 2, 3)) | 	3 | 	Length | 
| (1, 2, 3) + (4, 5, 6) | 	(1, 2, 3, 4, 5, 6) | 	Concatenation | 
| ('Halo!',) * 4 | 	('Halo!', 'Halo!', 'Halo!', 'Halo!') | 	Repetition | 
| 3 in (1, 2, 3) | 	True | 	Membership | 
| for x in (1,2,3) : print (x, end = ' ') | 	1 2 3 | 	Iteration | 

#### Indexing, Slicing dan Matrix Pada Tuple Python

Karena tupel adalah urutan, pengindeksan dan pengiris bekerja dengan cara yang sama untuk tupel seperti pada String, dengan asumsi masukan berikut

Dengan asumsi input berikut : `T = ('C++', 'Java', 'Python')`

 | Python Expression | 	Hasil | 	Penjelasan |
 | --- | --- | --- |
 | `T[2]` | 	`'Python'` | 	Offset mulai dari nol | 
 | `T[-2]` | 	`'Java'`	 | Negatif: hitung dari kanan | 
 | `T[1:]` | 	`('Java', 'Python')` | 	Slicing mengambil bagian | 

#### Fungsi Build-in Pada Tuple Python

Python menyertakan fungsi built-in sebagai berikut

| Python Function |	Penjelasan |	
| --- | --- |
| `cmp(tuple1, tuple2)` |		# Tidak lagi tersedia dengan Python 3 |	
| `len(tuple)` |		Memberikan total panjang tuple. |	
| `max(tuple)` |		Mengembalikan item dari tuple dengan nilai maks. |	
| `min(tuple)` |		Mengembalikan item dari tuple dengan nilai min. |	
| `tuple(seq)` |		Mengubah tuple menjadi tuple. |	
