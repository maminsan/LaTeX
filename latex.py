import tkinter as tk
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import io
from tkinter import filedialog

def convert_latex_to_image(latex_code):
    fig = plt.figure(figsize=(3, 1))
    plt.text(0.5, 0.5, f'${latex_code}$', fontsize=12, ha='center', va='center')
    plt.axis('off')
    plt.tight_layout()

    # Сохраняем изображение во временный буфер
    buf = io.BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buf)
    buf.seek(0)

    return buf

def show_image(latex_code):
    global img_data
    img_data = convert_latex_to_image(latex_code)
    img = tk.PhotoImage(data=img_data.getvalue())
    label = tk.Label(window, image=img)
    label.image = img
    label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def on_submit():
    latex_code = entry_latex.get()
    show_image(latex_code)

def save_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    if filename:
        with open(filename, "wb") as f:
            f.write(img_data.getvalue())

window = tk.Tk()
window.title("LaTeX to Image Converter")

label_instruction = tk.Label(window, text="Enter LaTeX code:")
label_instruction.grid(row=0, column=0, padx=10, pady=5)

entry_latex = tk.Entry(window, width=30)
entry_latex.grid(row=0, column=1, padx=10, pady=5)

button_submit = tk.Button(window, text="Convert", command=on_submit)
button_submit.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

button_save = tk.Button(window, text="Save", command=save_image)
button_save.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

window.mainloop()
