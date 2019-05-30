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

    def __call__(self, *args, **kwargs):
        print(args, kwargs)

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
        :param inplace: boolean: weather to replace the current polynomial with its integral
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


if __name__ == '__main__':
    p = Polynomial([4,0,0,1])
    p(4,{"2":1})
    print(p.differentiate())
    print(p.integrate())
