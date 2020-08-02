def decimal_to_octal(num):
    remainder = []
    while(num/8 != 0):
        for n in range(8):
            if num%8 == n:
                remainder.append(n)
        num = num//8
    remainder.reverse()
    return ''.join(map(str, remainder))
def D_to_O():
    num = int(input("Enter Decimal Value: "))
    ret = decimal_to_octal(num)
    print("Octal Value is: ", ret)
