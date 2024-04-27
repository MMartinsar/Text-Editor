import tkinter as tk
import ttkbootstrap as ttk

def uppercase():
    new_text = textbox.get('1.0', 'end-1c')
    resulting_text.delete('1.0', 'end')
    resulting_text.insert('1.0', new_text.upper())

def lowercase():
    new_text = textbox.get('1.0', 'end-1c')
    resulting_text.delete('1.0', 'end')
    resulting_text.insert('1.0', new_text.lower())

def titlecase():
    new_text = textbox.get('1.0', 'end-1c')
    resulting_text.delete('1.0', 'end')
    resulting_text.insert('1.0', new_text.title())

def alternate():
    textbox_text = textbox.get('1.0', 'end-1c')
    resulting_text.delete('1.0', 'end')
    new_text = ''

    for i, char in enumerate(textbox_text):
        if i % 2 == 0:
            new_text += char.upper()
        else:
            new_text += char.lower()

    resulting_text.insert('1.0', new_text)

def punctuation():
    new_text = textbox.get('1.0', 'end-1c')

    if resulting_text.get('end-2c','end-1c') == '.':
        resulting_text.delete('end-2c','end-1c')
        resulting_text.insert('end', '.')
    elif resulting_text.get('1.0', 'end-1c') == '':
        resulting_text.insert('end', new_text + '.')
    else:
        resulting_text.insert('end-1c', '.')

def firstcapital():
    textbox_text = textbox.get('1.0', 'end-1c').split(". ")
    new_text = ""

    for word in textbox_text:
        if not word:
            continue
        
        new_text += word.capitalize() + '. '

    resulting_text.delete('1.0', 'end')
    resulting_text.insert('1.0', new_text.strip())       

# Window
window = ttk.Window()
window.title('TextEditor')
window.geometry('1366x768')

# Title Label
title_label = ttk.Label(master = window, text = 'Text Editor', font = ('Times New Roman', '24', 'bold', 'underline'))
title_label.pack(pady = 30)

# Text-Box
textbox = ttk.Text(master = window, height = 12)
textbox.pack(pady = 15)

# Editing Buttons
button_frame = ttk.Frame(master = window)
button_frame.pack(pady = 10)
uppercase_button = ttk.Button(master = button_frame, text = 'Uppercase', command = uppercase)
uppercase_button.pack(side = 'left', padx = 3)
lowercase_button = ttk.Button(master = button_frame, text = 'Lowercase', command = lowercase)
lowercase_button.pack(side = 'left', padx = 3)
titlecase_button = ttk.Button(master = button_frame, text = 'Title Case', command = titlecase)
titlecase_button.pack(side = 'left', padx = 3)
firstcapital_button = ttk.Button(master = button_frame, text = 'First Letter Capital', command = firstcapital)
firstcapital_button.pack(side = 'left', padx = 3)
alternate_button = ttk.Button(master = button_frame, text = 'AlTeRnAtE cAsE', command = alternate)
alternate_button.pack(side = 'left', padx = 3)
punctuation_button = ttk.Button(master = button_frame, text = 'Add Punctuation', command = punctuation)
punctuation_button.pack(side = 'left', padx = 3)

# Result Label
result_label = ttk.Label(master = window, text = 'Resulting Text:', font = ('Times New Roman', '16', 'bold'))
result_label.pack(pady = (50, 5))

# Result
resulting_text = ttk.Text(master = window, height = 12)
resulting_text.pack(pady = 15)

# Run
window.mainloop()