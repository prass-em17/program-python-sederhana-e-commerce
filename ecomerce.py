#Nama : M. Eko Prasetyo
NIM : 014

#welcome
print("=====================================")
print("==>>> Selamat Datang Di OutCell <<<==")
print("=====================================")

#login
emoney = int(input("E-Money (angka) = Rp. "))
if emoney < int(25000):
    print ("***Maaf Jumlah E-Money Anda Tidak Mencukupi Batas Minimal, Silahkan Top Up E-Money Kembali***")
elif emoney >= int(25000):
    print("<><><><><><><><><><><><><><><><><><><><><><>")
    print("<><><><><>Silahkan Masukkan PIN<><><><><><>")
    print("<><><><><><><><><><><><><><><><><><><><><><>")

    while True:
        pin = input("PIN = ")
        if pin != "131720":
            print ("***PIN Anda Salah, Silahkan Masukkan PIN Dengan Benar***")
        else :
            print ("***PIN Anda Benar***")
            break
    print("")
    print("")
    print("")
gold = 15/100
silver = 10/100
premium = 5/100
hrga1 = 25000
hrga2 = 50000
if emoney >= 100000:
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("= = = = = = = = = Anda Adalah Member Gold = = = = = = = = =")
    print("= = = =  Anda Mendapatkan Potongan Harga Hingga 15% = = = =")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<MENU PEMBELIAN>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("1. Pulsa Rp. 25.000")
    print("2. Pulsa Rp. 50.000")
    while True:
        plhn = input("Pilihan Pembelian = ")
        if plhn == "1":
            print("...")
            print("......")
            print(".........")
            print("............")
            print("...............")
            print("...................")
            print(".......................")
            print("--------Proses Pembelian Anda Berhasil--------")
            print ("===============================================")
            hrgadskn = int(hrga1 * gold)
            saldo = int(emoney - hrgadskn)
            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
            print("Sisa Saldo = Rp.",saldo)
            print("")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
            if lagi == "ya":
                    print()
                    continue
            elif lagi == "tidak":
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    break
            else:
                print("Pilihan Tidak Tersedia")
                quit()
                
        if plhn == "2":
            print("...")
            print("......")
            print(".........")
            print("............")
            print("...............")
            print("...................")
            print(".......................")
            print("--------Proses Pembelian Anda Berhasil--------")
            print ("===============================================")
            hrgadskn = int(hrga2 * gold)
            saldo = int(emoney - hrgadskn)
            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
            print("Sisa Saldo = Rp.",saldo)
            print("")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
            if lagi == "ya":
                    print()
                    continue
            elif lagi == "tidak":
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    break
            else:
                print("Pilihan Tidak Tersedia")
                break
        else :
            print("Pilihan Tidak Tersedia")
            quit()
if emoney >= 75000:
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("= = = = = = = = = Anda Adalah Member Silver = = = = = = = = =")
    print("= = = =  Anda Mendapatkan Potongan Harga Hingga 10% = = = =")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<MENU PEMBELIAN>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("1. Pulsa Rp. 25.000")
    print("2. Pulsa Rp. 50.000")
    while True:
        plhn = input("Pilihan Pembelian = ")
        if plhn == "1":
            print("...")
            print("......")
            print(".........")
            print("............")
            print("...............")
            print("...................")
            print(".......................")
            print("--------Proses Pembelian Anda Berhasil--------")
            print ("===============================================")
            hrgadskn = int(hrga1 * silver)
            saldo = int(emoney - hrgadskn)
            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
            print("Sisa Saldo = Rp.",saldo)
            print("")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
            if lagi == "ya":
                    print()
                    continue
            elif lagi == "tidak":
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    break
            else:
                print("Pilihan Tidak Tersedia")
                quit()
                
        if plhn == "2":
            print("...")
            print("......")
            print(".........")
            print("............")
            print("...............")
            print("...................")
            print(".......................")
            print("--------Proses Pembelian Anda Berhasil--------")
            print ("===============================================")
            hrgadskn = int(hrga2 * silver)
            saldo = int(emoney - hrgadskn)
            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
            print("Sisa Saldo = Rp.",saldo)
            print("")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
            if lagi == "ya":
                    print()
                    continue
            elif lagi == "tidak":
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    break
            else:
                print("Pilihan Tidak Tersedia")
                
                quit()
        else :
            print("Pilihan Tidak Tersedia")
            quit()

