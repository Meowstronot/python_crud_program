from utils.data_manager import *
import datetime as dt

def show_filtered_database(nomor:str):
    """Menampilkan data dari satu nomor, nomor harus ada
    Args:
        nomor (str): nomor hp
    """
    filtered_database = [item for item in database if nomor in item["nomor_hp"]]
    print("No Hp ditemukan : ")
    print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
    print("")

def update_data():
    """Function untuk merubah data pada database
    """
    print("")
    print("Silahkan lengkapi informasi untuk mengubah data!")
    print("")

    stop_loop = False # untuk control keluar nested loop
    while True:
            
            # validasi input nomor hp
            while True:
                nomor_hp = input("Masukan nomor HP data yang ingin diupdate: ")
                if nomor_hp.isdigit() and (len(nomor_hp) == 12 or len(nomor_hp)== 13) :
                    #print("aman")
                    break
                else:
                    print("Nomor HP tidak valid!")

            # 2nd loop untuk cari nomor hp
            for i in range(0,len(database)):
                
                if database[i]["nomor_hp"] == nomor_hp:
                    
                    #----------------------------------------- EDIT DATA
                    show_filtered_database(nomor_hp)
                    #print("1. Nomor HP")
                    print("1. Email")
                    print("2. Nama")
                    print("3. Jenis Kelamin")
                    print("4. Provinsi")
                    print("5. Kota")
                    print("6. Alamat")
                    print("7. Kategoti")
                    print("8. Catatan")
                    print("9. Cancel")
                    # validasi input
                    while True:
                        option = input("Silahkan pilih kolom yang ingin di update: ")
                        try:
                            option = int(option)
                            if option in range(1,11):
                                break
                            else:
                                print("Silahkan masukan angka 1-10")
                                continue
                        except:
                            print("Silahkan masukan angka 1-10")
                    
                    # if option == 1:
                    #     while True:
                    #         nomor_hp = input("Silahkan masukan nomor HP: ")
                    #         if nomor_hp.isdigit() and (len(nomor_hp) == 12 or len(nomor_hp)== 13) :
                    #             #print("aman")
                    #             break
                    #         else:
                    #             print("Nomor HP tidak valid!")
                    #     database[i]["nomor_hp"] = nomor_hp

                    if option == 1:
                        while True:
                            email = input("Silahkan masukan email: ")
                            if email == "":
                                print("Email masih kosong")
                            else:
                                break
                        database[i]["email"] = email
                    
                    elif option == 2:
                        while True:
                            nama = input("Silahkan masukan nama: ")
                            if nama == "" or nama[0].isdigit() :
                                print("Input tidak valid")
                            else:
                                break
                        database[i]["nama"] = nama

                    elif option == 3:
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
                        database[i]["jenis_kelamin"] = jenis_kelamin

                    elif option == 4:
                        while True:
                            provinsi = input("Silahkan masukan provinsi: ")
                            if provinsi == "":
                                print("Provinsi masih kosong")
                            else:
                                break
                        database[i]["provinsi"] = provinsi

                    elif option == 5:
                        while True:
                            kota = input("Silahkan masukan kota: ")
                            if kota == "":
                                print("kota masih kosong")
                            else:
                                break
                        database[i]["kota"] = kota

                    elif option == 6:

                        alamat = input("Silahkan masukan alamat: ")
                        database[i]["alamat"] = alamat

                    elif option == 7:
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

                        database[i]["kategori"] = kategori

                    elif option == 8:

                        catatan = input("Silahkan masukan catatan: ")
                        database[i]["catatan"] = catatan
                    
                    elif option == 9:
                        print("Update Data Canceled!")
                        return

                    # ADD last update time and show data after edit
                    last_update = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    database[i]["last_update"] = last_update

                    show_filtered_database(nomor_hp)
                    print("Data Sukses diupdate")
                    stop_loop = True
                    break #exit loop cari nomor hp
            else:
                print("Nomor HP tidak ditemukan!")
                # loop untuk cari lagi
                while True:
                    cari_lagi = input("Ingin mencari lagi? (y/n) :")
                    if cari_lagi.lower() == "y":
                        break
                    elif cari_lagi.lower() == "n":
                        stop_loop=True
                        break
        
            if stop_loop:
                break



