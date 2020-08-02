def hexadecimal_to_decimal(num):
    integer = []
    for j in num :
        integer.append(j)
    hex_mul = 1
    new_int =0 
    for val in integer[::-1]:
        if val == "A":
            new_int += 10*hex_mul
        elif val == "B":
            new_int += 11*hex_mul
        elif val == "C":
            new_int += 12*hex_mul
        elif val == "D":
            new_int += 13*hex_mul
        elif val == "E":
            new_int += 14*hex_mul
        elif val == "F":
            new_int += 15*hex_mul
        else:
            new_int += int(val)*hex_mul
        hex_mul *= 16
    return new_int

num = input("Enter Hexa-Decimal Number: ")
ret = hexadecimal_to_decimal(num)
print("Decimal Value is: ", ret)