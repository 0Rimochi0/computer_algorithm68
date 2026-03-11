import customtkinter as ctk
import sqlite3
import os

# ตั้งค่าธีม
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Napintor Task Manager")
        self.geometry("600x650")

        # --- ส่วนจัดการฐานข้อมูล ---
        self.db_name = "tasks_data.db"
        self.init_db()

        # --- ส่วนของ UI ---
        self.label = ctk.CTkLabel(self, text="รายการงานที่ต้องทำ", font=("Helvetica", 24, "bold"))
        self.label.pack(pady=20)

        # ส่วนกรอกข้อมูล
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="ชื่องานของคุณ...")
        self.task_entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        self.date_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="ว/ด/ป", width=100)
        self.date_entry.pack(side="left", padx=10, pady=10)

        self.add_button = ctk.CTkButton(self, text="เพิ่มบันทึก", command=self.add_task)
        self.add_button.pack(pady=10)

        # ส่วนแสดงผลรายการ
        self.tasks_list_frame = ctk.CTkScrollableFrame(self, label_text="รายการที่บันทึกไว้ถาวร")
        self.tasks_list_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # โหลดข้อมูลเก่าจากฐานข้อมูลขึ้นมาแสดง
        self.load_tasks()

    def init_db(self):
        """สร้างตารางข้อมูลถ้ายังไม่มี"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, date TEXT)''')
        conn.commit()
        conn.close()

    def add_task(self):
        task = self.task_entry.get()
        date = self.date_entry.get()
        
        if task != "" and date != "":
            # บันทึกลง SQLite
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("INSERT INTO tasks (task, date) VALUES (?, ?)", (task, date))
            conn.commit()
            conn.close()
            
            # ล้างช่องกรอกและโหลดรายการใหม่
            self.task_entry.delete(0, 'end')
            self.date_entry.delete(0, 'end')
            self.load_tasks()

    def load_tasks(self):
        """ล้างหน้าจอแล้วดึงข้อมูลจาก DB มาแสดงใหม่ทั้งหมด"""
        # ลบ widget เก่าออกก่อน
        for widget in self.tasks_list_frame.winfo_children():
            widget.destroy()

        # ดึงข้อมูลจาก DB
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM tasks")
        rows = c.fetchall()
        conn.close()

        for row in rows:
            self.create_task_item(row[0], row[1], row[2])

    def create_task_item(self, task_id, task_text, date_text):
        """สร้างแถวงานที่มีทั้งข้อความและปุ่มลบ"""
        item_frame = ctk.CTkFrame(self.tasks_list_frame, fg_color="transparent")
        item_frame.pack(pady=5, padx=10, fill="x")

        label_text = f"📅 {date_text} | {task_text}"
        task_label = ctk.CTkLabel(item_frame, text=label_text, font=("Helvetica", 14))
        task_label.pack(side="left", padx=10)

        delete_btn = ctk.CTkButton(item_frame, text="ลบ", fg_color="#FF4B4B", hover_color="#D22B2B", 
                                   width=60, height=25, command=lambda: self.delete_task(task_id))
        delete_btn.pack(side="right", padx=10)

    def delete_task(self, task_id):
        """ลบข้อมูลออกจาก DB และรีโหลดหน้าจอ"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        self.load_tasks()

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()