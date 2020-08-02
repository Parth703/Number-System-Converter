def decimal_to_hexadecimal(num):
    remainder = []
    while(num/16!= 0):
        if num%16 == 10:
            remainder.append("A")
        if num%16 == 11:
            remainder.append("B")
        if num%16 == 12:
            remainder.append("C")
        if num%16 == 13:
            remainder.append("D")
        if num%16 == 14:
            remainder.append("E")
        if num%16 == 15:
            remainder.append("F")
        for n in range(10):
            if num%16 == n:
                remainder.append(n)
        num = num//16
    remainder.reverse()
    return ''.join(map(str, remainder))

num = int(input("Enter Decimal Value: "))
ret = decimal_to_hexadecimal(num)
print("Octal Value is: ", ret)