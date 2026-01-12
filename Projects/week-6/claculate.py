import sys

def MainMenu():
    print("-------------------------")
    print("Press Enter Q = Exit")
    print("C = Calculate")
    inp = input("Select : ")
    
    if(inp == "Q" or inp == "q"):
        print("Goodbye!")
        sys.exit() # ใช้คำสั่งนี้เพื่อปิดโปรแกรมอย่างสมบูรณ์
    elif(inp == "C" or inp == "c"):
        Calculate()
    else:
        MainMenu()

def Calculate():
    print("\n--- Calculator Mode (เครื่องคิดเลข) ---")
    print("+ = Plus การบวก (บวกเลขหลายจำนวน)")
    print("- = Minus การลบ (A - B)")
    print("* = Multiply การคูณ (การคูณเลขหลายจำนวน)")
    print("/ = Divide การหาร (A / B)")
    print("** = Power การคำนวณเลขยกกำลัง (A ** B)")
    print("M = Main/Home")
    
    inp = input("Select Operator กรุณาใส่เครื่องหมายการคำนวณ : ")

    # --- บวกเลข (+) ---
    if(inp == "+"):
        try:
            N = int(input("ต้องการบวกกี่จำนวนครับ? : "))
            total = 0
            for x in range(N):
                # ใช้ float เพื่อรับทศนิยมได้
                total += float(input(f"Number {x+1} : ")) 
            print(f">>> Total Sum = {total}")
        except ValueError:
            print("กรุณาใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    # --- ลบเลข (-) ---
    elif(inp == "-"):
        try:
            num1 = float(input("เลขตัวตั้ง : "))
            num2 = float(input("ลบด้วย : "))
            print(f">>> Result = {num1 - num2}")
        except ValueError:
            print("กรุณาใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    # --- คูณเลข (*) ---
    elif(inp == "*"):
        try:
            N = int(input("ต้องการคูณกี่จำนวนครับ? : "))
            total = 1 # การคูณต้องเริ่มที่ 1 (ถ้าเริ่ม 0 จะได้ 0 ตลอด)
            for x in range(N):
                total *= float(input(f"Number {x+1} : "))
            print(f">>> Result = {total}")
        except ValueError:
            print("กรุณาใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    # --- หารเลข (/) ---
    elif(inp == "/"):
        try:
            num1 = float(input("เลขตัวตั้ง : "))
            num2 = float(input("เลขหาร : "))
            if num2 == 0:
                print("กรุณาใส่แค่ตัวเลขเท่านั้น!!!")
            else:
                print(f">>> Result = {num1 / num2}")
        except ValueError:
            print("กรุณาใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()
        
    # --- เลขยกกำลัง (^) ---
    elif(inp == "**"):
        try:
            base = float(input("เลขตัวตั้ง : "))
            power = float(input("เลขยกกำลัง : "))
            # ใช้ ** แทนการยกกำลัง
            print(f">>> Result = {base ** power}") 
        except ValueError:
            print("กรุณาใส่แค่ตัวเลขเท่านั้น!!!")
        Calculate()

    # --- กลับเมนูหลัก ---
    elif(inp == "M" or inp == "m"):
        MainMenu()
    
    # --- กดผิด ---
    else:
        print("Invalid Command.")
        Calculate()

# เริ่มต้นโปรแกรม

MainMenu()
