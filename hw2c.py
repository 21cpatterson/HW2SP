def gauss_seidel(A, b, x0, tol=1e-5, Niter=15):
    """
    Estimates the solution to a system of linear equations using the Gauss-Seidel method.

    Parameters:
    A (list[list[float]]): The matrix of coefficients.
    b (list[float]): The vector of constants.
    x0 (list[float]): The initial guess for the solution.
    tol (float): The tolerance for the stopping criterion. Default is 1e-5.
    Niter (int): The maximum number of iterations to perform. Default is 15.

    Returns:
    list[float]: The estimated solution to the system of linear equations.
    """
    # Initialize a list to store the new x vectors
    x_new = [x0[:]]

    # Iterate to compute the new x vectors
    for _ in range(Niter):
        x_new_temp = [0] * len(A)
        for i in range(len(A)):
            s1 = sum(A[i][j] * x_new[-1][j] for j in range(i))
            s2 = sum(A[i][j] * x_new_temp[j] for j in range(i))
            x_new_temp[i] = (b[i] - s1 - s2) / A[i][i]

            # Check if the maximum change in the components of the solution vector is below the tolerance
            if i == len(A) - 1:
                if all(abs(x_new_temp[k] - x_new[-1][k]) < tol for k in range(len(A))):
                    break

        x_new.append(x_new_temp)

    # Return the estimated solution
    return x_new[-1]

def main():
    # Define the first set of linear equations
    A1 = [[3, 1, -1],
           [1, 4, 1],
           [1, 3, 9]]
    b1 = [2, 1, 12]
    x01 = [1, 1, 1]

    # Estimate and print the solution to the first set of linear equations
    x_sol1 = gauss_seidel(A1, b1, x01)
    print("Solution to the first set of linear equations:")
    print(x_sol1)

    # Define the second set of linear equations
    A2 = [[1, 2, 0],
           [1, 3, 4],
           [1, 2, 7]]
    b2 = [12, 21, 3]
    x02 = [1, 1, 1]

    # Estimate and print the solution to the second set of linear equations
    x_sol2 = gauss_seidel(A2, b2, x02)
    print("Solution to the second set of linear equations:")
    print(x_sol2)

if __name__ == "__main__":
    main()