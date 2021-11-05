#profil
umur = 0
emoney = 0
#waktu
import datetime
waktu = datetime.datetime.now()
jam = int(waktu.strftime("%H"))
tdk = "tidak"
rep = "ya"
rep1 = "ya"
while rep == ("ya"):
    nama = input ("Masukkan Username Anda = ")
    pin = int(input("Masukkan PIN Anda = "))
    nama1 = "umam"
    pin1 = 1234
    nama2 = "pras"
    pin2 = 2345
    nama3 = "tejo"
    pin3 = 3456
    #profil umam as anak
    #profil pras as muda
    #profil tejo as tua
        #anak umur 0 - 17
        #muda umur 17 - 25
        #tua umur 25 - 50
    #usia profil hanya bisa diubah ke usia yang telah ditetapkan untuk umur profil tersebut
    if nama == "umam" and pin == 1234:
        pin = pin1
        nama = nama1
        umur = 10
        emoney = 100000
    if nama == "pras" and pin == 2345:
        pin = pin2
        nama = nama2
        umur = 22
        emoney = 150000
    if nama == "tejo" and pin == 3456:
        pin = pin3
        nama = nama3
        umur = 41
        emoney = 300000
    #anakpagi
    if nama == nama1 and pin == pin1 and umur >= 0 and umur <= 17 and jam >= 00 and jam <= 10 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Pagi Dek <<<================")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
                    
    #anaksiang 
    if nama == nama1 and pin == pin1 and umur >= 0 and umur <= 17 and jam >= 10 and jam <= 15 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Siang Dek <<<===============")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #anaksore 
    if nama == nama1 and pin == pin1 and umur >= 0 and umur <= 17 and jam >= 15 and jam <= 18 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Sore Dek <<<================")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #anakmalam 
    if nama == nama1 and pin == pin1 and umur >= 0 and umur <= 17 and jam >= 18 and jam <= 24 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Malam Dek <<<===============")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
            
    #mudapagi
    if nama == nama2 and pin == pin2 and umur >= 17 and umur <= 25 and jam >= 00 and jam <= 10 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Pagi Kak <<<================")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500\n")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #mudasiang 
    if nama == nama2 and pin == pin2 and umur >= 17 and umur <= 25 and jam >= 10 and jam <= 15 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Siang Kak <<<===============")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #mudasore 
    if nama == nama2 and pin == pin2 and umur >= 17 and umur <= 25 and jam >= 15 and jam <= 18 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Sore Kak <<<================")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #mudamalam 
    if nama == nama2 and pin == pin2 and umur >= 17 and umur <= 25 and jam >= 18 and jam <= 24 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Malam Kak <<<===============")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #tuapagi
    if nama == nama3 and pin == pin3 and umur >= 25 and umur <= 50 and jam >= 00 and jam <= 10 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Pagi Pak <<<================")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500\n")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #tuasiang 
    if nama == nama3 and pin == pin3 and umur >= 25 and umur <= 50 and jam >= 10 and jam <= 15 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Siang Pak <<<===============")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #tuasore 
    if nama == nama3 and pin == pin3 and umur >= 25 and umur <= 50 and jam >= 15 and jam <= 18 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Sore Pak <<<================")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
    #tuamalam 
    if nama == nama3 and pin == pin3 and umur >= 25 and umur <= 50 and jam >= 18 and jam <= 24 :
        print("\n^^^^^ ✔ Username dan PIN Anda Benar ✔ ^^^^^\n")
        print("=====================================================")
        print("=============>>> Selamat Malam Pak <<<================")
        print("=======>>> Selamat Datang Di ωαяσєиggєρяєк <<<=======")
        print("=====================================================\n\n")
        rep1 = "ya"
        while rep1 == ("ya"):
            print("\n\n======>>> Silahkan Pilih мєиυ Yang Tersedia<<<=======")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<   мєиυ   >>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("1. Paket Geprek Kids + Es Nutrisari ----> Rp. 6.000")
            print("2. Paket Geprek Crispy Kids + Es Popice ----> Rp. 7.500")
            plhn = input("No Pilihan Pembelian = ")
            print("\n")
            #kode voucher = prs12
            hrga1 = 6000
            hrga2 = 7500
            #мєиυ 1
            if plhn == "1":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga1 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga1 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga1 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #мєиυ 2
            if plhn == "2":
                    print("Masukkan Kode Voucher, Jika Tidak ada isi 0")
                    rep2 = "ya"
                    while rep2 == ("ya"):
                        kode = input("Kode Voucher = ")
                        if kode == "prs12":
                            print("==============================================")
                            print("---------Anda Mendapatkan Diskon 15%----------\n")
                            hrgadskn = int(hrga2 * 0.15)
                            saldo = int(emoney - hrgadskn)
                            print("---------Proses Pembelian Anda Berhasil--------")
                            print("===============================================")

                            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                            print("Sisa Saldo = Rp.",saldo)
                            print("")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                            rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                            if rep1 == "ya":
                                break
                            if rep1 == "tidak":
                                print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                print(":::::::::::::::::::::::::::::::::::::::::::::")
                                break
                            elif rep1 != "ya" and rep1 != "tidak":
                                print("------------Pilihan Tidak Tersedia------------")
                                print("===============================================")
                                break
                        elif kode == "0":
                                print("===============================================")
                                hrgadskn = int(hrga2 * 1)
                                saldo = int(emoney - hrgadskn)
                                print("---------Proses Pembelian Anda Berhasil--------")
                                print("===============================================")
                                print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                print("Sisa Saldo = Rp.",saldo)
                                print("")
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                if rep1 == "ya":
                                        break
                                if rep1 == "tidak":
                                    print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                    print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                                    break
                                elif rep1 != "ya" and rep1 != "tidak":
                                    print("------------Pilihan Tidak Tersedia------------")
                                    print("==============================================")
                                    break
                        elif kode != "prs12" and kode != "0":
                                print("===============================================")
                                print("------------Kode Voucher Tidak Valid-----------")
                                rep2 = input("Apakah Anda Ingin Mencoba Lagi? \nya/tidak | ")
                                print("\n")
                                if rep2 == "tidak":
                                        hrgadskn = int(hrga2 * 1)
                                        saldo = int(emoney - hrgadskn)
                                        print("---------Proses Pembelian Anda Berhasil--------")
                                        print("===============================================")
                                        print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
                                        print("Sisa Saldo = Rp.",saldo)
                                        print("")
                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                        rep1 = input("Apakah Anda Ingin Melakukan Transaksi Lagi? \nya/tidak | ")
                                        if rep1 == "ya":
                                            break
                                        if rep1 == "tidak":
                                            print("\n\n:::::::::::::::::::::::::::::::::::::::::::::")
                                            print(":::::::::::::::ᴛᴇʀɪᴍᴀ ᴋᴀꜱɪʜ::::::::::::::::::")
                                            print(":::::::::::::::::::::::::::::::::::::::::::::")
                                            break
                                        elif rep1 != "ya" and rep1 != "tidak":
                                            print("------------Pilihan Tidak Tersedia------------")
                                            print("==============================================")
                                            break
            #menugakkenl
            elif plhn != "1" and plhn != "2" :
                print("=================>>> ERROR <<<==================")
                print("======>>> Pilihan мєиυ tidak dikenali <<<=======")
                print("=================>>> ERROR <<<==================")
            if rep1 == "tidak":
                break
            if rep1 != "ya" and rep1 != "tidak":
                break
            continue
        if rep1 == "tidak":
            break
        if rep1 != "ya" and rep1 != "tidak":
            break
    if rep1 == "tidak":
        break
    if rep1 != "ya" and rep1 != "tidak":
        break

    else :
        print("\n^^^^^  ❌ Username dan PIN Anda Salah ❌  ^^^^^\n")
        rep = input("Apakah Anda Ingin Mengulang login ? \nya/tidak | ")
        if rep == "tidak":
            break
