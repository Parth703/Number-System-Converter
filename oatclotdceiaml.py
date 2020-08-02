def octal_to_decimal(num):
    integer = []
    for j in num :
        integer.append(j)
    eights_mul = 1
    new_int = 0
    for val in integer[::-1] :
        new_int = new_int + int(val)*eights_mul
        eights_mul *= 8
	    #To do for fractoinal value uptill 4 decimals!!
    return new_int

num = input("Enter the Octal Value: ")
ret = octal_to_decimal(num)
print("The Decimal Value is: ",ret)