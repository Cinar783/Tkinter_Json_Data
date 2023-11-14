import requests
import tkinter
import locale

locale.setlocale(locale.LC_NUMERIC,'tr_TR.UFT-8')


window=tkinter.Tk()
window.minsize(500,500)




input=tkinter.Entry()
input.pack()


label=tkinter.Label()
label.pack()





def get_responsive_json():
    reponsive=requests.get("https://cinar783.github.io/examplejson/mydata.json")
    if reponsive.status_code==200:
        return reponsive.json()

crypto_data=get_responsive_json()

def Button():
    for crypto in crypto_data:
        if crypto["Country"] == input.get():
            # print(f'The Capital of {user_input} is {crypto['Capital City']}, its surface area is {crypto['Area']} m2')
            label.config(text=f'The Capital of {input.get()} is {crypto['Capital City']}, its surface area is {locale.format_string("%f",crypto['Area'],grouping=True)} m2')


button = tkinter.Button(text='Button', command=Button,height=2,width=20)

button.pack()

label=tkinter.Label()
label.pack()

label=tkinter.Label()
label.pack()



#user_input=input("Please enter crypto name: ")




tkinter.mainloop()