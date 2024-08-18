import tkinter as tk
from tkinter import messagebox
import random
import string

# Fungsi untuk membuat password unik berdasarkan username dan kriteria yang dipilih
def create_unique_password(username, use_upper, use_lower, use_digits, use_special):
    ascii_sum = sum(ord(char) for char in username)
    
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        characters = string.ascii_letters + string.digits

    random_chars = ''.join(random.choices(characters, k=8))
    unique_password = f"{ascii_sum}{random_chars}"
    return unique_password

# Fungsi untuk menghasilkan password ketika tombol diklik
def generate_password():
    username = entry_username.get()
    desired_password = entry_desired_password.get()
    
    if not username:
        messagebox.showerror("Error", "Username tidak boleh kosong!")
        return
    
    if desired_password:
        generated_password = desired_password
    else:
        use_upper = var_upper.get()
        use_lower = var_lower.get()
        use_digits = var_digits.get()
        use_special = var_special.get()
        
        generated_password = create_unique_password(username, use_upper, use_lower, use_digits, use_special)
    
    entry_password.delete(0, tk.END)
    entry_password.insert(0, generated_password)

# Membuat window utama
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x400")
root.configure(bg='#f0f0f0')

# Frame utama untuk padding
main_frame = tk.Frame(root, padx=20, pady=20, bg='#f0f0f0')
main_frame.pack(fill=tk.BOTH, expand=True)

# Styling
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Label dan Entry untuk Username
label_username = tk.Label(main_frame, text="Username:", font=label_font, bg='#f0f0f0')
label_username.pack(anchor='w', pady=5)

entry_username = tk.Entry(main_frame, font=entry_font)
entry_username.pack(fill=tk.X, pady=5)

# Label dan Entry untuk Kata Sandi yang Diinginkan
label_desired_password = tk.Label(main_frame, text="Desired Password (optional):", font=label_font, bg='#f0f0f0')
label_desired_password.pack(anchor='w', pady=5)

entry_desired_password = tk.Entry(main_frame, font=entry_font)
entry_desired_password.pack(fill=tk.X, pady=5)

# Frame untuk checkbox
checkbox_frame = tk.Frame(main_frame, bg='#f0f0f0')
checkbox_frame.pack(fill=tk.X, pady=10)

# Checkbox untuk memilih karakter yang digunakan
var_upper = tk.BooleanVar()
check_upper = tk.Checkbutton(checkbox_frame, text="Uppercase Letters", variable=var_upper, font=label_font, bg='#f0f0f0')
check_upper.pack(anchor='w')

var_lower = tk.BooleanVar()
check_lower = tk.Checkbutton(checkbox_frame, text="Lowercase Letters", variable=var_lower, font=label_font, bg='#f0f0f0')
check_lower.pack(anchor='w')

var_digits = tk.BooleanVar()
check_digits = tk.Checkbutton(checkbox_frame, text="Digits", variable=var_digits, font=label_font, bg='#f0f0f0')
check_digits.pack(anchor='w')

var_special = tk.BooleanVar()
check_special = tk.Checkbutton(checkbox_frame, text="Special Characters", variable=var_special, font=label_font, bg='#f0f0f0')
check_special.pack(anchor='w')

# Tombol untuk menghasilkan password
button_generate = tk.Button(main_frame, text="Generate Password", command=generate_password, font=button_font, bg='#4caf50', fg='white')
button_generate.pack(fill=tk.X, pady=20)

# Label dan Entry untuk menampilkan Password yang dihasilkan
label_password = tk.Label(main_frame, text="Generated Password:", font=label_font, bg='#f0f0f0')
label_password.pack(anchor='w', pady=5)

entry_password = tk.Entry(main_frame, font=entry_font)
entry_password.pack(fill=tk.X, pady=5)

# Menjalankan aplikasi
root.mainloop()