from typing import List, Dict, Optional

def main():
    items: List[Dict] = []

    while True:
        print("\n=== Smart Menu Analyzer ===")
        print("1) เพิ่มเมนู")
        print("2) ลบเมนู")
        print("3) แสดงรายการทั้งหมด")
        print("4) หาถูกสุด/แพงสุด")
        print("5) ยอดรวม/ค่าเฉลี่ย")
        print("6) นับเมนูที่ราคา > X")
        print("7) เรียงราคา (เลือกรูปแบบได้)")  # แก้ข้อความตรงนี้เล็กน้อย
        print("8) ใส่ข้อมูลตัวอย่าง (Sample Data)")
        print("0) ออก")

        choice = input("เลือกเมนู : ").strip()

        if choice == "1":
            add_item(items)
        elif choice == "2":
            remove_item(items)
        elif choice == "3":
            show_items(items)
        elif choice == "4":
            find_min_max(items)
        elif choice == "5":
            total_and_average(items)
        elif choice == "6":
            count_items_greater_than(items)
        elif choice == "7":
            sort_items_bubble(items)  # เรียกฟังก์ชันที่แก้ไขแล้ว
        elif choice == "8":
            add_sample_data(items)
        elif choice == "0":
            print("👋 ออกจากโปรแกรม")
            break
        else:
            print("❌ กรุณาเลือกเมนูให้ถูกต้อง")

# --- Helper Functions for Input ---

def input_float(prompt: str) -> float:
    while True:
        try:
            s = input(prompt).strip()
            value = float(s)
            if value < 0:
                print("❌ ราคาต้องเป็นค่าบวก")
                continue
            return value
        except ValueError:
            print("❌ กรุณากรอกตัวเลขทศนิยมที่ถูกต้อง")

def input_int(prompt: str) -> int:
    while True:
        try:
            s = input(prompt).strip()
            value = int(s)
            return value
        except ValueError:
            print("❌ กรุณากรอกตัวเลขจำนวนเต็มที่ถูกต้อง")

# --- Core Functions ---

def show_items(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    print("\n--- รายการเมนู ---")
    for i, it in enumerate(items, start=1):
        print(f"{i:>2}) {it['name']:<20} {it['price']:>8.2f} บาท")
    print("------------------\n")

def add_item(items: List[Dict]) -> None:
    name = input("ชื่อเมนู : ").strip()
    if not name:
        print("❌ ชื่อเมนูห้ามว่าง")
        return
    price = input_float("ราคา : ")
    items.append({"name": name, "price": price})
    print("✅ เพิ่มเมนูเรียบร้อย")

def remove_item(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    
    show_items(items)
    idx = input_int("ใส่ลำดับเมนูที่จะลบ: ")
    
    if idx < 1 or idx > len(items):
        print("❌ ลำดับไม่ถูกต้อง")
        return
        
    removed = items.pop(idx - 1)
    print(f"✅ ลบเมนู: {removed['name']} ราคา {removed['price']:.2f} บาท เรียบร้อยแล้ว")

def find_min_max(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    min_item = min(items, key=lambda x: x["price"])
    max_item = max(items, key=lambda x: x["price"])
    
    print(f"\n💸 ถูกสุด: {min_item['name']} = {min_item['price']:.2f} บาท")
    print(f"💰 แพงสุด: {max_item['name']} = {max_item['price']:.2f} บาท")

def total_and_average(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    
    total = sum(item['price'] for item in items)
    avg = total / len(items)
    
    print(f"\n💵 ราคารวมทั้งหมด: {total:.2f} บาท")
    print(f"📊 ราคาเฉลี่ย:     {avg:.2f} บาท")

def count_items_greater_than(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
        
    target = input_float("นับเมนูที่ราคามากกว่าเท่าไหร่? : ")
    count = 0
    print(f"\n--- รายการที่ราคา > {target} ---")
    for item in items:
        if item['price'] > target:
            print(f"- {item['name']} ({item['price']:.2f})")
            count += 1
            
    if count == 0:
        print("ไม่มีรายการที่ราคามากกว่าที่กำหนด")
    else:
        print(f"📌 รวมทั้งหมด: {count} รายการ")

# --- ส่วนที่แก้ไข: ฟังก์ชันเรียงลำดับ ---
def sort_items_bubble(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return

    print("\nเลือกรูปแบบการเรียงลำดับ:")
    print("1) มาก -> น้อย (แพงสุดขึ้นก่อน)")
    print("2) น้อย -> มาก (ถูกสุดขึ้นก่อน)")
    
    sub_choice = input("เลือก: ").strip()
    
    if sub_choice not in ("1", "2"):
        print("❌ ตัวเลือกไม่ถูกต้อง กลับสู่เมนูหลัก")
        return

    # Bubble Sort
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            should_swap = False
            
            if sub_choice == "1": 
                # มาก -> น้อย: ถ้าตัวหน้า "น้อยกว่า" ตัวหลัง ให้สลับ
                if items[j]['price'] < items[j + 1]['price']:
                    should_swap = True
            else:
                # น้อย -> มาก: ถ้าตัวหน้า "มากกว่า" ตัวหลัง ให้สลับ
                if items[j]['price'] > items[j + 1]['price']:
                    should_swap = True
            
            if should_swap:
                # สลับตำแหน่ง
                items[j], items[j + 1] = items[j + 1], items[j]
    
    mode_text = "มาก -> น้อย" if sub_choice == "1" else "น้อย -> มาก"
    print(f"✅ เรียงลำดับราคา ({mode_text}) เรียบร้อย")
    show_items(items)

def add_sample_data(items: List[Dict]) -> None:
    samples = [
        {"name": "Espresso", "price": 45.0},
        {"name": "Latte", "price": 55.0},
        {"name": "Green Tea", "price": 50.0},
        {"name": "Cocoa", "price": 60.0},
        {"name": "Water", "price": 10.0},
    ]
    items.extend(samples)
    print(f"✅ เพิ่มข้อมูลตัวอย่าง {len(samples)} รายการเรียบร้อย")

if __name__ == "__main__":
    main()