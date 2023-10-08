class Person:
    def __init__(self, fio, old, ps, weight):
        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    #@classmethod