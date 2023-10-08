from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы 1 символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО содержатся недопустимые символы")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 100:
            raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 100")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом, не менее 20 кг")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат пасспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер пасспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, new_fio):
        self.verify_fio(new_fio)
        self.__fio = new_fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        self.verify_old(new_old)
        self.__old = new_old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.verify_weight(new_weight)
        self.__weight = new_weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, new_ps):
        self.verify_ps(new_ps)
        self.__passport = new_ps

p1 = Person('Заживнов Антон Дмитриевич', 30, '1234 567890', 80.0)
p1.fio = 'Зажирнов Антон Дмитриевич'
print(p1.fio)
p1.fio = 'Заживнов Антон Дмитриевич'
print(p1.__dict__)