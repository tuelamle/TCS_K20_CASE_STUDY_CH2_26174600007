cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# Dien nang = 250 * 90 / 60 / 1000 = 0.375 kWh
# Chi phi = 0.375 * 3000 = 1125 dong
print("Dien nang tieu thu:", dien_nang_kwh, "kWh")
print("Kieu du lieu", type(dien_nang_kwh))

print("Chi phi:", chi_phi, "đồng")
print("Kieu du lieu:", type(chi_phi))

so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang trong 60p:", dien_nang_kwh, "kWh")
print("Chi phi sau 60p:", chi_phi, "dong")