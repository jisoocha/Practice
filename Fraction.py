def gcd(m, n):
    while m % n != 0:
        old_m = m

        m = n
        n = old_m % n
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self)

    def __add__(self, other):
        newnum = self.num * other.den + other.num * self.den
        newden = self.den * other.den

        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        return self.den * other.num == self.num * other.den

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)


if __name__ == '__main__':
    print(Fraction(3, 6) * Fraction(1, 2))
