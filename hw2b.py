def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Use the Secant Method to find the root of fcn(x) in the neighborhood of x0 and x1.

    Parameters:
    - fcn: the function for which we want to find the root
    - x0 and x1: two x values in the neighborhood of the root
    - xtol: exit if the |xnewest - xprevious| < xtol
    - maxiter: exit if the number of iterations (new x values) equals this number

    Returns:
    - The final estimate of the root (most recent new x value)
    """
    x_prev = x0
    x_curr = x1

    for _ in range(maxiter):
        f_prev = fcn(x_prev)
        f_curr = fcn(x_curr)

        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)

        if abs(x_new - x_curr) < xtol:
            return x_new

        x_prev = x_curr
        x_curr = x_new

    return x_curr

def main():

    root1 = Secant(lambda x: x - 3 * math.cos(x), 1, 2, maxiter=5, xtol=1e-4)

    root2 = Secant(lambda x: math.cos(2*x) * x**3, 1, 2, maxiter=15, xtol=1e-8)

    root3 = Secant(lambda x: math.cos(2*x) * x**3, 1, 2, maxiter=3, xtol=1e-8)

    print(f"Root of x - 3cos(x) = 0: {root1:.5f}")
    print(f"Root of cos(2x) * x^3 = 0: {root2:.5f}")
    print(f"Root of cos(2x) * x^3 = 0 (with maxiter=3): {root3:.5f}")

if __name__ == "__main__":
    import math
    main()
