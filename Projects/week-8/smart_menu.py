1111
def input_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v < 0:
                print("ราคาไม่ควรติดลบ")
                continue
            return v
        except ValueError:
            print("กรุณากรอกตัวเลข")

def show_menu():
    print("\n=== Smart Menu Analyzer ===")
    print("1) Add item")
    print("2) Show all")
    print("3) Update item price")
    print("4) Delete item")
    print("5) Search by name")
    print("6) Summary")
    print("7) Count price > X")
    print("8) Sort by price")
    print("0) Exit")

def add_item(items):
    print("\n--- เพิ่มเมนูใหม่ ---")
    name = input("ชื่อเมนู: ").strip()
    if not name:
        print("Error: ชื่อเมนูไม่ควรว่าง")
        return
    price = input_float("ราคา: ")
    items.append({"name": name, "price": price})
    print(f"บันทึก '{name}' ราคา {price} บาท เรียบร้อยแล้ว")

def show_items(items):
    if not items:
        print("\n[!] ยังไม่มีข้อมูลเมนู")
        return
    print("\n--- รายการเมนูทั้งหมด ---")
    # แก้ไข formatting ให้แสดงเลขลำดับสวยงาม
    for i, item in enumerate(items, start=1):
        print(f"{i:>2}. {item['name']:<20} - {item['price']:8.2f} บาท")
    print("-" * 35)

def update_item(items):
    show_items(items)
    if not items:
        return
    
    print("\n--- อัพเดทราคาเมนู ---")
    try:
        idx = int(input("เลือกหมายเลขเมนูที่จะแก้ไข: ")) - 1
        if 0 <= idx < len(items):
            target = items[idx]
            print(f"กำลังแก้ไข: {target['name']} (ราคาเดิม {target['price']})")
            new_price = input_float("ราคาใหม่: ")
            target['price'] = new_price
            print(">> อัพเดทเรียบร้อย")
        else:
            print("Error: หมายเลขเมนูไม่ถูกต้อง")
    except ValueError:
        print("Error: กรุณากรอกเป็นตัวเลขจำนวนเต็ม")

def delete_item(items):
    show_items(items)
    if not items:
        return

    print("\n--- ลบเมนู ---")
    try:
        idx = int(input("เลือกหมายเลขเมนูที่จะลบ: ")) - 1
        if 0 <= idx < len(items):
            removed = items.pop(idx)
            print(f">> ลบเมนู '{removed['name']}' เรียบร้อยแล้ว")
        else:
            print("Error: หมายเลขเมนูไม่ถูกต้อง")
    except ValueError:
        print("Error: กรุณากรอกเป็นตัวเลขจำนวนเต็ม")

def search_item(items):
    if not items:
        print("ยังไม่มีเมนูให้ค้นหา")
        return

    keyword = input("\nค้นหาชื่อเมนู (บางส่วน): ").strip().lower()
    found_items = [item for item in items if keyword in item['name'].lower()]

    if found_items:
        print(f"\n--- ผลการค้นหา '{keyword}' พบ {len(found_items)} รายการ ---")
        for item in found_items:
            print(f"- {item['name']} : {item['price']:.2f} บาท")
    else:
        print(">> ไม่พบเมนูที่ค้นหา")

def summary(items):
    if not items:
        print("ยังไม่มีข้อมูลสำหรับสรุปผล")
        return

    prices = [item['price'] for item in items]
    min_p = min(prices)
    max_p = max(prices)
    total = sum(prices)
    avg = total / len(prices)

    print("\n--- สรุปข้อมูลเมนู (Summary) ---")
    print(f"จำนวนเมนูทั้งหมด : {len(items)} รายการ")
    print(f"ราคาน้อยสุด (Min) : {min_p:.2f} บาท")
    print(f"ราคามากสุด (Max) : {max_p:.2f} บาท")
    print(f"ราคารวม (Total)   : {total:.2f} บาท")
    print(f"ราคาเฉลี่ย (Avg)  : {avg:.2f} บาท")

def count_price_gt_x(items):
    if not items:
        print("ยังไม่มีข้อมูล")
        return
    
    threshold = input_float("\nกรอกราคาขั้นต่ำ (X): ")
    count = 0
    print(f"\n--- รายการที่ราคามากกว่า {threshold} บาท ---")
    for item in items:
        if item['price'] > threshold:
            print(f"- {item['name']} ({item['price']:.2f})")
            count += 1
            
    if count == 0:
        print(">> ไม่พบรายการที่ราคาสูงกว่าที่กำหนด")
    else:
        print(f"\nสรุป: พบทั้งหมด {count} รายการ")

def sort_items(items):
    if not items:
        print("ยังไม่มีข้อมูลให้เรียงลำดับ")
        return

    direction = input("\nเลือกการเรียงลำดับ (A=น้อยไปมาก, D=มากไปน้อย): ").strip().upper()
    
    if direction == 'A':
        # เรียงจากน้อยไปมาก (Ascending)
        items.sort(key=lambda x: x["price"])
        print(">> เรียงลำดับจาก น้อย -> มาก เรียบร้อยแล้ว")
        show_items(items)
    elif direction == 'D':
        # เรียงจากมากไปน้อย (Descending)
        items.sort(key=lambda x: x["price"], reverse=True)
        print(">> เรียงลำดับจาก มาก -> น้อย เรียบร้อยแล้ว")
        show_items(items)
    else:
        print("Error: กรุณาเลือก A หรือ D เท่านั้น")

def seed_data(items):
    items.clear()
    items.extend([
        {"name": "Fried Rice", "price": 50.0},
        {"name": "Noodle Soup", "price": 45.0},
        {"name": "Pad Krapao", "price": 55.0},
        {"name": "Iced Tea", "price": 25.0},
        {"name": "Steak", "price": 129.0},
    ])

def main():
    items = []
    seed_data(items) # โหลดข้อมูลตัวอย่างเริ่มต้น
    
    while True:
        show_menu()
        choice = input("เลือกเมนู (0-8): ").strip()

        if choice == "1":
            add_item(items)
        elif choice == "2":
            show_items(items)
        elif choice == "3":
            update_item(items)
        elif choice == "4":
            delete_item(items)
        elif choice == "5":
            search_item(items)
        elif choice == "6":
            summary(items)
        elif choice == "7":
            count_price_gt_x(items)
        elif choice == "8":
            sort_items(items)
        elif choice == "0":
            print("Bye! ขอบคุณที่ใช้งาน")
            break
        else:
            print("เมนูไม่ถูกต้อง กรุณาเลือกใหม่")

if __name__ == "__main__":
    main()