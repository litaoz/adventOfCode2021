'''
--- Part Two ---
As the submarine starts booting up things like the Retro Encabulator, you realize that maybe you don't need all these submarine features after all.

What is the smallest model number accepted by MONAD?


'''


def op(w, z, a, b, c):
    # inp w
    # mul x 0
    # add x z
    # mod x 26
    # div z .+(a)
    # add x .+(b)
    # eql x w
    # eql x 0
    # mul y 0
    # add y 25
    # mul y x
    # add y 1
    # mul z y
    # mul y 0
    # add y w
    # add y .+(c)
    # mul y x
    # add z y

    if z % 26 + b == w:
        # 0 <= x < 26
        # if b > 9: always false, for all a = 1
        # all a=26 must satisfy this
        z = z // 26
    else:
        if a == 26:  # should not happen if we want to end with 0
            z = z + w + c
        elif a == 1:
            z = z * 26 + w + c
    return z


def main():
    return

    '''
    inc a= 1, b= 12, c= 7  PUSH m1 +  7
    inc a= 1, b= 13, c= 8  PUSH m2 +  8
    inc a= 1, b= 13, c=10  PUSH m3 + 10
        a=26, b= -2, c= 4  POP  m4 == popped - 2
        a=26, b=-10, c= 4  POP  m5 == popped - 10
    inc a= 1, b= 13, c= 6  PUSH m6 + 6
        a=26, b=-14, c=11  POP  m7 == popped - 14
        a=26, b= -5, c=13  POP  m8 == popped - 5
    inc a= 1, b= 15, c= 1  PUSH m9 + 1
    inc a= 1, b= 15, c= 8  PUSH m10+ 8
        a=26, b=-14, c= 4  POP  m11== popped - 14
    inc a= 1, b= 10, c=13  PUSH m12+ 13
        a=26, b=-14, c= 4  POP  m13== popped - 14
        a=26, b= -5, c=14  POP  m14== popped - 5

    PUSH m1 +  7
    PUSH m2 +  8
    PUSH m3 + 10
    POP  m4 == popped - 2
    POP  m5 == popped - 10
    PUSH m6 + 6
    POP  m7 == popped - 14
    POP  m8 == popped - 5
    PUSH m9 + 1
    PUSH m10+ 8
    POP  m11== popped - 14
    PUSH m12+ 13
    POP  m13== popped - 14
    POP  m14== popped - 5

    PUSH m1 +  7
    PUSH m2 +  8
    PUSH m3 + 10
    POP  m4 == m3 + 8
    POP  m5 == m2 - 2
    PUSH m6 + 6
    POP  m7 == m6 - 8
    POP  m8 == m1 + 2
    PUSH m9 + 1
    PUSH m10 + 8
    POP  m11 == m10 - 6
    PUSH m12 + 13
    POP  m13 == m12 - 1
    POP  m14 == m9 - 4

    m4 == m3 + 8
    m5 == m2 - 2
    m7 == m6 - 8
    m8 == m1 + 2
    m11 == m10 - 6
    m13 == m12 - 1
    m14 == m9 - 4

    m3 == m4 - 8
    m1 == m8 - 2
    m5 == m2 - 2
    m7 == m6 - 8
    m11 == m10 - 6
    m13 == m12 - 1
    m14 == m9 - 4

    m4 == m3 + 8
    m2 == m5 + 2
    m6 == m7 + 8
    m8 == m1 + 2
    m10 == m11 + 6
    m12 == m13 + 1
    m9 == m14 + 4
    '''


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    result = main()
    print(result)  # 13191913571211
