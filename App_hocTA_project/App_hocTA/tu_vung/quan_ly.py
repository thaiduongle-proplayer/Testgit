class QuanLyTuVung:
    def __init__(self):
        self.danh_sach_bai_hoc = []

    def them_bai_hoc(self, bai_hoc):
        self.danh_sach_bai_hoc.append(bai_hoc)

    def tim_theo_cap_do(self, cap_do):
        ket_qua = []

        for bai in self.danh_sach_bai_hoc:
            if bai.cap_do == cap_do:
                ket_qua.append(bai)

        return ket_qua

    def tim_theo_chu_de(self, chu_de):
        ket_qua = []

        for bai in self.danh_sach_bai_hoc:
            if bai.chu_de == chu_de:
                ket_qua.append(bai)

        return ket_qua

    def tim_bai(self, ma_bai):
        for bai in self.danh_sach_bai_hoc:
            if bai.ma_bai == ma_bai:
                return bai

        return None