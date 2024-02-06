import math

def Simpson_13(PDF, args, a, b, n=1000):
    h = (b - a) / n
    x = a
    integral = PDF(args, x)

    for i in range(1, n, 2):
        x += h
        integral += 4 * PDF(args, x)

    x = a + h

    for i in range(2, n - 1, 2):
        x += h
        integral += 2 * PDF(args, x)

    integral *= h / 3
    return integral


def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability of x being less than or greater than a given value.

    Parameters:
    - PDF: callback function for the Gaussian/normal probability density function
    - args: tuple containing μ and σ
    - c: floating point value (upper limit of integration)
    - GT: boolean indicating if we want the probability of x being greater than c (GT=True) or less than c (GT=False)

    Returns:
    - Probability value
    """
    mu, sigma = args
    if GT:
        a = mu - 5 * sigma
        b = c
    else:
        a = c
        b = mu + 5 * sigma

    result = Simpson_13(PDF, args, a, b)
    return result

def main():

    result1 = Probability(
        lambda args, x: (1 / (args[1] * math.sqrt(2 * math.pi))) * math.exp(-(x - args[0]) ** 2 / (2 * args[1] ** 2)),
        (100, 12.5), 105, GT=False)

    result2 = Probability(
        lambda args, x: (1 / (args[1] * math.sqrt(2 * math.pi))) * math.exp(-(x - args[0]) ** 2 / (2 * args[1] ** 2)),
        (100, 3), 100 + 2 * 3, GT=True)

    print(f'P(x<105|N(100,12.5))={result1:.2f}')
    print(f'P(x>{100 + 2 * 3:.2f}|N(100,3))={result2:.2f}')


if __name__ == "__main__":
    main()
