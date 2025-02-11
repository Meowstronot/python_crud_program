from utils.data_manager import *
import datetime as dt

def add_data():
    """Function untuk add data baru ke database

       Jika data sudah ada maka bisa di update dengan yang baru
    """
    print("")
    print("Silahkan isi Data Kontak untuk dimasukan kedalam Database: ")
    print("")

    while True:
        nomor_hp = input("Silahkan masukan nomor HP: ")
        if nomor_hp.isdigit() and (len(nomor_hp) == 12 or len(nomor_hp)== 13) :
            #print("aman")
            break
        else:
            print("Nomor HP tidak valid!")

    while True:
        email = input("Silahkan masukan email: ")
        if email == "":
            print("Email masih kosong")
        else:
            break
    
    while True:
        nama = input("Silahkan masukan nama: ")
        if nama == "" or nama[0].isdigit() :
            print("Input tidak valid")
        else:
            break
            
    while True:
        print("1. Laki-laki")
        print("2. Perempuan")
        jenis_kelamin = input("Silahkan pilih kelamin :")
        if jenis_kelamin.lower() == "1" or jenis_kelamin == "2":
            
            if jenis_kelamin == "1":
                jenis_kelamin = "Laki-laki"
            elif jenis_kelamin == "2":
                jenis_kelamin = "Perempuan"
            #print("aman")
            break
        else:
            print("Input tidak valid!")
    
    while True:
        provinsi = input("Silahkan masukan provinsi: ")
        if provinsi == "":
            print("Provinsi masih kosong")
        else:
            break

    while True:
        kota = input("Silahkan masukan kota: ")
        if kota == "":
            print("Kota masih kosong")
        else:
            break

    while True:
        alamat = input("Silahkan masukan alamat: ")
        if alamat == "":
            print("Alamat masih kosong")
        else:
            break
    
    while True:
         
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

         kategori = input("Silahkan pilih kategori : ")
         try:
            kategori = int(kategori)
            if kategori in range(1,8):
                kategori = list_kategori[kategori-1]
                break
            else:
                print("Silahkan masukan angka 1-7")
                continue
         except:
            print("Silahkan masukan angka 1-7")


    catatan = input("Tambahkan catatan pada kontak(optional): ")
    last_update = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    inputed_data = {"nomor_hp": nomor_hp,
                    "email": email,
                    "nama": nama,
                    "jenis_kelamin": jenis_kelamin,
                    "provinsi":provinsi,
                    "kota": kota,
                    "alamat":alamat,
                    "kategori":kategori,
                    "catatan":catatan,
                    "last_update": last_update} 

    # cek duplikat pada database
    index = 0
    for data in database:
        index += 1

        if data["nomor_hp"] == nomor_hp:

            print("")
            print("Data dari nomor HP yang anda masukan sudah ada!")
            show_duplikat_database = [item for item in database if nomor_hp in item["nomor_hp"]]
            print("Data lama :")
            print(tabulate(show_duplikat_database, headers="keys", tablefmt="pipe"))
            print("Data baru yang diinput :")
            print(tabulate([inputed_data], headers="keys", tablefmt="pipe"))

            timpa = None
            while True:
                timpa = input("Apakah anda ingin mengganti data lama dengan data baru? (y/n): ")

                if timpa == "y":
                    database[index-1] = inputed_data
                    print("Perubahan data berhasil disimpan!")
                    return
                elif timpa == "n":
                    print("Perubahan data tidak disimpan!")
                    return
                else:
                    print("Input invalid!")          
            
    # jika tidak ada data duplikat maka akan add data
    database.append(inputed_data)
    print(f"Add Data Kontak {nomor_hp} Berhasil! :")
    show_database()  
