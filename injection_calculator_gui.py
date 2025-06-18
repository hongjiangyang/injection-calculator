import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # 获取输入值
        weight = float(entry_weight.get())
        dose = float(entry_dose.get())
        concentration = float(entry_concentration.get())
        syringe_volume = float(entry_syringe_volume.get())
        syringe_grids = int(entry_syringe_grids.get())

        # 输入校验
        if weight <= 0 or dose <= 0 or concentration <= 0 or syringe_volume <= 0 or syringe_grids <= 0:
            raise ValueError("All inputs must be positive numbers.")
        
        # 计算注射体积 (ml)
        injection_volume = (weight * dose) / (1000 * concentration)

        # 每格体积
        grid_volume = syringe_volume / syringe_grids

        # 总格数
        grid_number = injection_volume / grid_volume
        grid_number_rounded = round(grid_number)

        # 显示结果
        label_result_volume.config(text=f"Injection Volume: {injection_volume:.4f} ml")
        label_result_grids.config(text=f"Grid Number: {grid_number:.2f} (suggest {grid_number_rounded} grids)")

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# 创建主窗口
root = tk.Tk()
root.title("Injection Calculator")
root.geometry("600x400")
root.configure(bg="#E6E6E6")

# 输入框区域
frame_input = tk.LabelFrame(root, text="Input Parameters", fg="blue", font=("Arial", 12))
frame_input.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.5)

tk.Label(frame_input, text="Weight (g):").grid(row=0, column=0, sticky='e')
entry_weight = tk.Entry(frame_input)
entry_weight.insert(0, "27")
entry_weight.grid(row=0, column=1)

tk.Label(frame_input, text="Dose (mg/kg):").grid(row=1, column=0, sticky='e')
entry_dose = tk.Entry(frame_input)
entry_dose.insert(0, "100")
entry_dose.grid(row=1, column=1)

tk.Label(frame_input, text="Concentration (mg/ml):").grid(row=2, column=0, sticky='e')
entry_concentration = tk.Entry(frame_input)
entry_concentration.insert(0, "10")
entry_concentration.grid(row=2, column=1)

tk.Label(frame_input, text="Syringe Volume (ml):").grid(row=3, column=0, sticky='e')
entry_syringe_volume = tk.Entry(frame_input)
entry_syringe_volume.insert(0, "1")
entry_syringe_volume.grid(row=3, column=1)

tk.Label(frame_input, text="Syringe Grids:").grid(row=4, column=0, sticky='e')
entry_syringe_grids = tk.Entry(frame_input)
entry_syringe_grids.insert(0, "40")
entry_syringe_grids.grid(row=4, column=1)

# 结果区域
frame_result = tk.LabelFrame(root, text="Results", fg="blue", font=("Arial", 12))
frame_result.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.25)

label_result_volume = tk.Label(frame_result, text="Injection Volume: ", anchor='w')
label_result_volume.pack(fill='x', padx=10, pady=5)

label_result_grids = tk.Label(frame_result, text="Grid Number: ", anchor='w')
label_result_grids.pack(fill='x', padx=10, pady=5)

# 计算按钮
btn_calculate = tk.Button(root, text="Calculate", font=("Arial", 12), bg="lightblue", command=calculate)
btn_calculate.place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.1)

root.mainloop()
