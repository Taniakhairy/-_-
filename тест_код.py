from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json

def update_cripta_label(event):
    code = cripta_combobox.get()
    name = cripta_spr[code]
    currency_label.config(text=name)

def exchange():
    cripta_code = cripta_combobox.get()
    cur_code = cur_combobox.get()

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripta_code}&vs_currencies={cur_code}"
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)
    price = data[cripta_code.lower()][cur_code.lower()]
    print(price)
            #else:
                #print('Ошибка')
            #if cripta_code == data[0]: #data['rates']:
             #   exchange_rate = data[1] #'rates'][cripta_code]
              #  cur = currencies[cur_code]
               # cripta = cripta_spr[cripta_code]
    text_cur = price #data #f" {cur} - {exchange_rate:.2f} {cripta} "
#            return text_cur
    cur.config(text=f'Курс: {text_cur}')
            #else:
                #mb.showerror("Ошибка", f"Криптовалюта {cripta} не найдена")
    #    except Exception as e:
    #        mb.showerror("Ошибка", f"Ошибка: {e}")
    #else:
     #   mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "RUB": "Российский рубль"
}

cripta_spr = {
    "Bitcoin": "Биткоин",
    "Litecoin": "Лайткоин",
    "Ethereum": "Эфириум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("400x400")

Label(text="Валюта:").pack(padx=10, pady=5)
cur_combobox = ttk.Combobox(values=list(currencies.keys()))
cur_combobox.pack(padx=10, pady=5)

Label(text="Криптовалюта:").pack(padx=10, pady=5)
cripta_combobox = ttk.Combobox(values=list(cripta_spr.keys()))
cripta_combobox.pack(padx=10, pady=5)
cripta_combobox.bind("<<ComboboxSelected>>", update_cripta_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

cur = ttk.Label()
cur.pack(padx=10, pady=10)

window.mainloop()
