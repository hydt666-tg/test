def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = exgcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def inv(a, p):
    a %= p
    g, x, _ = exgcd(a, p)
    if g != 1:
        raise ValueError("No inverse")
    return x % p


INF = None


def point_add(P, Q, a, p):
    if P is INF:
        return Q
    if Q is INF:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return INF

    if P == Q:
        if y1 % p == 0:
            return INF

        lam = ((3 * x1 * x1 + a)
               * inv(2 * y1, p)) % p
    else:
        lam = ((y2 - y1)
               * inv(x2 - x1, p)) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)


def point_neg(P, p):
    if P is INF:
        return INF
    x, y = P
    return (x, (-y) % p)


def scalar_mul(k, P, a, p):
    R0 = INF
    R1 = P

    bits = bin(k)[2:]

    for bit in bits:
        if bit == '0':
            R1 = point_add(R0, R1, a, p)
            R0 = point_add(R0, R0, a, p)
        else:
            R0 = point_add(R0, R1, a, p)
            R1 = point_add(R1, R1, a, p)

    return R0


def main():
    p = int(input())
    a = int(input())
    b = int(input())

    G = tuple(map(int, input().split()))

    op = int(input())

    if op == 1:
        Pm = tuple(map(int, input().split()))
        k = int(input())
        PB = tuple(map(int, input().split()))
        N = int(input())

        C1 = scalar_mul(k, G, a, p)

        kPB = scalar_mul(k, PB, a, p)

        C2 = Pm

        for _ in range(N + 1):
            C2 = point_add(C2, kPB, a, p)

        print(C1[0], C1[1])
        print(C2[0], C2[1])

    else:
        C1 = tuple(map(int, input().split()))
        C2 = tuple(map(int, input().split()))
        nB = int(input())
        N = int(input())

        S = scalar_mul(nB, C1, a, p)

        Pm = C2

        negS = point_neg(S, p)

        for _ in range(N + 1):
            Pm = point_add(Pm, negS, a, p)

        print(Pm[0], Pm[1])


if __name__ == "__main__":
    main()