x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

if x > 0 and y > 0:
    print(f"Điểm M({x}, {y})thuộc góc phần tư thứ 1 ")
elif x < 0 and y > 0:
    print(f"Điểm M({x}, {y})thuộc góc phần tư thứ 2")
elif x < 0 and y < 0:
    print(f"Điểm M({x}, {y})thuộc góc phần tư thứ 3")
elif x > 0 and y < 0:
    print(f"Điểm M({x}, {y})thuộc góc phần tư thứ 4")