if emoney >= 50000:
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("= = = = = = = = = Anda Adalah Member Premium = = = = = = = = =")
    print("= = = =  Anda Mendapatkan Potongan Harga Hingga 5% = = = =")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<MENU PEMBELIAN>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("1. Pulsa Rp. 25.000")
    print("2. Pulsa Rp. 50.000")
    while True:
        plhn = input("Pilihan Pembelian = ")
        if plhn == "1":
            print("...")
            print("......")
            print(".........")
            print("............")
            print("...............")
            print("...................")
            print(".......................")
            print("--------Proses Pembelian Anda Berhasil--------")
            print ("===============================================")
            hrgadskn = int(hrga1 * premium)
            saldo = int(emoney - hrgadskn)
            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
            print("Sisa Saldo = Rp.",saldo)
            print("")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
            if lagi == "ya":
                    print()
                    continue
            elif lagi == "tidak":
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    break
            else:
                print("Pilihan Tidak Tersedia")
                quit()
        if plhn == "2":
            print("...")
            print("......")
            print(".........")
            print("............")
            print("...............")
            print("...................")
            print(".......................")
            print("--------Proses Pembelian Anda Berhasil--------")
            print ("===============================================")
            hrgadskn = int(hrga2 * premium)
            saldo = int(emoney - hrgadskn)
            print("Total = ","Rp.",emoney,"-","Rp.",hrgadskn)
            print("Sisa Saldo = Rp.",saldo)
            print("")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
            if lagi == "ya":
                    print()
                    continue
            elif lagi == "tidak":
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    break
            else:
                print("Pilihan Tidak Tersedia")
                
                quit()
        else :
            print("Pilihan Tidak Tersedia")
            quit()

if emoney >= 25000:
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("= = = = = = = = = = = Anda Bukan Member = = = = = = = = = =")
    print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<MENU PEMBELIAN>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("1. Pulsa Rp. 25.000")
    print("2. Pulsa Rp. 50.000")
    while True:
        plhn = input("Pilihan Pembelian = ")
        if plhn == "1":
            print("...")
            print("......")
            print(".........")
            print("............")
            print("...............")
            print("...................")
            print(".......................")
            print("--------Proses Pembelian Anda Berhasil--------")
            print ("===============================================")
            saldo = int(emoney - hrga1)
            print("Total = ","Rp.",emoney,"-","Rp.",hrga1)
            print("Sisa Saldo = Rp.",saldo)
            print("")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
            if lagi == "ya":
                    print()
                    continue
            elif lagi == "tidak":
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                    print(":::::::::::::::::::::::::::::::::::::::::::::")
                    break
            else:
                print("Pilihan Tidak Tersedia")
                quit()
        if plhn == "2":
            saldo = int(emoney - hrga2)
            if saldo <=0 :
                print("...")
                print("......")
                print(".........")
                print("............")
                print("...............")
                print("...................")
                print(".......................")
                print("--------Proses Pembelian Anda Gagal--------")
                print ("===============================================")
                print("Total = ","Rp.",emoney,"-","Rp.",hrga2)
                print("Saldo Anda Tidak Cukup")
                print("")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
                if lagi == "ya":
                        print()
                        continue
                elif lagi == "tidak":
                        print(":::::::::::::::::::::::::::::::::::::::::::::")
                        print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                        print(":::::::::::::::::::::::::::::::::::::::::::::")
                        break
                else:
                    print("Pilihan Tidak Tersedia")
                    
                    quit()
            else :
                print("...")
                print("......")
                print(".........")
                print("............")
                print("...............")
                print("...................")
                print(".......................")
                print("--------Proses Pembelian Anda Berhasil--------")
                print ("===============================================")
                saldo = int(emoney - hrga2)
                print("Total = ","Rp.",emoney,"-","Rp.",hrga2)
                print("Sisa Saldo = Rp.",saldo)
                print("")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                lagi = input("Apakah Anda Ingin Melakukan Transaksi Lagi? ya/tidak | ")
                if lagi == "ya":
                        print()
                        continue
                elif lagi == "tidak":
                        print(":::::::::::::::::::::::::::::::::::::::::::::")
                        print(":::::::::::::::TERIMA KASIH::::::::::::::::::")
                        print(":::::::::::::::::::::::::::::::::::::::::::::")
                        quit()
                else:
                    print("Pilihan Tidak Tersedia")
                    
                    quit()
        else :
            print("Pilihan Tidak Tersedia")

