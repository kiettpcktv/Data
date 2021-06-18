# Code by Pham Van Minh
# Chỉ dùng để tham khảo
# Chỉ dùng để tham khảo
# Chỉ dùng để tham khảo
# Chỉ dùng để tham khảo
# Chỉ dùng để tham khảo
# Chỉ dùng để tham khảo
# Chỉ dùng để tham khảo

# Hàm tính tổng các PV qua hằng năm có 2 tham số đầu vào t: số năm, r: lãi suất
def tong_pv_hang_nam(t,r):
	# Tạo biến đếm
	total_pv=0
	# Cho vòng lặp từ 0 đến t-1
	for i in range (0,t):
		# Cho nhập doanh thu của hằng năm
		a=int(input("Nhap doanh thu nam "+str(i+1)+": "))
		# Tính PV của mỗi năm
		pv=a/(1+r/100)**(i+1)
		# Cộng dồn vào biến đếm
		total_pv=total_pv+pv
	# Trả về kết quả tổng các PV hằng năm
	return total_pv

# Ví dụ
gia_tri_dau_tu_ban_dau=int(input("Nhap gia tri dau tu ban dau: "))
lai_suat=int(input("Nhap lai suat: "))
so_nam_dau_tu=int(input("Nhap so nam dau tu: "))
# tong_pv bằng kết quả của hàm tong_pv_hang_nam truyền 2 tham số đầu vào so_nam_dau_tu,lai_suat
tong_pv=tong_pv_hang_nam(so_nam_dau_tu,lai_suat)

npv=tong_pv-gia_tri_dau_tu_ban_dau

print("NPV: "+str(npv))
