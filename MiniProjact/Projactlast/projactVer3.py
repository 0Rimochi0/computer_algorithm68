import customtkinter as ctk
import sqlite3

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Kishimo Task Manager")
        self.geometry("600x650")
        self.db_name = "tasks_data.db"
        self.init_db()

        # UI Header
        self.label = ctk.CTkLabel(self, text="รายการงานที่ต้องทำ", font=("Helvetica", 24, "bold"))
        self.label.pack(pady=20)

        # Input Frame
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="ชื่องานของคุณ...")
        self.task_entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        self.date_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="ว/ด/ป", width=100)
        self.date_entry.pack(side="left", padx=10, pady=10)

        self.add_button = ctk.CTkButton(self, text="เพิ่มบันทึก", command=self.add_task)
        self.add_button.pack(pady=10)

        # Task List Frame
        self.tasks_list_frame = ctk.CTkScrollableFrame(self, label_text="รายการบันทึก")
        self.tasks_list_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.load_tasks()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        # เพิ่มคอลัมน์ status (0 = ยังไม่ทำ, 1 = ทำแล้ว)
        c.execute('''CREATE TABLE IF NOT EXISTS tasks 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      task TEXT, 
                      date TEXT, 
                      status INTEGER DEFAULT 0)''')
        conn.commit()
        conn.close()

    def add_task(self):
        task = self.task_entry.get()
        date = self.date_entry.get()
        if task != "" and date != "":
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("INSERT INTO tasks (task, date, status) VALUES (?, ?, 0)", (task, date))
            conn.commit()
            conn.close()
            self.task_entry.delete(0, 'end')
            self.date_entry.delete(0, 'end')
            self.load_tasks()

    def load_tasks(self):
        for widget in self.tasks_list_frame.winfo_children():
            widget.destroy()

        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM tasks")
        rows = c.fetchall()
        conn.close()

        for row in rows:
            self.create_task_item(row[0], row[1], row[2], row[3])

    def create_task_item(self, task_id, task_text, date_text, status):
        item_frame = ctk.CTkFrame(self.tasks_list_frame, fg_color="transparent")
        item_frame.pack(pady=5, padx=10, fill="x")

        # กำหนดสีเริ่มต้น: ถ้า status เป็น 1 (เสร็จแล้ว) ให้เป็นสีเขียว ถ้า 0 ให้เป็นสีขาว/เทาปกติ
        current_color = "#2ECC71" if status == 1 else ["#DCE4EE", "#DCE4EE"] # สีเขียว emerald กับสีปกติ

        check_var = ctk.IntVar(value=status)
        
        # สร้าง Checkbox โดยส่งตัวแปร checkbox เข้าไปใน toggle_task ด้วย
        checkbox = ctk.CTkCheckBox(item_frame, text=f"📅 {date_text} | {task_text}", 
                                   variable=check_var,
                                   text_color=current_color, # ตั้งสีเริ่มต้น
                                   command=lambda: self.toggle_task(task_id, check_var.get(), checkbox))
        checkbox.pack(side="left", padx=10)
        
        if status == 1:
            checkbox.select()

        delete_btn = ctk.CTkButton(item_frame, text="ลบ", fg_color="#FF4B4B", width=60, height=25, 
                                   command=lambda: self.delete_task(task_id))
        delete_btn.pack(side="right", padx=10)

    def toggle_task(self, task_id, new_status, checkbox_widget):
        """อัปเดตสถานะใน DB และเปลี่ยนสีตัวอักษรทันที"""
        # เปลี่ยนสีตัวอักษร: 1 = เขียว, 0 = สีปกติ
        if new_status == 1:
            checkbox_widget.configure(text_color="#2ECC71") # สีเขียวสด
        else:
            checkbox_widget.configure(text_color=["#DCE4EE", "#DCE4EE"]) # กลับเป็นสีปกติ

        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
        conn.commit()
        conn.close()

    def delete_task(self, task_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        self.load_tasks()

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()