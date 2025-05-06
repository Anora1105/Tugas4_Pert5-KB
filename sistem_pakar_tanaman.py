import tkinter as tk
from tkinter import messagebox

# Data pengetahuan (aturan berbasis forward chaining)
rules = {
    "Daun menguning dan tanah selalu basah": "Overwatering (terlalu banyak air)",
    "Daun kering dan tanah sangat kering": "Underwatering (kekurangan air)",
    "Tanaman terlihat tinggi tapi lemah": "Kurang cahaya matahari",
    "Terdapat serangga di daun atau batang": "Serangan hama",
    "Pertumbuhan lambat dan daun pucat": "Kekurangan nutrisi",
}

# Saran penanganan
solutions = {
    "Overwatering (terlalu banyak air)": "Kurangi frekuensi penyiraman dan pastikan pot memiliki drainase baik.",
    "Underwatering (kekurangan air)": "Tingkatkan penyiraman secara bertahap.",
    "Kurang cahaya matahari": "Pindahkan tanaman ke area dengan sinar matahari cukup.",
    "Serangan hama": "Gunakan insektisida alami dan bersihkan daun secara rutin.",
    "Kekurangan nutrisi": "Berikan pupuk sesuai jenis tanaman secara berkala.",
}

# Fungsi untuk diagnosa
def diagnose():
    selected = []
    for var, text in zip(variables, rules.keys()):
        if var.get():
            selected.append(text)

    if not selected:
        messagebox.showwarning("Peringatan", "Silakan pilih minimal satu gejala.")
        return

    for symptom in selected:
        diagnosis = rules.get(symptom)
        if diagnosis:
            solution = solutions[diagnosis]
            messagebox.showinfo("Hasil Diagnosa", f"Penyebab: {diagnosis}\n\nSaran: {solution}")
            return

    messagebox.showinfo("Hasil Diagnosa", "Penyebab tidak terdeteksi secara spesifik. Silakan konsultasi lebih lanjut.")

# GUI
root = tk.Tk()
root.title("Sistem Pakar Tanaman Hias Layu")
root.geometry("500x400")

label = tk.Label(root, text="Pilih Gejala yang Terjadi:", font=("Arial", 14))
label.pack(pady=10)

variables = []
for symptom in rules:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=symptom, variable=var, font=("Arial", 12))
    chk.pack(anchor="w", padx=20)
    variables.append(var)

btn = tk.Button(root, text="Diagnosa", command=diagnose, bg="green", fg="white", font=("Arial", 12))
btn.pack(pady=20)

root.mainloop()
