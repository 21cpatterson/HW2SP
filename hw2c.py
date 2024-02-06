def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Use the Secant Method to find the root of a function.

    Parameters:
    - fcn (function): The function to find the root.
    - x0 (float): The first initial guess.
    - x1 (float): The second initial guess.
    - maxiter (int): Max number of iterations.
    - xtol (float): Exit if the absolute difference between consecutive
                   estimates is less than xtol.

    Returns:
    float: The final estimate of the root.
    """
    x_prev = x0
    x_current = x1

    for iteration in range(maxiter):
        f_prev = fcn(x_prev)
        f_current = fcn(x_current)

        if f_current - f_prev == 0:
            raise ValueError("Secant method: Division by zero.")

        x_new = x_current - f_current * (x_current - x_prev) / (f_current - f_prev)

        if abs(x_new - x_current) < xtol:
            return x_new

        x_prev = x_current
        x_current = x_new

    return x_current


def main():
    """
    Main function to demonstrate the Secant method for different equations.
    """
    fcn1 = lambda x: x - 3 * cos(x)
    root1 = Secant(fcn1, x0=1, x1=2, maxiter=5, xtol=1e-4)
    print(f"Root for x - 3cos(x) = 0: {root1}")

    fcn2 = lambda x: cos(2*x) * x**3
    root2 = Secant(fcn2, x0=1, x1=2, maxiter=15, xtol=1e-8)
    print(f"Root for cos(2x) * x^3 = 0: {root2}")

    fcn3 = lambda x: cos(2*x) * x**3
    root3 = Secant(fcn3, x0=1, x1=2, maxiter=3, xtol=1e-8)
    print(f"Root for cos(2x) * x^3 = 0 (limited iterations): {root3}")


if __name__ == "__main__":
    from math import cos
    main()
