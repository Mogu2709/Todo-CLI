from datetime import datetime

# =========================
# LOAD & SAVE
# =========================

def load_tugas():
    tugas = []
    try:
        with open("tugas.txt", "r") as file:
            for line in file:
                status, tanggal, teks = line.strip().split("|")
                tugas.append([int(status), tanggal, teks])
    except FileNotFoundError:
        pass
    return tugas

def save_tugas(tugas):
    with open("tugas.txt", "w") as file:
        for status, tanggal, teks in tugas:
            file.write(f"{status}|{tanggal}|{teks}\n")

# =========================
# FITUR
# =========================

def tambah_tugas(tugas):
    item = input("Masukkan tugas baru: ")
    tanggal = datetime.now().strftime("%Y-%m-%d")
    tugas.append([0, tanggal, item])
    save_tugas(tugas)
    print("Tugas ditambahkan!")

def lihat_tugas(tugas):
    print("\nDaftar Tugas:")
    if not tugas:
        print("Belum ada tugas.")
    else:
        for i, (status, tanggal, teks) in enumerate(tugas):
            tanda = "✅" if status == 1 else "❌"
            print(f"{i+1}. {tanda} [{tanggal}] {teks}")

def tandai_selesai(tugas):
    lihat_tugas(tugas)
    try:
        nomor = int(input("Nomor tugas yang selesai: "))
        if 1 <= nomor <= len(tugas):
            tugas[nomor-1][0] = 1
            save_tugas(tugas)
            print("Tugas ditandai selesai!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")

def hapus_tugas(tugas):
    lihat_tugas(tugas)
    try:
        nomor = int(input("Nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(tugas):
            tugas.pop(nomor-1)
            save_tugas(tugas)
            print("Tugas dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")

def edit_tugas(tugas):
    lihat_tugas(tugas)
    try:
        nomor = int(input("Nomor tugas yang ingin diedit: "))
        if 1 <= nomor <= len(tugas):
            teks_baru = input("Masukkan teks baru: ")
            tugas[nomor-1][2] = teks_baru
            save_tugas(tugas)
            print("Tugas berhasil diedit!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus angka.")

# =========================
# MAIN
# =========================

def main():
    tugas = load_tugas()

    while True:
        print("\n=== TO DO LIST ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Tandai selesai")
        print("4. Edit tugas")
        print("5. Hapus tugas")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_tugas(tugas)
        elif pilihan == "2":
            lihat_tugas(tugas)
        elif pilihan == "3":
            tandai_selesai(tugas)
        elif pilihan == "4":
            edit_tugas(tugas)
        elif pilihan == "5":
            hapus_tugas(tugas)
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
