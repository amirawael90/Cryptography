import tkinter as tk
from tkinter import scrolledtext
import string
from collections import Counter

# تكرار الأحرف في اللغة الإنجليزية (نموذجي)
english_freq = "etaoinshrdlcumwfgypbvkjxqz"

# دالة لفك التشفير باستخدام مفتاح معين
def decrypt_monoalphabetic(ciphertext, key_mapping):
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

# دالة تحليل التردد ومحاولة تخمين المفتاح
def frequency_analysis_attack():
    ciphertext = input_text.get("1.0", tk.END).strip().lower()
    
    if not ciphertext:
        return
    
    # حساب تكرار الحروف في النص المشفر
    char_counts = Counter(ciphertext)
    sorted_chars = sorted(char_counts, key=char_counts.get, reverse=True)
    
    # توليد خريطة المفتاح المحتمل
    key_mapping = {}
    for i, char in enumerate(sorted_chars):
        if char in string.ascii_lowercase:
            key_mapping[char] = english_freq[i]
    
    # فك التشفير باستخدام المفتاح المستنتج
    decrypted = decrypt_monoalphabetic(ciphertext, key_mapping)
    
    # عرض النتيجة
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Estimated Key Mapping: {key_mapping}\n\nDecrypted Text:\n{decrypted}")
    output_text.config(state=tk.DISABLED)

# إعداد واجهة المستخدم
root = tk.Tk()
root.title("Monoalphabetic Cipher Breaker")
root.geometry("600x400")

tk.Label(root, text="Enter Ciphertext:").pack()
input_text = scrolledtext.ScrolledText(root, height=3, width=60)
input_text.pack()

attack_button = tk.Button(root, text="Frequency Analysis Attack", command=frequency_analysis_attack)
attack_button.pack()

tk.Label(root, text="Decryption Result:").pack()
output_text = scrolledtext.ScrolledText(root, height=10, width=60)
output_text.pack()
output_text.config(state=tk.DISABLED)

root.mainloop()