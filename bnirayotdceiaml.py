def binary_to_decimal(num):
	integer = []
	fractional = []
	for ind,i in enumerate(num):
		if i == ".":
			for j in num[0:ind]:
				integer.append(j)
			for k in num[ind+1:]:
				fractional.append(k)
	for j in num:
		integer.append(j)
	twos_mul = 1
	new_int = 0
	for val in integer[::-1] :
		new_int = new_int + int(val)*twos_mul
		twos_mul *= 2
	#To do for fractoinal value uptill 4 decimals!!
	return new_int

num = input("Enter the Binary Value: ")
ret = binary_to_decimal(num)
print("The Decimal Value is: ",ret)