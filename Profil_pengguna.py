from fungsi import simpan_data, validasi_tanggal_lahir, data_pengguna
from fungsi import muat_data

def tampilkan_profil(profil):
    print("="*70)
    print("Profil Pengguna".center(70))
    print("="*70)
    print(f"Nama: {profil['nama']}")
    print(f"NIM: {profil['NIM']}")
    print(f"Kelas: {profil['kelas']}")
    print(f"Tanggal Lahir: {profil['tanggal_lahir']}")
    print(f"No Telepon: {profil['no_telepon']}")
    print(f"Email: {profil['email']}")

def edit_profil(profil, username):
    print("\n=== Edit Profil Pengguna ===")
    while True:
        print("\nPilih bagian profil yang ingin Anda edit:")
        print("1. Nama")
        print("2. NIM")
        print("3. Kelas")
        print("4. Tanggal Lahir")
        print("5. No Telepon")
        print("6. Email")
        print("7. Selesai")
        pilihan = input("Masukkan pilihan (1-7): ").strip()

        if pilihan == "1":
            while True:
                nama = input("Masukkan nama baru: ").strip()
                if not nama:
                    print("Nama tidak boleh kosong.")
                    continue
                elif len(nama) > 20:
                    print("Nama maksimal terdiri dari 20 karakter.")
                    continue
                elif not all(c.isalpha() or c.isspace() for c in nama):
                    print("Nama harus berupa huruf.")
                    continue
                break
            profil["nama"] = nama

        elif pilihan == "2":
            while True:
                NIM = input("Masukkan NIM baru (7 digit): ").strip()
                if not NIM.isdigit() or len(NIM) != 7:
                    print("NIM harus berupa angka 7 digit.")
                    continue
                break
            profil["NIM"] = NIM

        elif pilihan == "3":
            while True:
                kelas = input("Masukkan kelas baru (contoh: RPL 1B): ").strip()
                try:
                    bagian = kelas.split()
                    if len(bagian) != 2:
                        raise ValueError
                    program, subkelas = bagian
                    if program.upper() not in ["RPL", "TEKKOM", "PGPAUD", "PGSD", "PMM"]:
                        raise ValueError
                    if program.upper() == "RPL" or program.upper() == "TEKKOM":
                        if subkelas[:-1].isdigit() and int(subkelas[:-1]) in range(1, 8) and subkelas[-1].upper() in ["A", "B", "C"]:
                            break
                        else:
                            raise ValueError
                    else:
                        if subkelas[:-1].isdigit() and int(subkelas[:-1]) in range(1, 8) and subkelas[-1].upper() in ["A", "B", "C", "D", "E", "F"]:
                            break
                        else:
                            raise ValueError
                except ValueError:
                    print("Kelas tidak valid. Pastikan format dan program sesuai dengan aturan.")
                    continue
            profil["kelas"] = kelas

        elif pilihan == "4":
            while True:
                tanggal_lahir = input("Masukkan tanggal lahir baru (DD-MM-YYYY): ").strip()
                if not validasi_tanggal_lahir(tanggal_lahir):
                    print("Format tanggal lahir tidak valid. Gunakan format DD-MM-YYYY.")
                    continue
                break
            profil["tanggal_lahir"] = tanggal_lahir

        elif pilihan == "5":
            while True:
                no_telepon = input("Masukkan no telepon baru (10-13 digit): ").strip()
                if not no_telepon.isdigit() or not (10 <= len(no_telepon) <= 13):
                    print("Nomor telepon harus berupa angka dengan panjang 10-13 digit.")
                    continue
                break
            profil["no_telepon"] = no_telepon

        elif pilihan == "6":
            while True:
                email = input("Masukkan email baru (ex: nama@gmail.com/@upi.edu): ").strip()
                if not email:
                    print("Email tidak boleh kosong.")
                    continue
                elif email.count("@gmail.com") != 1 and email.count("@upi.edu") != 1:
                    print("Format email tidak valid. Gunakan @gmail.com atau @upi.edu.")
                    continue
                break
            profil["email"] = email

        elif pilihan == "7":
            print("Perubahan profil berhasil disimpan!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        data_pengguna["users"][username]["profil"] = profil
        simpan_data(data_pengguna)
        print("Perubahan berhasil disimpan!")

    while True:
        lihat_profil = input("Apakah Anda ingin melihat profil yang diperbarui? (Y/N): ").strip().lower()
        if lihat_profil == "y":
            tampilkan_profil(profil)
            break
        elif lihat_profil == "n":
            print("Anda kembali ke menu sebelumnya.")
            break
        else:
            print("Pilihan tidak valid. Masukkan Y atau N.")
