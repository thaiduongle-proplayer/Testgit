class TienDo:
    def __init__(self, tong_tu=8):
        self.tong_tu = tong_tu
        self.so_tu_da_hoc = 0
        self.so_cau_dung = 0
        self.so_cau_da_lam = 0

    def cap_nhat_tien_do(self, so_tu):
        self.so_tu_da_hoc = so_tu

    def phan_tram(self):
        if self.tong_tu == 0:
            return 0

        return self.so_tu_da_hoc / self.tong_tu * 100

    def cap_nhat_ket_qua(self, dung):
        self.so_cau_da_lam += 1

        if dung:
            self.so_cau_dung += 1

    def tinh_diem(self):
        if self.so_cau_da_lam == 0:
            return 0

        return self.so_cau_dung / self.so_cau_da_lam * 100