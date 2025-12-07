n = int(input("Bảng cửu chương cần in: "))
print(f"--- Bảng cửu chương {n} ---")

for i in range(1, 11):
    Ket_qua = n * i
    print(f"{n} x {i} = {Ket_qua}")