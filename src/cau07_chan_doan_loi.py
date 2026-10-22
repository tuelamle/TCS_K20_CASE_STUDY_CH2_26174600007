ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
#Cho loi
#ten tep: cau07_chan_doan_loi.py
#so dong: dong 5
#loai loi: TypeError
#thong bao loi: unsupported operand type(s) for /: 'str' and 'int'

#Nguyen nhan: cong_suat_w la chuoi str do dung input().
#Cach sua: dung float() de chuyen cong suat sang so thuc.