
def poly_string(coefficients):
    """:returns the string representation of the polynomial."""
    res = "f(x) ="
    super_script = str.maketrans("0123456789+-=()ni.", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱ·")
    size_coeff = len(coefficients)
    for i in range(size_coeff):
        degree = size_coeff - i - 1
        c_ = coefficients[i]
        if c_ == 0 and size_coeff == 1:
            res += " 0"
        if c_ == 0:
            pass
        else:
            if c_ > 0 and i > 0:
                res += " + "
            elif c_ < 0:
                res += " - "
            else:
                res += " "
            if abs(c_) != 1 or degree == 0:
                res += str(abs(c_))
            if degree > 0:
                res += "x"
                if degree != 1:
                    res += str(degree).translate(super_script)

    return res


if __name__ == '__main__':
    print(poly_string([1,0]))
