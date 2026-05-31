def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(a, m):
    a %= m
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("inverse not exists")
    return x % m


def point_add(P, Q, a, p):
    # 无穷远点
    if P == (0, 0):
        return Q
    if Q == (0, 0):
        return P

    x1, y1 = P
    x2, y2 = Q

    # P + (-P) = O
    if x1 == x2 and (y1 + y2) % p == 0:
        return (0, 0)

    # 倍点
    if P == Q:
        lam = ((3 * x1 * x1 + a) * mod_inverse(2 * y1, p)) % p
    else:
        lam = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)


def point_neg(P, p):
    if P == (0, 0):
        return P
    x, y = P
    return (x, (-y) % p)


def scalar_mul(k, P, a, p):
    result = (0, 0)
    addend = P

    while k:
        if k & 1:
            result = point_add(result, addend, a, p)
        addend = point_add(addend, addend, a, p)
        k >>= 1

    return result


def main():
    p = int(input())
    a = int(input())
    b = int(input())
    G = tuple(map(int, input().split()))
    op=int(input())
    if op == 1:##代表加密
        P= tuple(map(int, input().split()))
        k=int(input())
        PB=tuple(map(int, input().split()))
        C1=scalar_mul(k,G, a, p)
        kp=scalar_mul(k,PB, a, p)
        C2=point_add(P,kp, a, p)
        print(C1[0], C1[1])
        print(C2[0], C2[1])
    else:
        C1=tuple(map(int, input().split()))
        C2=tuple(map(int, input().split()))
        nb=int(input())
        nk=scalar_mul(nb,C1, a, p)
        Pm=point_add(C2,point_neg(nk, p), a, p)
        print(Pm[0], Pm[1])

if __name__ == "__main__":
    main()