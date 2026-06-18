import tkinter as tk
from tkinter import ttk, messagebox

class AWSEstimator:
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Re/Start - EC2 Cost Estimator")
        self.root.geometry("500x600")
        self.root.configure(bg="#232f3e") # Color corporativo AWS (Squid Ink)

        # Base de datos simulada de instancias (Tipo: [Precio_Hora, vCPU, RAM_GB])
        self.instancias = {
            "t3.nano": [0.0052, 2, 0.5],
            "t3.micro": [0.0104, 2, 1],
            "t3.small": [0.0208, 2, 2],
            "t3.medium": [0.0416, 2, 4],
            "m5.large": [0.096, 2, 8],
            "m5.xlarge": [0.192, 4, 16],
            "c5.xlarge": [0.170, 4, 8],
            "p3.2xlarge": [3.06, 8, 61]
        }

        self.setup_ui()

    def setup_ui(self):
        # Estilo para los widgets
        style = ttk.Style()
        style.theme_use('clam')
        
        # Header con el logo/texto
        header = tk.Label(
            self.root, text="AWS EC2 Estimator", font=("Arial", 20, "bold"),
            bg="#ff9900", fg="white", pady=20
        )
        header.pack(fill="x")

        # Contenedor principal
        main_frame = tk.Frame(self.root, bg="#232f3e", padx=30, pady=20)
        main_frame.pack(fill="both", expand=True)

        # Selección de Instancia
        tk.Label(main_frame, text="Seleccione Tipo de Instancia:", bg="#232f3e", fg="white", font=("Arial", 11)).pack(anchor="w")
        self.combo_instancia = ttk.Combobox(main_frame, values=list(self.instancias.keys()), state="readonly", font=("Arial", 12))
        self.combo_instancia.pack(fill="x", pady=(5, 20))
        self.combo_instancia.current(0)

        # Entrada de Horas
        tk.Label(main_frame, text="Horas de uso al mes (Máx 730):", bg="#232f3e", fg="white", font=("Arial", 11)).pack(anchor="w")
        self.horas_entry = tk.Entry(main_frame, font=("Arial", 12))
        self.horas_entry.insert(0, "730") # Valor por defecto (24/7)
        self.horas_entry.pack(fill="x", pady=(5, 20))

        # Botón Calcular
        btn_calc = tk.Button(
            main_frame, text="CALCULAR ESTIMACIÓN", bg="#ff9900", fg="black",
            font=("Arial", 12, "bold"), relief="flat", command=self.calcular,
            cursor="hand2", pady=10
        )
        btn_calc.pack(fill="x", pady=10)

        # Área de Resultados
        self.res_frame = tk.LabelFrame(main_frame, text=" Detalles de la Estimación ", bg="#232f3e", fg="#ff9900", font=("Arial", 10, "bold"), padx=10, pady=10)
        self.res_frame.pack(fill="both", expand=True, pady=20)

        self.lbl_specs = tk.Label(self.res_frame, text="vCPU: -\nRAM: -", bg="#232f3e", fg="white", justify="left", font=("Arial", 11))
        self.lbl_specs.pack(anchor="w")

        self.lbl_precio = tk.Label(self.res_frame, text="Costo Mensual: $0.00", bg="#232f3e", fg="#34c759", font=("Arial", 16, "bold"))
        self.lbl_precio.pack(pady=10)

    def calcular(self):
        try:
            tipo = self.combo_instancia.get()
            horas = float(self.horas_entry.get())

            if horas < 0 or horas > 744:
                raise ValueError

            datos = self.instancias[tipo]
            precio_hora = datos[0]
            vcpus = datos[1]
            ram = datos[2]

            total = precio_hora * horas

            # Actualizar Interfaz
            self.lbl_specs.config(text=f"Especificaciones Técnicas:\n• vCPUs: {vcpus}\n• Memoria RAM: {ram} GB\n• Precio/Hora: ${precio_hora}")
            self.lbl_precio.config(text=f"Costo Mensual: ${total:.2f} USD")

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número de horas válido (0-744).")

if __name__ == "__main__":
    root = tk.Tk()
    app = AWSEstimator(root)
    root.mainloop()