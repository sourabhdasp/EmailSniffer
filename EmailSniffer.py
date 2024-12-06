import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import pyperclip

def find_gmails(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        text_content = soup.get_text()

        gmail_pattern = r'[a-zA-Z0-9._%+-]+@gmail\.com'

        gmails = re.findall(gmail_pattern, text_content)

        if gmails:
            return set(gmails)
        else:
            return "No Gmail addresses found."

    except requests.exceptions.RequestException as e:
        return f"Error fetching the webpage: {e}"

def on_submit():
    url = entry_url.get()
    if url:
        result = find_gmails(url)
        if isinstance(result, set):
            result_text.set('\n'.join(result))
        else:
            result_text.set(result)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")

def copy_to_clipboard():
    result = result_text.get()
    if result:
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Gmail addresses copied to clipboard.")
    else:
        messagebox.showwarning("No Data", "No Gmail addresses to copy.")

def paste_from_clipboard():
    """Paste the contents of the clipboard into the entry URL field."""
    clipboard_content = pyperclip.paste()
    entry_url.delete(0, tk.END)  # Clear the current content
    entry_url.insert(0, clipboard_content)  # Insert the clipboard content

root = tk.Tk()
root.title("Gmail Finder")
root.geometry("500x450")
root.config(bg="#2E2E2E")

heading_font = font.Font(family="Helvetica", size=14, weight="bold")
normal_font = font.Font(family="Helvetica", size=12)

label_url = tk.Label(root, text="Enter Website URL:", font=heading_font, bg="#2E2E2E", fg="#FFFFFF", anchor="w")
label_url.pack(pady=15, padx=20, fill="x")

entry_url = tk.Entry(root, width=50, font=normal_font, bd=2, relief="solid", highlightbackground="#ddd", bg="#424242", fg="#FFFFFF")
entry_url.pack(pady=10, padx=20)
entry_url.focus_set()

# Easy Paste Button
button_paste = tk.Button(root, text="Paste URL", font=normal_font, bg="#FF5722", fg="white", bd=0,
                         relief="flat", activebackground="#F4511E", command=paste_from_clipboard)
button_paste.pack(pady=5)

button_submit = tk.Button(root, text="Find Gmail Addresses", font=normal_font, bg="#6200EE", fg="white", bd=0,
                          relief="flat", activebackground="#3700B3", command=on_submit)
button_submit.pack(pady=20)

label_result = tk.Label(root, text="Gmail Addresses Found:", font=heading_font, bg="#2E2E2E", fg="#FFFFFF", anchor="w")
label_result.pack(pady=5, padx=20, fill="x")

result_text = tk.StringVar()
label_result_display = tk.Label(root, textvariable=result_text, font=normal_font, anchor="w", justify="left",
                                width=50, height=8, relief="solid", bd=2, bg="#424242", fg="#FFFFFF", wraplength=400)
label_result_display.pack(pady=10, padx=20)

button_copy = tk.Button(root, text="Copy to Clipboard", font=normal_font, bg="#03A9F4", fg="white", bd=0,
                        relief="flat", activebackground="#0288D1", command=copy_to_clipboard)
button_copy.pack(pady=10)

root.mainloop()
