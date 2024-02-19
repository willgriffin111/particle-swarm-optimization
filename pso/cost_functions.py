

N = 20  

def dixonPriceFunc(x):
    utility = (x[0] - 1)**2
    for i in range(1, N):
        utility += i * (2 * x[i]**2 - x[i-1])**2
    return utility


def zakharovFunc(x):

    # Calculate sigma1
    sigma1 = 0
    for i in range(N):
        sigma1 += x[i]**2

    # Calculate sigma2
    sigma2 = 0
    for i in range(N):
        sigma2 += 0.5 * (i + 1) * x[i]

    # Calculate utility
    utility = sigma1 + sigma2**2 + sigma2**4
    return utility

if __name__ == "__main__":
    dixonPriceFunc()
    zakharovFunc()
