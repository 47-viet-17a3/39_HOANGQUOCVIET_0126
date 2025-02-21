import math
class TamGiac:
    def __init__(self, canh_a, canh_b, canh_c):
        self.canh_a = canh_a  
        self.canh_b = canh_b  
        self.canh_c = canh_c  

    def chu_vi(self):
        return self.canh_a + self.canh_b + self.canh_c

    def dien_tich(self):
        p = self.chu_vi() / 2  
        return math.sqrt(p * (p - self.canh_a) * (p - self.canh_b) * (p - self.canh_c))

    def hien_thi(self):
        print(f"Cạnh a: {self.canh_a}, Cạnh b: {self.canh_b}, Cạnh c: {self.canh_c}")
        print(f"Chu vi tam giác: {self.chu_vi()}")
        print(f"Diện tích tam giác: {self.dien_tich()}")

class TamGiacCan(TamGiac):
    def __init__(self, canh_ben, canh_day):
        super().__init__(canh_ben, canh_day, canh_ben)

class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)

class TamGiacVuong(TamGiac):
    def __init__(self, canh_goc_vuong_1, canh_goc_vuong_2):
        canh_huyen = math.sqrt(canh_goc_vuong_1**2 + canh_goc_vuong_2**2)
        super().__init__(canh_goc_vuong_1, canh_goc_vuong_2, canh_huyen)

    def hien_thi(self):
        print("Tam giác vuông:")
        super().hien_thi()
if __name__ == "__main__":
    print("Tam giác thường:")
    tam_giac = TamGiac(3, 4, 5)
    tam_giac.hien_thi()

    print("\nTam giác vuông:")
    tam_giac_vuong = TamGiacVuong(3, 4)
    tam_giac_vuong.hien_thi()

    print("\nTam giác cân:")
    tam_giac_can = TamGiacCan(5, 6)
    tam_giac_can.hien_thi()

    print("\nTam giác đều:")
    tam_giac_deu = TamGiacDeu(4)
    tam_giac_deu.hien_thi()
