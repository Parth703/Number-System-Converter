from bnirayotdceiaml import B_to_D
from oatclotdceiaml import O_to_D
from hxeaotdceiaml import H_to_D
from dceiamlotbniray import D_to_B
from dceiamlotoatcl import D_to_O
from dceiamlothxea import D_to_H

while True:
    print("Number System Converter")
    print("1. ANY To Decimal\n2. Decimal To ANY\n3. Exit")
    opt1 = int(input("Your Choice: "))
    if opt1 == 1:
        while True:
            print("1.From Binary To Decimal\n2.From Octal To Decimal\n3.From Hexa-Decimal To Decimal\n4.Exit")
            opt2 = int(input("Your Choice: "))
            if opt2 == 1:
                B_to_D()
            elif opt2 == 2:
                O_to_D()
            elif opt2 == 3:
                H_to_D()
            elif opt2 == 4:
                break
            else:
                print("Invalid Choice")
    elif opt1 == 2:
        while True:
            print("1.From Decimal To Binary\n2.From Decimal To Octal\n3.From Decimal To Hexa-Decimal\n4.Exit")
            opt2 = input("Your Choice: ")
            if opt2 == 1:
                D_to_B()
            elif opt2 == 2:
                D_to_O()
            elif opt2 == 3:
                D_to_H()
            elif opt2 == 4:
                break
            else:
                print("Invalid Choice")
    elif opt1 == 3:
        break
    else:
        print("Invalid Choice")
