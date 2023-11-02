def jumlah_bulan(pilih, tahun):
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    if pilih >= 1 and pilih <= 12:
        if pilih == 1 or pilih == 3 or pilih == 5 or pilih == 7 or pilih == 8 or pilih == 10 or pilih == 12:
            return f"Ini bulan {bulan[pilih-1]} dan sebulan sebanyak 31 Hari"
        elif pilih == 2:
            if tahun is not None and ((tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0):
                return f"Ini bulan {bulan[pilih-1]} dan sebulan sebanyak 29 Hari"
            else:
                return f"Ini bulan {bulan[pilih-1]} dan sebulan sebanyak 28 Hari"
        elif pilih == 4 or pilih == 6 or pilih == 9 or pilih == 11:
            return f"Ini bulan {bulan[pilih-1]} dan sebulan sebanyak 30 hari"
    else:
        return "Input harus 1 - 12!"

def main():
    ulang = "y"
    while ulang.lower() == "y":
        pilih = int(input("Masukkan bulan (1 - 12): "))
        if pilih >= 1 and pilih <= 12:
            if pilih == 2:
                tahun = int(input("Masukkan tahunnya: "))
                hasil = jumlah_bulan(pilih, tahun)
            else:
                hasil = jumlah_bulan(pilih, None)
            print(hasil)
        else:
            print("Input salah!")

        ulang = input("Lagi? (y / n): ")
        if ulang.lower() != "y":
            break


main()
