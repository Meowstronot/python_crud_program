from utils.data_manager import *
from utils.update_data import *
import datetime as dt

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

                        del database[i]
                        print("Data Sukses Dihapus!")
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