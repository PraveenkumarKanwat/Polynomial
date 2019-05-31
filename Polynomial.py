import poly_string as ps


class Polynomial:

    def __init__(self, coefficients=[0]):
        """Initializes the polynomial by passing the coefficients of polynomial."""
        self.coefficients = list(coefficients)
        self.refresh_coefficients()

    def __repr__(self):
        return f"Polynomial({self.coefficients})"

    def __str__(self):
        """
        :returns the string representation of the polynomial.
        example : f(x) = x² + 2x + 1 for coefficients = [1, 2, 1]
        """
        return ps.poly_string(self.coefficients)

    def __len__(self):
        """:returns the degree of the polynomial"""
        return len(self.coefficients) - 1

    def __add__(self, other):
        """
        :param other: the other polynomial provided
        :return: the addition of two polynomial self and other
        """
        big, small = (self.coefficients, other.coefficients) if len(self.coefficients) >= len(other.coefficients) \
            else (other.coefficients, self.coefficients)
        big = list(big)
        diff = len(big) - len(small)
        for i in range(len(small)):
            big[i + diff] += small[i]
        return Polynomial(big)

    def __sub__(self, other):
        """
        :param other: the other polynomial provided
        :return: the subtraction of two polynomial self and other
        """
        return self.__add__(-other)

    def __mul__(self, other):
        new_coeff = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                new_coeff[i+j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(new_coeff)

    def __eq__(self, other):
        return self.coefficients == other.coefficients

    def __neg__(self):
        new_coeff = [-x for x in self.coefficients]
        return Polynomial(new_coeff)

    def __pow__(self, power, modulo=None):
        result = Polynomial([1])
        for i in range(power):
            result = result.__mul__(self)
        return result

    def __call__(self, *args, **kwargs):
        """calculates the value of function at a given value(s) of x"""
        result = []
        if len(args) == 0:
            raise TypeError("takes one or more arguments (0 given)")
        for arg in args:
            value = 0
            for coefficient in self.coefficients:
                value = value * arg + coefficient
            result.append(value)
        if len(args) == 1:
            return result[0]
        return tuple(result)

    def refresh_coefficients(self):
        """Updates coefficients after any operations that affects the coefficient."""
        while self.coefficients[0] == 0 and len(self.coefficients) > 1:
            self.coefficients.remove(0)

    def differentiate(self, inplace=False):
        """
        Calculates the differentiation of the polynomial.
        :param inplace: boolean: weather to replace the current polynomial with its derivative
        :return: new polynomial with after differentiation.
        """
        degree = len(self.coefficients) - 1
        new_coeff = [0] * degree
        for i in range(0, degree):
            new_coeff[i] = self.coefficients[i] * (degree - i)
        if inplace:
            self.coefficients = new_coeff
        return Polynomial(new_coeff)

    def integrate(self, constant=0, inplace=False):
        """
        Calculates the integration of the polynomial.
        :param constant: the constant of integration default assumed to be 0.
        :param inplace: boolean: weather to replace the current polynomial with its integral.
        :return: new polynomial with after integration.
        """
        degree = len(self.coefficients) + 1
        new_coeff = [0] * degree
        new_coeff[degree - 1] = constant
        for i in range(0, degree - 1):
            new_coeff[i] = self.coefficients[i] / (degree - i - 1)
        if inplace:
            self.coefficients = new_coeff
        return Polynomial(new_coeff)

    def definite_integral(self, x1, x2):
        """:returns definite ingration of the polynomial from x1 to x2 """
        value_x1, value_x2 = self.integrate()(x1, x2)
        return value_x2 - value_x1


if __name__ == '__main__':
    p = Polynomial([4,0,0,1])
    p2 = Polynomial([1,-1])
    p3 = Polynomial([1,-1])
    print(p, p2, p-p2)
    print(p2**4)
    # print(p)
    # print(p2)
    print(p-p2)
    # print(p2)
    # print(-p)
    # print(p)
    # # print(p.definite_integral(2,3))
    # print(p.integrate(constant=4))
