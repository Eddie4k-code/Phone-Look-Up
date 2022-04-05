import json

import requests
import bs4
import tkinter as tk
from tkinter import *
import time

root = tk.Tk()
root.geometry('600x800')


def lookup():
    parameters = {
        'number': f'{num_entry.get()}',
        'country_code': f'{country_entry.get()}',
    }

    response = requests.get('http://apilayer.net/api/validate?access_key=KEY-GOES-HERE',
                            params=parameters)

    data = response.json()




    try:

        phone_num = data['location']

        line_type = data['line_type']

        info_label['text'] = f'Location: {phone_num}\n\nLine Type: {line_type}'

    except:
        info_label['text'] = 'Not valid phone number\nor Country Code'





    num_entry.delete(0, END)
    country_entry.delete(0, END)



root.resizable(False, False)
root.title('Phone Look up')

frame = tk.Frame(root, bg='yellow')
frame.place(width=600, height=800)

title = tk.LabelFrame(frame, bg='black')
title.place(relx=0.25, rely=0.100, width=300, height=50)

title_text = tk.Label(title, text='Phone Lookup', bg='black', font=(40), fg='white')
title_text.pack()

phone_num_label = tk.Label(frame, bg='yellow', text='Phone Number (Include Area Code)\n Example(1231231234)', font=('Helvetica 10 bold'), fg='black')
phone_num_label.place(rely=0.20, relx=0.30)

num_entry = tk.Entry(bg='white')
num_entry.place(relx=0.30, rely=0.26, width=230)

country_code_label = tk.Label(frame, bg='yellow', text='Country Code EX: US', font=('Helvetica 10 bold'), fg='black')
country_code_label.place(relx=0.30, rely=0.29, width=230)

country_entry = tk.Entry(bg='white')
country_entry.place(relx=0.30, rely=0.33, width=230)

lookup_btn = tk.Button(text='Lookup!', fg='white', bg='black', command=lambda :lookup())
lookup_btn.place(width=230, relx=0.30, rely=0.36)

info_frame = tk.LabelFrame(bg='black', width=400, height=350)
info_frame.place(relx=0.17, rely=0.50)

info_label = tk.Label(info_frame, bg='black', fg='white', font=('Helvetica 10 bold'))
info_label.place(relx=0.30, rely=0.30)




root.mainloop()

