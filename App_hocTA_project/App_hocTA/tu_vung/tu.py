class TuVung:
    def __init__(self, ma_tu, tieng_anh, tieng_viet,
                 loai_tu, ipa, am_thanh, cau_mau, cap_do):

        self.ma_tu = ma_tu
        self.tieng_anh = tieng_anh
        self.tieng_viet = tieng_viet
        self.loai_tu = loai_tu
        self.ipa = ipa
        self.am_thanh = am_thanh
        self.cau_mau = cau_mau
        self.cap_do = cap_do

    def hien_thi(self):
        print("Từ:", self.tieng_anh)
        print("Loại từ:", self.loai_tu)
        print("IPA:", self.ipa)
        print("Nghĩa:", self.tieng_viet)
        print("Câu mẫu:", self.cau_mau)