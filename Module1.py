import random


# [Bài tập tổng hợp] Python Basic
# https://portal.rikkei.edu.vn/learn/236/homework/10418


name = input("Nhập tên bệnh nhân: ")
gender = input("Giới tính: ")
birth_year = input("Năm sinh: ")
phone = int(input("Nhập SDT: "))
email = input("Nhập email: ")
symptoms = input("Nhập triệu chứng của bệnh: ")
price = float(input("Chi phí khám bệnh: "))

cid = f"BN{birth_year}{random.randint(0, 999):03d}"

print(f"""------Thẻ bệnh nhân------
ID: {cid} {type(cid)}
Tên: {name} {type(name)}
Giới tính: {gender} {type(gender)}
Năm sinh: {birth_year} {type(birth_year)}
Điện thoại: {phone} {type(phone)}
Email: {email} {type(email)}
Triệu chứng: {symptoms} {type(symptoms)}
Chi phí: {price} {type(price)}""")
