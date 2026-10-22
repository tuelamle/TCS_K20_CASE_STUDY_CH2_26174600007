tong_phut = 135
cong_suat_w = 250

so_gio_tron_ven = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("So gio tron ven:",so_gio_tron_ven)
print("So phut con lai:",so_phut_con_lai)

su_dung_lau = tong_phut > 60
print("Su dung lau:", su_dung_lau)

du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print("Du lieu hop le:", du_lieu_hop_le)

#Bieu thuc 1 co ket qua la 160
#iBeu thuc 1 co ket qua la 360
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3
print("100 + 20 * 3 =", bieu_thuc_1)
print("(100 + 20) * 3 =", bieu_thuc_2)


