from utils.data_manager import *

def add_data():
    """Function untuk add data baru ke database

       Jika data sudah ada maka bisa di update dengan yang baru
    """
    print("")
    print("Silahkan isi Data Kontak untuk dimasukan kedalam Database: ")
    print("")

    while True:
        nomor_hp = input("Silahkan masukan nomor HP: ")
        if nomor_hp.isdigit():
            #print("aman")
            break
        else:
            print("Nomor HP tidak valid!")

    email = input("Silahkan masukan email: ")

    while True:
        nama = input("Silahkan masukan nama: ")
        if nama == "":
            print("Nama masih kosong")
        else:
            break
            
    while True:
        jenis_kelamin = input("Silahkan pilih kelamin (Laki-laki/Perempuan): ")
        if jenis_kelamin.lower() == "laki-laki" or jenis_kelamin == "perempuan":
            #print("aman")
            break
        else:
            print("Masukan Laki-laki atau Perempuan!")
    
    while True:
        tgl = input("Silahkan masukan tanggal lahir (1-31): ")
        if tgl.isdigit() == True and int(tgl) in range(1,32):
            tgl = int(tgl)
            #print("aman")
            break
        else:
            print("Tanggal lahir tidak valid!")

    while True:
        bulan_lahir = input("Silahkan masukan bulan lahir(1-12): ")
        if bulan_lahir.isdigit() == True and int(bulan_lahir) in range(1,13):
            bulan_lahir = int(bulan_lahir)
            #print("aman")
            break
        else:
            print("Bulan lahir tidak valid!")

    while True:
        tahun_lahir = input("Silahkan masukan tahun lahir: ")
        if tahun_lahir.isdigit() == True and len(tahun_lahir) == 4:
            tahun_lahir = int(tahun_lahir)
            #print("aman")
            break
        else:
            print("Tahun lahir tidak valid!")

    while True:
        alamat = input("Silahkan masukan alamat: ")
        if alamat == "":
            print("Alamat masih kosong")
        else:
            break

    pekerjaan = input("Silahkan masukan pekerjaan: ")
    catatan = input("Silahkan masukan catatan: ")

    inputed_data = {"nomor_hp": nomor_hp,
                        "email": email,
                        "nama": nama,
                        "jenis_kelamin": jenis_kelamin,
                        "tgl_lahir":dt.date(tahun_lahir,bulan_lahir,tgl),
                        "usia": None,
                        "alamat":alamat,
                        "pekerjaan":pekerjaan,
                        "catatan":catatan} 

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
