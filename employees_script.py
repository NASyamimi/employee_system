employees=[]

while True:
    print("\n---Sistem Pendaftaran Pekerja Dedikasi--")
    print("1. Pendaftaran.")
    print("2. Semak semula pendaftaran.")
    print("3. Keluar. ")

    choice=input("Sila pilih pilihan anda yang tertera di bawah ")

    if choice == "1":
        nama_id=input("Sila masukkan nama penuh anda dengan huruf besar: ")
        email=input("Sila masukkan Alamat E-mel anda: ")
        no_telephone=input("Sila masukkan nombor telefon anda bermula digit 60: ")

        employee={
            "nama_id":nama_id,
            "email":email,
            "no_telephone":no_telephone
        }

        employees.append(employee)

        print("Pendaftaran anda telah berjaya")

    elif choice == "2":
        print("\n Semak semula pendafatran anda di bawah: ")

        for employee in employees:
            print("nama_id  :", employee["nama_id"])
            print("email  :", employee["email"])
            print("no_telephone  :", employee["no_telephone"]) 
            print("-----------------------------")

    elif choice =="3":
            print("Pendaftaran anda telah disemak.")

    else:
            print("Keluar dari sistem pendaftaran. Sila hubungi pihak pentadbiran untuk sebarang pertanyaan lanjut.")