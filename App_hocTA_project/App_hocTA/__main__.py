import os
import sys

try:
    from App_hocTA.tu_vung.tu import TuVung
    from App_hocTA.tu_vung.bai_hoc import BaiHoc
    from App_hocTA.tu_vung.quan_ly import QuanLyTuVung
except ModuleNotFoundError:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from App_hocTA.tu_vung.tu import TuVung
    from App_hocTA.tu_vung.bai_hoc import BaiHoc
    from App_hocTA.tu_vung.quan_ly import QuanLyTuVung


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    # Tạo bộ quản lý
    quan_ly = QuanLyTuVung()

    bai1 = BaiHoc(
        1,
        "Lesson 1",
        "A1",
        "Family"
    )

    bai1.them_tu(TuVung(
        1,
        "mother",
        "mẹ",
        "noun",
        "/ˈmʌðər/",
        "mother.mp3",
        "My mother is a teacher.",
        "A1"
    ))

    bai1.them_tu(TuVung(
        2,
        "father",
        "bố",
        "noun",
        "/ˈfɑːðər/",
        "father.mp3",
        "My father is a doctor.",
        "A1"
    ))

    bai1.them_tu(TuVung(
        3,
        "brother",
        "anh/em trai",
        "noun",
        "/ˈbrʌðər/",
        "brother.mp3",
        "I have one brother.",
        "A1"
    ))

    bai1.them_tu(TuVung(
        4,
        "sister",
        "chị/em gái",
        "noun",
        "/ˈsɪstər/",
        "sister.mp3",
        "My sister is a student.",
        "A1"
    ))

    bai1.them_tu(TuVung(
        5,
        "parents",
        "bố mẹ",
        "noun",
        "/ˈperənts/",
        "parents.mp3",
        "My parents live in Vietnam.",
        "A1"
    ))

    bai1.them_tu(TuVung(
        6,
        "son",
        "con trai",
        "noun",
        "/sʌn/",
        "son.mp3",
        "They have a son.",
        "A1"
    ))

    bai1.them_tu(TuVung(
        7,
        "daughter",
        "con gái",
        "noun",
        "/ˈdɔːtər/",
        "daughter.mp3",
        "Their daughter is five years old.",
        "A1"
    ))

    bai1.them_tu(TuVung(
        8,
        "family",
        "gia đình",
        "noun",
        "/ˈfæməli/",
        "family.mp3",
        "I have a small family.",
        "A1"
    ))

    # Đưa Lesson vào quản lý
    quan_ly.them_bai_hoc(bai1)

    # Hiển thị Lesson
    bai1.hien_thi()


if __name__ == "__main__":
    main()
