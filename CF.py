# angka = 23
# run = True
# while run:
#     masukkan = int(input('Masukkan angka tebakkan: '))
#     if masukkan == angka:
#         print('Tebakan kamu benar')
#         run = False
#     elif masukkan < angka:
#         print('Tebakanmu lebih besar sedikit lagi dari', masukkan)
#     else:
#         print('Tebakanmu lebih kecil sedikit lagi dari', masukkan)
# else:
#     print('Selamat')
# print('yeayy')

# hasil = 'keluar'
# run = True
# while True:
#     masukkan = input('Ketikkan sembarang: ')
#     if masukkan.lower() == hasil: #Sensitif besar kecil
#         break
#     print('Panjang Karakter', len(masukkan))
# print('yeayy')

# while True:
#     s = input('Masukkan angka: ')
#     if s.lower() == 'keluar':
#         break
#     elif len(s) < 3:
#         print('Karakter yang anda masukkan terlalu pendek')
#         continue
#     print("Karakter sudah cukup panjang")

my_wihlist = ['fff','ccc','ddd']
print('Jumlah wish saya: ',len(my_wihlist))
print('Yaitu: ', end='')
for i in my_wihlist:
    print(i.capitalize(), end=',')
print('\n')
my_wihlist.sort()
print('Diurutkan: ', end='')
for i in my_wihlist:
    print(i.capitalize(), end=',')
print('\n')
my_wihlist.append('aaa')
print('Ditambahin: ', end='')
for i in my_wihlist:
    print(i.capitalize(), end=',')
print('\n')
my_wihlist.remove('aaa')
print('Sisa yang belom dibeli: ', end='')
for i in my_wihlist:
    print(i.capitalize(), end=',')