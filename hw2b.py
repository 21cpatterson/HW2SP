import math
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
    # Initialize the previous and current x values
    x_prev = x0
    x_curr = x1

    # Iterate until the maximum number of iterations is reached
    for _ in range(maxiter):
        # Evaluate the function at the previous and current x values
        f_prev = fcn(x_prev)
        f_curr = fcn(x_curr)

        # Compute the new x value using the Secant Method formula
        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)

        # Check if the new x value satisfies the exit criterion
        if abs(x_new - x_curr) < xtol:
            # If so, return the new x value
            return x_new

        # Otherwise, update the previous and current x values
        x_prev = x_curr
        x_curr = x_new

    # If the maximum number of iterations is reached, return the current x value
    return x_curr

def main():
    # Define the first function and its root
    root1 = Secant(lambda x: x - 3 * math.cos(x), 1, 2, maxiter=5, xtol=1e-4)

    # Define the second function and its root
    root2 = Secant(lambda x: math.cos(2*x) * x**3, 1, 2, maxiter=15, xtol=1e-8)

    # Define the second function and its root with a smaller number of iterations
    root3 = Secant(lambda x: math.cos(2*x) * x**3, 1, 2, maxiter=3, xtol=1e-8)

    # Print the roots
    print(f"Root of x - 3cos(x) = 0: {root1:.5f}")
    print(f"Root of cos(2x) * x^3 = 0: {root2:.5f}")
    print(f"Root of cos(2x) * x^3 = 0 (with maxiter=3): {root3:.5f}")

if __name__ == "__main__":
    main()