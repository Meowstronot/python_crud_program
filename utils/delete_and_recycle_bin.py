from utils.data_manager import *
from utils.update_data import *
import datetime as dt

recycle_bin_storage = []

def recycle_bin_menu():
    """Function untuk akses recycle bin
    """
    option = None
    while option != "2":

        print("Recycle Bin Storage :")
        print(tabulate(recycle_bin_storage, headers="keys", tablefmt="pipe"))
        print("")
        print("1. Restore Data")
        print("2. Kembali ke menu utama")
        option = input("Silahkan pilih menu : ")

        if option == "1":

            # 1. validasi input nomor hp
            while True:
                nomor_hp = input("Masukan nomor HP untuk mencari di recycle bin : ")
                if nomor_hp.isdigit() and (len(nomor_hp) == 12 or len(nomor_hp)== 13) :
                    break
                else:
                    print("Nomor HP tidak valid! (harus 12 atau 13 digit)")

            # 2. cari data nomor di recycle bin
            for i in range(0,len(recycle_bin_storage)):
                
                if recycle_bin_storage[i]["nomor_hp"] == nomor_hp:
                    filtered_database = [item for item in recycle_bin_storage if nomor_hp in item["nomor_hp"]]
                    print(tabulate(filtered_database, headers="keys", tablefmt="pipe"))
                    
                    # 3. option restore jika data ada di recycle bin
                    restore = None
                    while restore != "n":
                        restore = input(f"Ingin restore data {nomor_hp}? (y/n) :")

                        if restore == "y":
                            
                            last_update = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            recycle_bin_storage[i]["last_update"] = last_update
                            database.append(recycle_bin_storage[i])
                            del recycle_bin_storage[i]
                            print("Data berhasil di restore!")
                            return
                        
                        elif restore == "n":
                            pass
                        else:
                            print("Input tidak valid!")
                    break
            else:
                print("Nomor HP tidak ditemukan pada Recycle Bin")
            
        elif option == "2":
            return
        else:
            print("Input tidak valid!")




def delete_data():
    """Function untuk delete data
    """
    print("")

    stop_loop = False # untuk control keluar nested loop
    while True:
            
        # validasi input nomor hp
        while True:
            nomor_hp = input("Masukan nomor HP untuk mencari data yang akan dihapus : ")
            if nomor_hp.isdigit() and (len(nomor_hp) == 12 or len(nomor_hp)== 13) :
                #print("aman")
                break
            else:
                print("Nomor HP tidak valid! (harus 12 atau 13 digit)")
        
        # 2nd loop untuk cari nomor hp
        for i in range(0,len(database)):

            if database[i]["nomor_hp"] == nomor_hp:
                show_filtered_database(nomor_hp)

                while True:
                    del_option = input(f"Ingin menghapus data {nomor_hp}? (y/n) :")
                    if del_option.lower() == "y":

                        # menyimpan data yang terhapus ke recycle bin
                        last_update = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        database[i]["last_update"]=last_update
                        recycle_bin_storage.append(database[i])

                        del database[i]
                        print("Data sukses dihapus dan masuk recycle bin!")
                        return

                    elif del_option.lower() == "n":
                        print(f"Cancel Hapus data {nomor_hp}")
                        break

                stop_loop = True
                break
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