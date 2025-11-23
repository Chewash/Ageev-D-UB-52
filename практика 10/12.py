import requests
import json
import tkinter as tk

def get_data():
    url = "https://api.github.com/users/rust-lang"
    response = requests.get(url)
    user_data = response.json()

    result = {
        'company': user_data['company'],
        'created_at': user_data['created_at'],
        'email': user_data['email'],
        'id': user_data['id'],
        'name': user_data['name'],
        'url': user_data['url']
    }

    with open("rust_info.json", "w") as f:
        json.dump(result, f, indent=2)

    result_label.config(text="Данные сохранены в файл rust_info.json")


window = tk.Tk()
window.title("GitHub Info")
window.geometry("400x200")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)
entry.insert(0, "rust-lang")

button = tk.Button(window, text="Получить данные", command=get_data)
button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
