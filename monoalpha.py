import tkinter as tk
from tkinter import scrolledtext
import itertools
import string

# دالة لفك تشفير Monoalphabetic باستخدام مفتاح معين
def decrypt_monoalphabetic(ciphertext, key_mapping):
    alphabet = string.ascii_lowercase
    decrypted_text = ""
    
    for char in ciphertext:
        if char.lower() in key_mapping:
            new_char = key_mapping[char.lower()]
            if char.isupper():
                new_char = new_char.upper()
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

# دالة تجربة جميع المفاتيح الممكنة بالقوة الغاشمة
def brute_force_attack():
    ciphertext = input_text.get("1.0", tk.END).strip().lower()
    alphabet = string.ascii_lowercase
    all_permutations = itertools.permutations(alphabet)
    
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    
    for perm in all_permutations:
        key_mapping = dict(zip(alphabet, perm))
        decrypted = decrypt_monoalphabetic(ciphertext, key_mapping)
        output_text.insert(tk.END, f"Key: {''.join(perm)}\nDecrypted: {decrypted}\n\n")
    
    output_text.config(state=tk.DISABLED)

# إعداد واجهة المستخدم باستخدام Tkinter
root = tk.Tk()
root.title("Monoalphabetic Brute Force Cipher")
root.geometry("600x400")

# إدخال النص المشفر
tk.Label(root, text="Enter Ciphertext:").pack()
input_text = scrolledtext.ScrolledText(root, height=3, width=60)
input_text.pack()

# زر تنفيذ الهجوم
attack_button = tk.Button(root, text="Brute Force Attack", command=brute_force_attack)
attack_button.pack()

# عرض النتائج
tk.Label(root, text="Possible Decryptions:").pack()
output_text = scrolledtext.ScrolledText(root, height=10, width=60)
output_text.pack()
output_text.config(state=tk.DISABLED)

# تشغيل الواجهة
root.mainloop()