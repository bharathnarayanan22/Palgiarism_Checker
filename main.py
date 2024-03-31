import tkinter as tk
from tkinter import messagebox
from difflib import SequenceMatcher
import os
def perform_file_comparison():
    filepath = entry.get()
    if not os.path.isfile(filepath):
        messagebox.showerror("Error", "Invalid file path")
        return

    with open(filepath) as f:
        content = f.read()

    directory = r'C:\Users\P A BHARATHNARAYANAN\PycharmProjects\pythonProject\files'
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath) as f:
                comparison_content = f.read()

            similarity = calculate_similarity(content, comparison_content)
            display_similarity(filename, similarity)

    entry.delete(0, tk.END)

def calculate_similarity(text1, text2):
    cleaned_text1 = text1.casefold().replace(" ", "").replace(",", "").replace(".","")
    cleaned_text2 = text2.casefold().replace(" ", "").replace(",", "").replace(".","")
    match = SequenceMatcher(None, cleaned_text1, cleaned_text2).ratio()
    similarity = match * 100
    return similarity


def display_similarity(filename, similarity):
    messagebox.showinfo("Match Percentage", f"Similarity with {filename}: {similarity:.2f}%")

main = tk.Tk()
main.title("File Comparison")

window_width = 500
window_height = 300
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
main.geometry(f"{window_width}x{window_height}+{x}+{y}")

canvas = tk.Canvas(main, width=window_width, height=window_height)
canvas.pack()

background_image = tk.PhotoImage(file=r"C:\Users\P A BHARATHNARAYANAN\Downloads\image.png.png")
background_label = tk.Label(main, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(main, text='Enter File Path:', font=("Arial", 16), bg="white")
label.place(relx=0.5, rely=0.3, anchor="center")

entry = tk.Entry(main, width=50, font=("Arial", 12))
entry.place(relx=0.5, rely=0.4, anchor="center")

button = tk.Button(main, text='Compare Files', font=("Arial", 12), command=perform_file_comparison)
button.place(relx=0.5, rely=0.5, anchor="center")

main.mainloop()
