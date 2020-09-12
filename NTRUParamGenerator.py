from random import randint


def generate_N(p):
    while(True):
        N = randint(100, 512)
        if gcd(N, p) == 1:
            return N

def generate_q(N, p):
    while(True):
        q = random_prime(512, False, 4)
        if (N)/2 < q < N - 1 and q != p:
            return q

def generate_polynomial_ring(p, N):
    FP=GF(p)
    RP.<x>=PolynomialRing(FP)
    ring.<x>=RP.quotient(x^(N - 1))
    return ring

def generate_ring_element(ring):
    return ring.random_element()

def calculate_probability(N, q):
    Z.<x> = ZZ[]
    factors = factor(x**N-1)
    factor_degree = [single_factor[0].degree() for single_factor in factors]
    probability = 1 - float(1/(q^factor_degree[0]))

    for i in range(1, len(factor_degree) - 1):
        probability *= 1 - float(1/(q^factor_degree[i]))
        return probability

def main_test():
    for i in range(1000):
        p = random_prime(512, False, 11)
        N = generate_N(p)
        q = generate_q(N,p)
        ring = generate_polynomial_ring(p,N)
        inverse_numbers = 1000

        if q:
            probability = calculate_probability(N,q) * 100
            for k in range(1000):
                try:
                    random_element = generate_ring_element(ring)
                    inverse = random_element^(-1)
                except:
                    inverse_numbers -= 1
            print(" p {} ; q {} ; N {} ; inverse {} ; probability {} " .format(p, q, N, inverse_numbers, probability))

main_test()
