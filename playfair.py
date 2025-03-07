import re
import tkinter as tk
from tkinter import messagebox

def prepare_text(text):
    text = re.sub(r'[^A-Za-z]', '', text).upper().replace('J', 'I')
    prepared_text = ""
    
    i = 0
    while i < len(text):
        if i == len(text) - 1:  
            prepared_text += text[i] + 'X'
            i += 1
        elif text[i] == text[i + 1]:  
            prepared_text += text[i] + 'X'
            i += 1
        else:  
            prepared_text += text[i] + text[i + 1]
            i += 2
    
    return prepared_text

def create_playfair_matrix(keyword):
    keyword = re.sub(r'[^A-Za-z]', '', keyword).upper().replace('J', 'I')
    matrix = []
    used_chars = set()
    
    for char in keyword:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def encrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)
    
    if row1 == row2:  
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)
    
    if row1 == row2:  
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt(text, matrix):
    text = prepare_text(text)
    ciphertext = ""
    
    for i in range(0, len(text), 2):
        ciphertext += encrypt_pair(matrix, text[i], text[i + 1])
    
    return ciphertext

def decrypt(text, matrix):
    plaintext = ""
    
    for i in range(0, len(text), 2):
        plaintext += decrypt_pair(matrix, text[i], text[i + 1])
    
    return plaintext

def display_matrix(matrix):
    return "\n".join([" ".join(row) for row in matrix])

def encrypt_message():
    keyword = keyword_entry.get()
    plaintext = text_entry.get()

    if not keyword or not plaintext:
        messagebox.showerror("error", "please enter both the keyword and text.")
        return
    
    matrix = create_playfair_matrix(keyword)
    ciphertext = encrypt(plaintext, matrix)
    matrix_display.config(text=display_matrix(matrix))
    result_label.config(text=f"encrypted text: {ciphertext}")

def decrypt_message():
    keyword = keyword_entry.get()
    ciphertext = text_entry.get()

    if not keyword or not ciphertext:
        messagebox.showerror("error", "please enter both the keyword and text.")
        return
    
    matrix = create_playfair_matrix(keyword)
    plaintext = decrypt(ciphertext, matrix)
    matrix_display.config(text=display_matrix(matrix))
    result_label.config(text=f"decrypted text: {plaintext}")

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("Playfair Cipher - GUI")
root.geometry("400x400")

# واجهة المستخدم
tk.Label(root, text="keyword:", font=("Arial", 12)).pack(pady=5)
keyword_entry = tk.Entry(root, font=("Arial", 12))
keyword_entry.pack(pady=5)

tk.Label(root, text="cipher text:", font=("Arial", 12)).pack(pady=5)
text_entry = tk.Entry(root, font=("Arial", 12))
text_entry.pack(pady=5)

tk.Button(root, text = "encrypt", font=("Arial", 12), command=encrypt_message).pack(pady=5)
tk.Button(root, text=" decrypt", font=("Arial", 12), command=decrypt_message).pack(pady=5)

matrix_display = tk.Label(root, text="", font=("Courier", 12), justify="left")
matrix_display.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

# تشغيل النافذة
root.mainloop()