class Polynomial:

    def __init__(self, *coeffs):  # setting coeffs
        self.coeffs = list(coeffs)

    def __repr__(self):
        return "Polynomial" + str(tuple(self.coeffs))

    def __call__(self, x):  # calculate the polynomial with given x
        calculated = 0
        for index, coeff in enumerate(self.coeffs):
            calculated += coeff * x ** index
        return calculated

    def __add__(self, other):
        result = [sum(k) for k in Polynomial.group(self, other)]
        return Polynomial(*result)

    def __sub__(self, other):
        result = [k1 - k2 for k1, k2 in Polynomial.group(self, other)]
        return Polynomial(*result)

    def __mul__(self, other):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        # multiply every element of poly1 by every element of poly2
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(*result)

    def __bool__(self, x):
        return self.__call__(x) != 0

    # different implement of add (I was just checking if it will work)
    def add(self, other):
        size = max(len(self.coeffs), len(other.coeffs))
        sum = [0 for i in range(size)]
        for i in range(0, len(self.coeffs), 1):
            sum[i] = self.coeffs[i]
        for i in range(len(other.coeffs)):
            sum[i] += other.coeffs[i]
        return Polynomial(*sum)

    @staticmethod
    def group(poly1, poly2):  # this will group polys' terms
        c1 = poly1.coeffs
        c2 = poly2.coeffs
        for i in range(max(len(c1), len(c2))):
            if i >= len(c1):
                yield 0, c2[i]
            elif i >= len(c2):
                yield c1[i], 0
            else:
                yield c1[i], c2[i]
            # i += 1

    def print_polynomial(self):  # more "mathematical" way of print
        for i in range(len(self.coeffs)):
            print(self.coeffs[i], end="")
            if i != 0:
                print("x^", i, end="")
            if i != len(self.coeffs) - 1:
                print(" + ", end="")
        print()
