from tabulate import tabulate
from copy import deepcopy
import datetime as dt

database = [
                {"nomor_hp": "081382838527",
                 "email": "shinaruikhisan@gmail.com",
                 "nama": "MOH. KHISANUL FAKHRUDIN AKBAR",
                 "jenis_kelamin": "Laki-laki",
                 "provinsi":"Jawa Timur",
                 "kota": "Gresik",
                 "alamat":"RT 4 RW 3 GOLOKAN SIDAYU",
                 "kategori":"Teman Kuliah",
                 "catatan":"",
                 "last_update": None},

                 {"nomor_hp": "081234567890", 
                  "email": "aisyahrahmawati@gmail.com", 
                  "nama": "Aisyah Rahmawati", 
                  "jenis_kelamin": "Perempuan", 
                  "provinsi": "Jawa Barat", 
                  "kota": "Bandung", 
                  "alamat": "Jl. Sukajadi No. 12", 
                  "kategori": "Teman SMA", 
                  "catatan": "", 
                  "last_update": None},

                  {"nomor_hp": "082345678901", 
                   "email": "muhammadfauzi23@gmail.com", 
                   "nama": "Muhammad Fauzi", 
                   "jenis_kelamin": "Laki-laki",
                   "provinsi": "Jawa Tengah", 
                   "kota": "Semarang", 
                   "alamat": "Jl. Pemuda No. 45", 
                   "kategori": "Teman Kerja", 
                   "catatan": "", 
                   "last_update": None},

                   {"nomor_hp": "083456789012", 
                    "email": "siti-fatimah27@gmail.com", 
                    "nama": "Siti Fatimah", 
                    "jenis_kelamin": "Perempuan", 
                    "provinsi": "Jawa Timur", 
                    "kota": "Surabaya", 
                    "alamat": "Jl. Raya Darmo No. 123", 
                    "kategori": "Teman Kuliah", 
                    "catatan": "", 
                    "last_update": None}

              ]

def show_database():
   """function untuk menampilkan Database Yellow Pages
   """
   copy_database = deepcopy(database) # memerlukan deepcopy karena dictionary pada list dictionary masih nyangkut/ikut keubah jika hanya menggunakan copy()
   for data in copy_database:
       if data["last_update"] != None:
         data["last_update"] = data["last_update"].strftime("%H:%M %d-%m-%Y")

   print("")
   print(tabulate(copy_database, headers="keys", tablefmt="pipe"))
   print("")

def sort_nama():
   """mengurutkan data berdasarkan nama
   """
   option = None
   database_sorted = None

   while option != 3:
      
      print("1. Urutkan nama dari A-Z")
      print("2. Urutkan nama dari Z-A")
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
         print("Mengurutkan nama dari A-z:")
         
         database_sorted = sorted(database, key=lambda list_dict: list_dict["nama"])
         print("")
         print(tabulate(database_sorted, headers="keys", tablefmt="pipe"))
         print("Sukses mengurutkan nama dari A-z")
         print("")
         
      elif option == 2:
         print("Mengurutkan nama dari Z-A: ")

         database_sorted = sorted(database, key=lambda list_dict: list_dict["nama"], reverse=True)
         print("")
         print(tabulate(database_sorted, headers="keys", tablefmt="pipe"))
         print("Sukses mengurutkan nama dari Z-A!")
         print("")
         
      else:
          # jika user memasukan pilihan diluar rentang pilihan
          print("Masukan nilai 1-3")
   

def filter_database():
   """Filter Database berdasarkan menu pilihan
   """
   option = None
   filtered_database = None

   while option != 6:

      print("")
      print("1. Cari Kontak berdasarkan nomor HP")
      print("2. Cari Kontak berdasarkan nama")
      print("3. Cari Kontak berdasarkan kategori")
      print("4. Cari Kontak berdasarkan provinsi")
      print("5. Cari Kontak berdasarkan kota")
      print("6. Kembali ke menu utama")
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
         # filter berdasarkan string nomor hp
         show_database()

         input_no = input("Silahkan masukan nomor HP untuk filter: ")
         filtered_database = [item for item in database if input_no in item["nomor_hp"]]

         if filtered_database != []:
            print("Hasil Filter: ")
            print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
            print("Filter Sukses!")
         else:
            print("")
            print("Hasil Filter Kosong!")
            print("")

      elif option == 2:
         # filter berdasarkan string nama
         show_database()

         input_nama = input("Silahkan masukan nomor HP untuk filter: ")
         filtered_database = [item for item in database if input_nama.lower() in item["nama"].lower()]

         if filtered_database != []:
            print("Hasil Filter: ")
            print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
            print("Filter Sukses!")
         else:
            print("")
            print("Hasil Filter Kosong!")
            print("")

      elif option == 3:
         # filter berdasarkan kategori
         show_database()

         print("Kategori Kontak :")
         print("1. Keluarga")
         print("2. Teman Kerja")
         print("3. Teman Kuliah")
         print("4. Teman SMA")
         print("5. Teman SMP")
         print("6. Teman SD")
         print("7. Teman Main")
         print("")
         list_kategori = ["Keluarga","Teman Kerja","Teman Kuliah","Teman SMA","Teman SMP","Teman SD","Teman Main"]
         # mencegah user memasukan input selain integer
         while True:
            kategori = input("Silahkan pilih kategori untuk filter : ")
            try:
                  kategori = int(kategori)
                  if kategori in range(1,8):
                     break
                  else:
                      print("Silahkan masukan angka 1-7")
                      continue
            except:
                  print("Silahkan masukan angka 1-7")
            
         filtered_database = [item for item in database if list_kategori[kategori-1].lower() in item["kategori"].lower()]
         if filtered_database != []:
            print("Hasil Filter: ")
            print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
            print("Filter Sukses!")
         else:
            print("")
            print("Hasil Filter Kosong!")
            print("")

      elif option == 4:
         # filter berdasarkan string provinsi
         show_database()

         provinsi = input("Silahkan masukan provinsi untuk filter: ")
         filtered_database = [item for item in database if provinsi.lower() in item["provinsi"].lower()]

         if filtered_database != []:
            print("Hasil Filter: ")
            print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
            print("Filter Sukses!")
         else:
            print("")
            print("Hasil Filter Kosong!")
            print("")

      elif option == 5:
         # filter berdasarkan string kota
         show_database()

         kota = input("Silahkan masukan kota untuk filter: ")
         filtered_database = [item for item in database if kota.lower() in item["kota"].lower()]

         if filtered_database != []:
            print("Hasil Filter: ")
            print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
            print("Filter Sukses!")
         else:
            print("")
            print("Hasil Filter Kosong!")
            print("")

      elif option == 6:
          pass
      else:
          print("Input is not valid !")

