import tkinter as tk
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 700

def formattedWeather(w):
    try:
        place = w['name']
        weather = w['weather'][0]['description']
        temp = w['main']['temp']

        output = "City: {}\nConditions: {}\nTemperature: {}c".format(place, weather, temp)

    except:
        output = "Error: cannot find location!\n\nPlease try entering its fullname."

    return output    

def getWeather(city):
    #add your own openweathermap API key below
    key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {'appid': key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=param)
    currentWeather = response.json()

    label['text'] = formattedWeather(currentWeather)
    


#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}


root = tk.Tk()
root.title("Alex's Weather App")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bgI = tk.PhotoImage(file='bg.png')
bgL = tk.Label(root, image=bgI)
bgL.place(x=0, y=0)

frame = tk.Frame(root, bd=5, bg="#b3e0ff")
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, font=('Arial', 20), text="Check", command=lambda:getWeather(entry.get()))
button.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

entry = tk.Entry(frame, font=('Arial', 20))
entry.place(relx=0, rely=0, relwidth=0.7, relheight=1)

frame2 = tk.Frame(root, bd=5, bg="#b3e0ff")
frame2.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(frame2, bg="white", font=('Arial', 20))
label.place(relwidth=1, relheight=1)

root.mainloop()
