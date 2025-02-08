from tabulate import tabulate
from copy import deepcopy
import datetime as dt

database = [
                {"nomor_hp": "081382838527",
                 "email": "shinaruikhisan@gmail.com",
                 "nama": "MOH. KHISANUL FAKHRUDIN AKBAR",
                 "jenis_kelamin": "Laki-laki",
                 "tgl_lahir":dt.date(2001,2,14),
                 "usia": None,
                 "alamat":"Gresik",
                 "pekerjaan":"info loker",
                 "catatan":""},

               {
                  "nomor_hp": "081382838528",
                  "email": "example1@gmail.com",
                  "nama": "Person One",
                  "jenis_kelamin": "Laki-laki",
                  "tgl_lahir": dt.date(2001, 12, 1),
                  "usia": None,
                  "alamat": "Surabaya",
                  "pekerjaan": "admin",
                  "catatan": "Catatan 1",
               },
               {
                  "nomor_hp": "081382838529",
                  "email": "example2@gmail.com",
                  "nama": "Person Two",
                  "jenis_kelamin": "Perempuan",
                  "tgl_lahir": dt.date(2003, 5, 23),
                  "usia": None,
                  "alamat": "Malang",
                  "pekerjaan": "IT support",
                  "catatan": "Catatan 2",
               },
               {
                  "nomor_hp": "081382838530",
                  "email": "example3@gmail.com",
                  "nama": "Person Three",
                  "jenis_kelamin": "Laki-laki",
                  "tgl_lahir": dt.date(1999, 8, 15),
                  "usia": None,
                  "alamat": "Jakarta",
                  "pekerjaan": "freelancer",
                  "catatan": "Catatan 3",
               },
               {
                  "nomor_hp": "081382838531",
                  "email": "example4@gmail.com",
                  "nama": "Person Four",
                  "jenis_kelamin": "Perempuan",
                  "tgl_lahir": dt.date(1998, 5, 30),
                  "usia": None,
                  "alamat": "Bandung",
                  "pekerjaan": "teacher",
                  "catatan": "Catatan 4"
               }
              ]

def show_database():
   """function untuk menampilkan Database Yellow Pages
   """
   for item in database:

      # auto mengisi kolom usia
      tgl_lahir = item["tgl_lahir"]
      tgl_sekarang = dt.date.today()
      usia = tgl_sekarang.year - tgl_lahir.year - ((tgl_sekarang.month, tgl_sekarang.day) < (tgl_lahir.month, tgl_lahir.day))
      item["usia"] = usia

   # merubah format tgl lahir
   copy_database = deepcopy(database) # memerlukan deepcopy karena dictionary pada list dictionary masih nyangkut/ikut keubah jika hanya menggunakan copy()
   for data in copy_database:
       data["tgl_lahir"] = data["tgl_lahir"].strftime("%d-%m-%Y")

   print("")
   print(tabulate(copy_database, headers="keys", tablefmt="pipe"))
   print("")

def sort_usia():
   """mengurutkan usia data berdasarkan data tanggal lahir database
   """
   option = None
   database_sorted = None

   while option != 3:
      
      print("1. Urutkan usia dari paling muda")
      print("2. Urutkan usia dari paling tua")
      print("3. Kembali ke menu utama")
      print("")

      # mencegah user memasukan input selain integer
      while True:
         option = input("Masukan pilihan menu: ")
         try:
               option = int(option)
               break
         except:
               print("Silahkan masukan angka!")
   
      if option == 3:
          
          ask_save = None
          while True:

            ask_save = (input("Apakah anda ingin menyimpan perubahan? (y/n) :")).lower()
            if ask_save == "y":
               
               global database # error kalo tidak make ini, untuk modify data diluar function harus make global
               if database_sorted != None:
                  database = database_sorted.copy() # menyimpan sorted data ke dalam database
                  print("Perubahan berhasil disimpan!")
               break

            elif ask_save == "n":
               print("Perubahan tidak disimpan!")
               break

      elif option == 1:
         print("Mengurutkan usia dari paling muda ke paling tua: ")

         # mengurutkan tanpa mengubah data asli ### opsi 1
         database_sorted = sorted(database, key=lambda list_dict: list_dict["tgl_lahir"], reverse=True)
         print("")
         print(tabulate(database_sorted, headers="keys", tablefmt="pipe"))
         print("Sukses mengurutkan usia dari paling muda ke paling tua!")
         print("")

         # # mengurutkan langsung di data asli ### opsi 2
         # database.sort(key=lambda list_dict: list_dict["tgl_lahir"],reverse=True)
         # print("")
         # show_database()
         # print("Sukses mengurutkan usia dari paling muda ke paling tua!")
         # print("")
         
      elif option == 2:
         print("mengurutkan usia dari paling tua ke paling muda")
         
         # mengurutkan tanpa mengubah data asli ### opsi 1
         database_sorted = sorted(database, key=lambda list_dict: list_dict["tgl_lahir"])
         print("")
         print(tabulate(database_sorted, headers="keys", tablefmt="pipe"))
         print("Sukses mengurutkan usia dari paling tua ke paling muda!")
         print("")

         # # mengurutkan langsung di data asli ### opsi 2
         # database.sort(key=lambda list_dict: list_dict["tgl_lahir"])
         # print("")
         # show_database()
         # print("Sukses mengurutkan usia dari paling tua ke paling muda!")
         # print("")

      else:
          # jika user memasukan pilihan diluar rentang pilihan
          print("Masukan nilai 1-3")
   

def filter_tgl_lahir():
   """Filter Database berdasarkan tahin atau bulan kelahiran
      \nHasil Filter tidak akan disimpan
   """
   option = None
   filtered_database = None

   while option != 3:

      print("")
      print("1. Filter berdasarkan tahun lahir")
      print("2. Filter berdasarkan bulan lahir")
      print("3. Kembali ke menu utama")
      print("")

      # mencegah user memasukan input selain integer
      while True:
         option = input("Masukan pilihan menu: ")
         try:
               option = int(option)
               break
         except:
               print("Silahkan masukan angka!")
      
      if option == 1:
         show_database()

         # mencegah user memasukan input selain integer
         while True:
            tahun = input("Masukan tahun lahir untuk filter: ")
            try:
                  tahun = int(tahun)
                  break
            except:
                  print("Silahkan masukan angka!")

         filtered_database = [item for item in database if item["tgl_lahir"].year == tahun]

         if filtered_database != []:
            print("Hasil Filter: ")
            print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
            print("Filter Sukses!")
            
         else:
            print("")
            print("Hasil Filter Kosong!")
            print("")

      elif option == 2:
         show_database()

         # mencegah user memasukan input selain integer
         while True:
            bulan = input("Masukan bulan lahir (1-12) untuk filter: ")
            try:
                  bulan = int(bulan)
                  if bulan in range(1,13):
                     break
                  else:
                      print("Silahkan masukan angka 1-12")
                      continue
            except:
                  print("Silahkan masukan angka!")

         filtered_database = [item for item in database if item["tgl_lahir"].month == bulan]

         if filtered_database != []:
            print("Hasil Filter: ")
            print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
            print("Filter Sukses!")
            
         else:
            print("")
            print("Hasil Filter Kosong!")
            print("")


show_database()
sort_usia()
# filter_tgl_lahir()

# show_database()
# sort_usia()
# show_database()