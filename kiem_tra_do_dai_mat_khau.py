password = int(input("Hãy nhập mật khẩu của bạn:"))

if len(password) < 8:
    print("Mật khẩu đạt yêu cầu")
else:
    print("Mật khẩu quá ngắn")