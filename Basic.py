import datetime
print ('Waktu sekarang',datetime.datetime.now())

"""Variabel"""
date = datetime.datetime.now()
print(date)

"""Mengabungkan integer & string"""
number = 10
string = 'Sabil'
print(number, string)

"""Simple Type"""
x = 15
y = '15'
z = 15.1

sum1 = x+x
sum2 = y+y
sum3 = z+z

print(x,y,z)
print(type(x),type(y),type(z))

"""List"""
print(list(range(1,10)))
print(list(range(1,10,2)))

"""Menjumlahkan nilai didalam list"""
student_grades = [4,12.1,6,9]
mysum = sum(student_grades)
print(mysum)
"""Panjang nilai didalam list"""
length = len(student_grades)
print(length)
mean = mysum/length
print(mean)
"""Mencari jumlah nilai dalam list"""
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0)) #mencari nilai didalamnya
student = {'sabil':8.0, 'yanuar':7.0,'peby':9.0}
print(student.values()) # menampilkan nilainya
print(student.keys()) # menampilkan stringnya

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Class']: ", dict['Class'])

import time; # Digunakan untuk meng-import modul time
ticks = time.time()
print ("Berjalan sejak 12:00am, January 1, 1970:", ticks)
localtime = time.localtime(time.time())
print ("Waktu lokal saat ini :", localtime)
