# ulang = 10
# for i in range(ulang):
#     print("perulangan ke-"+str(i)+" kali")
#     print(f"perulangan ke--{i} kali")

# for i in range(1, 11, 2):
#     print(f"perulangan ke--{i} kali")

# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in range (simpan):
#     print(i)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")


# for i in range(1, 6, 2):
#     for j in range(1, 6, 2):
#         print(f"{i} x {j} = {i * j}")


# for i in range(10, -1, -1):
#     print(f"anak ayam turun {i}")

# ulang = "ya"
# hitung = 0
# while ulang == "ya":
#     print(f"perulangan ke{hitung}")
#     ulang = input("apakah anda masi ingin mengulang ? ")
#     hitung +=1
# print("perulangan selesai")

# x = 0
# while x < 5
#     print(x)
#     x+=1

# hitung = 1
# while True:
#     ulang = input("apakag anda masi ingin mengulang ? ")
#     if ulang == "tidak":
#         break 
#     hitung +=1
# print(f"total perulangan: {hitung}")

# for i in range(10):
#     if i  %2 == 0:
#         continue
#     if i == 9:
#         break
#     print(i)

usn = "admin"
pw = "123"
salah = 0

while salah < 3:
    ussername = input("masukkan ussername anda: ")
    password = input("masukkan password anda: ")
    if usn == ussername and pw == password:
        print("login berhasil")
        break
    else: 
        print("login gagal")
        salah+=1
