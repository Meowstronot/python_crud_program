# ===================================
# [Contact Manager Program]
# ===================================
# Developed by. MOH. KHISANUL FAKHRUDIN AKBAR
# JCDS - [JCDS0512]


# /************************************/

# /===== Bahan yang dibutuhkan =====/
from tabulate import tabulate
import datetime as dt
from utils.data_manager import *  # import seluruh code from data_manager.py
from utils.add_data import *

# /===== Data Model =====/
# Data model yang digunakan adalah list of dictionary yang tersimpan pada file data_manager.py

# # /===== Feature Program =====/
# # Create your feature program here
# def read():
#     """Function for read the data
#     """
#     return

# def create():
#     """Function for create the data
#     """
#     return

# def update():
#     """Function for update the data
#     """
#     return

# def delete():
#     """Function for delete the data
#     """
#     return

# /===== Main Program =====/
def main():
    """Function for main program
    """
    input_user = None

    while input_user != "6":

        
        print("""█▀▀ █▀█ █▄░█ ▀█▀ ▄▀█ █▀▀ ▀█▀   █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀█   █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█
█▄▄ █▄█ █░▀█ ░█░ █▀█ █▄▄ ░█░   █░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █▀▄   █▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█""")
        print("")
        print("List Menu :")
        print("1. Tampilkan Data Kontak")
        print("2. Pencarian Data Kontak")
        print("3. Menambahkan Data Kontak")
        print("4. Update Data kontak")
        print("5. Hapus Data Kontak")
        print("6. Exit Program")
        print("")

        input_user = input("Silahkan pilih menu yang ingin dijalankan: ")

        if input_user == "1":
            show_database()
            sort_nama()
        elif input_user == "2":
            show_database()
            filter_database()
        elif input_user == "3":
            show_database()
            add_data()
        #elif input_user == "4":

        #elif input_user == "5":

        elif input_user == "6":
            print("")
            print("Good bye!")
            print("")
            
        else:
            print("Input is not valid !")


if __name__ == "__main__":
    main()