import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Re/Start - To-Do List")
        self.root.geometry("450x550")
        self.root.configure(bg="#f4f7f6")

        # Fuentes y Estilos
        self.font_task = ("Segoe UI", 12)
        self.bg_color = "#f4f7f6"
        self.accent_color = "#2980b9"

        # --- Interfaz de Entrada ---
        self.setup_ui()

    def setup_ui(self):
        # Título
        tk.Label(
            self.root, text="Mis Tareas", font=("Segoe UI", 18, "bold"),
            bg=self.bg_color, fg="#2c3e50", pady=20
        ).pack()

        # Marco para entrada
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = tk.Entry(
            input_frame, font=self.font_task, relief="flat", borderwidth=5
        )
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.task_entry.bind("<Return>", lambda e: self.add_task()) # Enter para agregar

        add_btn = tk.Button(
            input_frame, text="Agregar", bg="#27ae60", fg="white",
            relief="flat", font=("Segoe UI", 10, "bold"), command=self.add_task,
            padx=15
        )
        add_btn.pack(side="right")

        # --- Lista de Tareas (Listbox) ---
        list_frame = tk.Frame(self.root, bg=self.bg_color)
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.tasks_listbox = tk.Listbox(
            list_frame, font=self.font_task, relief="flat", borderwidth=5,
            selectbackground="#d35400", yscrollcommand=self.scrollbar.set
        )
        self.tasks_listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.tasks_listbox.yview)

        # --- Botones de Acción ---
        action_frame = tk.Frame(self.root, bg=self.bg_color)
        action_frame.pack(pady=20)

        buttons = [
            ("Completar", self.mark_task, "#2980b9"),
            ("Editar", self.edit_task, "#f39c12"),
            ("Eliminar", self.delete_task, "#c0392b")
        ]

        for text, cmd, color in buttons:
            btn = tk.Button(
                action_frame, text=text, bg=color, fg="white",
                relief="flat", font=("Segoe UI", 10, "bold"),
                command=cmd, width=10, pady=5
            )
            btn.pack(side="left", padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks_listbox.insert(tk.END, f"[ ] {task}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "Escribe una tarea primero.")

    def mark_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)
            
            if task.startswith("[ ]"):
                new_task = task.replace("[ ]", "[✔]", 1)
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, new_task)
                self.tasks_listbox.itemconfig(index, fg="#95a5a6") # Gris para completado
            else:
                new_task = task.replace("[✔]", "[ ]", 1)
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, new_task)
                self.tasks_listbox.itemconfig(index, fg="black")
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para marcar.")

    def edit_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            old_task = self.tasks_listbox.get(index)
            
            # Limpiar el prefijo para editar solo el texto
            clean_text = old_task.replace("[ ] ", "").replace("[✔] ", "")
            
            new_text = simpledialog.askstring("Editar Tarea", "Modifica la tarea:", initialvalue=clean_text)
            
            if new_text:
                prefix = "[ ]" if "[ ]" in old_task else "[✔]"
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"{prefix} {new_text}")
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para editar.")

    def delete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            if messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar esta tarea?"):
                self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()