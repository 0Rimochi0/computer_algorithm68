import sys

def MainMenu():
    print("----- Calculator -----")
    print("Press Enter Q = Exit")
    print("Press Enter M = Menu")
    inp = input("Select : ")

    if(inp == "Q" or inp == "q"):
        print("Exit Goodbye~!")
        sys.exit()
    elif(inp == "M" or inp == "m"):
        Calculate()
    else:
        MainMenu()

def Calculate():
    print("\n--- Calculator Mode ---")
    print("H = Home")
    print("W = Addition(+)")
    print("X = Subtraction(-)")
    print("Y = Multiplication(*)")
    print("Z = Division(/)")
    print("E = Exponentiation(Power)(^)")

    inp = input("Select Operator : ")

    # --- Addition (บวก) ---
    if(inp == "W" or inp == "w"):
        try:
            N = int(input("ต้องการบวกกี่จำนวน : "))
            if N > 0:
                total = 0
                for x in range(N):
                    total += float(input(f"Number {x+1} : "))
                print(f">>> Total Sum = {total}")
            else:
                print("ต้องใส่จำนวนมากกว่า 0")
        except ValueError:
            print("ช่วยใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    # --- Subtraction (ลบ) ---
    elif(inp == "X" or inp == "x"):
        try:
            N = int(input("ต้องการลบกี่จำนวน : "))
            if N > 0:
                # รับค่าตัวตั้งตัวแรกก่อน
                total = float(input("Number 1 (ตัวตั้ง) : "))
                # ลูปรับค่าตัวลบที่เหลือ
                for x in range(N - 1):
                    val = float(input(f"Number {x+2} (ลบด้วย) : "))
                    total -= val
                print(f">>> Result = {total}")
            else:
                print("ต้องใส่จำนวนมากกว่า 0")
        except ValueError:
            print("ช่วยใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    # --- Multiplication (คูณ) ---
    elif(inp == "Y" or inp == "y"):
        try:
            N = int(input("ต้องการคูณกี่จำนวน : "))
            if N > 0:
                total = 1
                for x in range(N):
                    total *= float(input(f"Number {x+1} : "))
                print(f">>> Result = {total}")
            else:
                print("ต้องใส่จำนวนมากกว่า 0")
        except ValueError:
            print("ช่วยใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    # --- Division (หาร) ---
    elif(inp == "Z" or inp == "z"):
        try:
            N = int(input("ต้องการหารกี่จำนวน : "))
            if N > 0:
                # รับค่าตัวตั้งตัวแรกก่อน
                total = float(input("Number 1 (ตัวตั้ง) : "))
                is_error = False
                
                # ลูปรับค่าตัวหารที่เหลือ
                for x in range(N - 1):
                    val = float(input(f"Number {x+2} (หารด้วย) : "))
                    if val == 0:
                        print("Error!! Cannot divide by Zero.")
                        is_error = True
                        break
                    total /= val
                
                if not is_error:
                    print(f">>> Result = {total}")
            else:
                print("ต้องใส่จำนวนมากกว่า 0")
        except ValueError:
            print("ช่วยใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    # --- Exponentiation (ยกกำลัง) ---
    elif(inp == "E" or inp == "e"):
        try:
            N = int(input("ต้องการทำยกกำลังกี่จำนวน : "))
            if N > 0:
                # รับค่าฐานตัวแรก
                total = float(input("Number 1 (ตัวตั้ง) : "))
                
                # ลูปรับค่ากำลัง
                for x in range(N - 1):
                    val = float(input(f"Number {x+2} (ยกกำลัง) : "))
                    total **= val
                print(f">>> Result = {total}")
            else:
                print("ต้องใส่จำนวนมากกว่า 0")
        except ValueError:
            print("ช่วยใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    elif(inp == "H" or inp == "h"):
        MainMenu()

    else:
        print("Invalid Command.")
        Calculate()

MainMenu()