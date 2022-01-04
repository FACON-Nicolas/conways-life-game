class platform:
    """"""
    def __init__(self, height, width):
        self.__MAX_SIZE = 40
        self.__MIN_SIZE = 10
        self.__HEIGHT = self.__SizeIsCorrect(height)
        self.__WIDTH = self.__SizeIsCorrect(width)
        self.__platform = self.__makePlatform(self.__WIDTH, self.__HEIGHT)

    def isRange(self, case):
        l,c = case
        return l in range(self.__platform.__len__()) and c in range(self.__platform[0].__len__())

    def __SizeIsCorrect(self, size):
        assert(size >= self.__MIN_SIZE)
        if size in range(self.__MIN_SIZE, self.__MAX_SIZE): return size
        return self.__MAX_SIZE

    def CopyPlatform(self):
        """"""
        return [i.copy() for i in self.__platform]

    def __makePlatform(self, w, h):
        """"""
        return [[0 for _ in range(w)]for _ in range(h)]

    def checkCase(self, pos: tuple):
        """"""
        cases = 0
        r,c = pos
        for r_dir in range(-1,2):
            for c_dir in range(-1,2):
                if (r_dir, c_dir) != (0,0):
                    if self.isRange(r+r_dir, c+c_dir):
                        if self.__platform[r+r_dir][c+c_dir]:
                            cases += 1
        return cases

