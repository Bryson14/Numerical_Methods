# Adaptive Quadrature Integration
def adap_quad_integration(a, b, function, tol):
    c = (a + b) / 2
    I_1 = ((b - a) / 6) * (function(a) + 4 * function(c) + function(b))
    I_2 = ((b - a) / 12) * (function(a) + 4 * function((a + c) / 2) + 2 *
                            function(c) + 4 * function((b + c) / 2) + function(b))

    # if the difference between I_1 and I_2 is less that user defined tolerance, return
    if abs(I_1 - I_2) <= tol:
        return 16 * I_2 / 15 - I_1 / 15
    else:
        # else split the area is half and add the sums through recursion stack
        return adap_quad_integration(a, c, function, tol) +\
               adap_quad_integration(c, b, function, tol)
