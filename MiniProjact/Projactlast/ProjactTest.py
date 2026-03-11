import customtkinter as ctk

# ตั้งค่าธีมและสี
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Napintor Task Manager")
        self.geometry("500x600")

        # --- ส่วนของ Header ---
        self.label = ctk.CTkLabel(self, text="รายการงานที่ต้องทำ", font=("Helvetica", 24, "bold"))
        self.label.pack(pady=20)

        # --- ส่วนกรอกข้อมูล ---
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="ชื่องานของคุณ...")
        self.task_entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

        self.date_entry = ctk.CTkEntry(self.entry_frame, placeholder_text="ว/ด/ป", width=100)
        self.date_entry.pack(side="left", padx=10, pady=10)

        self.add_button = ctk.CTkButton(self, text="เพิ่มบันทึก", command=self.add_task)
        self.add_button.pack(pady=10)

        # --- ส่วนแสดงผลรายการ (Scrollable Frame) ---
        self.tasks_list = ctk.CTkScrollableFrame(self, label_text="รายการที่บันทึกไว้")
        self.tasks_list.pack(pady=20, padx=20, fill="both", expand=True)

    def add_task(self):
        task = self.task_entry.get()
        date = self.date_entry.get()
        
        if task != "" and date != "":
            # สร้างแถวใหม่สำหรับงาน
            task_text = f"📅 {date} | {task}"
            new_task = ctk.CTkCheckBox(self.tasks_list, text=task_text)
            new_task.pack(pady=5, padx=10, anchor="w")
            
            # ล้างช่องกรอกหลังจากเพิ่มเสร็จ
            self.task_entry.delete(0, 'end')
            self.date_entry.delete(0, 'end')

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()