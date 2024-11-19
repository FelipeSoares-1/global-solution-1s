import tkinter as tk
from tkinter import ttk
import random
import time
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EnergySmartOptimizer:
    def __init__(self, root):
        self.root = root
        self.root.title("EnergySmartOptimizer")
        self.root.geometry("800x600")

        # Dados simulados de tarifas e consumo
        self.tarifas = {"Rede Elétrica": 0.45, "Solar": 0.25, "Eólica": 0.30}
        self.consumo_atual = random.uniform(1, 5)  # Consumo inicial em kWh

        # Interface gráfica
        self.setup_ui()

        # Atualização em tempo real
        self.update_consumption()

    def setup_ui(self):
        # Título
        title = tk.Label(
            self.root, text="EnergySmartOptimizer", font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # Frame para gráficos
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)

        # Botão para gerar relatório
        report_btn = tk.Button(
            self.root, text="Gerar Relatório", command=self.generate_report
        )
        report_btn.pack(pady=10)

        # Fonte econômica recomendada
        self.recommendation_label = tk.Label(
            self.root, text="", font=("Arial", 14, "italic")
        )
        self.recommendation_label.pack(pady=5)

    def calculate_optimal_source(self):
        """Calcula a fonte de energia mais econômica."""
        custos = {k: self.consumo_atual * v for k, v in self.tarifas.items()}
        fonte_ideal = min(custos, key=custos.get)
        return fonte_ideal, custos[fonte_ideal]

    def update_consumption(self):
        """Atualiza o consumo em tempo real e exibe a recomendação."""
        self.consumo_atual = random.uniform(1, 5)  # Simula consumo entre 1 e 5 kWh
        fonte, custo = self.calculate_optimal_source()
        self.recommendation_label.config(
            text=f"Fonte mais econômica: {fonte} (Custo estimado: R$ {custo:.2f})"
        )
        self.plot_consumption()
        self.root.after(5000, self.update_consumption)

    def plot_consumption(self):
        """Plota os dados simulados de consumo energético."""
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_title("Consumo Energético em Tempo Real")
        ax.set_ylabel("Consumo (kWh)")
        ax.set_xlabel("Tempo (segundos)")

        # Dados simulados
        timestamps = [time.time() - i for i in range(10, 0, -1)]
        consumptions = [random.uniform(1, 5) for _ in range(10)]

        ax.plot(timestamps, consumptions, label="Consumo (kWh)", marker="o")
        ax.legend()

        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def generate_report(self):
        """Gera um relatório de consumo e salva em CSV."""
        data = {
            "Fonte": list(self.tarifas.keys()),
            "Tarifa (R$/kWh)": list(self.tarifas.values()),
            "Consumo Atual (kWh)": [self.consumo_atual] * len(self.tarifas),
            "Custo Estimado (R$)": [
                self.consumo_atual * v for v in self.tarifas.values()
            ],
        }
        df = pd.DataFrame(data)
        df.to_csv("relatorio_consumo.csv", index=False)
        tk.messagebox.showinfo(
            "Relatório Gerado", "Relatório de consumo salvo como 'relatorio_consumo.csv'."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = EnergySmartOptimizer(root)
    root.mainloop()
