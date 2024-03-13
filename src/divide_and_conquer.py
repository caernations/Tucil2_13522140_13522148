def midpoint(p1, p2):
    return ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

def quadraticBezierDivideAndConquer(P0, P1, P2, iterations):
    if iterations == 0:
        return [P0, P2]

    Q0 = midpoint(P0, P1)
    Q1 = midpoint(P1, P2)
    R0 = midpoint(Q0, Q1)

    left_curve = quadraticBezierDivideAndConquer(P0, Q0, R0, iterations - 1)
    right_curve = quadraticBezierDivideAndConquer(R0, Q1, P2, iterations - 1)

    return left_curve + right_curve[1:]

def generate_control_points(P0, P1, P2, iterations):
    S0 = midpoint(P0, P1)
    S1 = midpoint(P1, P2)
    S2 = midpoint(S0, S1)

    T0 = midpoint(S0, S2)
    T1 = midpoint(S2, S1)

    return [P0, T0, S2, T1, P2]


### ini baru yg divide and conquer blm yg bruteforce