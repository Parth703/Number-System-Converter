def decimal_to_binary(num):
    remainder = []
    while(num/2 != 0):
        if num%2 == 0 :
            remainder.append(0)
        if num%2 == 1 :
            remainder.append(1)
        num = num//2
    remainder.reverse()
    return ''.join(map(str, remainder))
def D_to_B():
    num = int(input("Enter Decimal Value: "))
    ret = decimal_to_binary(num)
    print("Binary Value is: ", ret)
