from .tu import TuVung
from .tien_do import TienDo

class BaiHoc:
    def __init__(self, ma_bai, ten_bai, cap_do, chu_de):
        self.ma_bai = ma_bai
        self.ten_bai = ten_bai
        self.cap_do = cap_do
        self.chu_de = chu_de

        self.danh_sach_tu = []
        self.tien_do = TienDo()

    def them_tu(self, tu):
        if len(self.danh_sach_tu) < 8:
            self.danh_sach_tu.append(tu)

    def lay_danh_sach_tu(self):
        return self.danh_sach_tu

    def hien_thi(self):
        print("Lesson:", self.ten_bai)
        print("Cấp độ:", self.cap_do)
        print("Chủ đề:", self.chu_de)

        print("\nDanh sách từ:")

        for tu in self.danh_sach_tu:
           print(tu.tieng_anh, "-", tu.tieng_viet)