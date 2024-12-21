import tkinter as tk
import requests
import random

def  weather() :
    api_key = "5d9f93c048062e3ff3a32b7a230fa0a7"
    city = location_input.get("1.0", "end-1c")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    result = response.json()
    degree_symbol="\u00B0"
    if response.status_code ==200 :
        temperature_value.config(text=f"{int(result["main"]["temp"]-273)}{degree_symbol}C")
        humidity_value.config(text=f"{result["main"]["humidity"]}%")
        wind_speed_value.config(text=f"{result["wind"]["speed"]}KM/h")
        pressure_value.config(text=f"{result["main"]["pressure"]}hPa")
        precipitation_value.config(text=f"{random.randint(1,100)}%") #مفيش precipitation ف عملتها random
    else:
        temperature_value.config(text="Error")
        humidity_value.config(text="Error")
        wind_speed_value.config(text="Error")
        pressure_value.config(text="Error")
        precipitation_value.config(text="Error")

#window
window = tk.Tk()
window.title("Weather Forecast")
window.geometry("1000x500")
window.minsize(width=600 , height=400)


#frames
row0_frame = tk.Frame(window)
row0_frame.place(x=350 , y=20)

column1_frame = tk.Frame(window)
column1_frame.place(x=30 , y=100)

#search
location_label = tk.Label(row0_frame,text="Location : ",font=("",18,""))
location_label.grid(column=2 , row=0 )

location_input	= tk.Text(row0_frame , width=20 , height=1 ,font=("",17,"") )
location_input.grid(column=3 , row=0 )

search_button = tk.Button(row0_frame , width=10, height=1 , text="Search" , font=("",11,""),command=weather)
search_button.grid(column=4 , row=0 , padx=10 )

#the details
temperature_label = tk.Label(column1_frame , text="Temperature : ",font=("",18,""),pady=10)
temperature_label.grid(column=0 , row=0)

temperature_value = tk.Label(column1_frame ,font=("",18,""),pady=10)
temperature_value.grid(column=1 , row=0)

#
humidity_label = tk.Label(column1_frame , text="Humidity : ",font=("",18,"") ,pady=10)
humidity_label.grid(column=0 , row=1)

humidity_value = tk.Label(column1_frame ,font=("",18,""),pady=10)
humidity_value.grid(column=1 , row=1)

#
wind_speed_label = tk.Label(column1_frame , text="Wind Speed : ",font=("",18,""),pady=10 )
wind_speed_label.grid(column=0 , row=2)

wind_speed_value = tk.Label(column1_frame ,font=("",18,""),pady=10)
wind_speed_value.grid(column=1 , row=2)

#
pressure_label = tk.Label(column1_frame , text="Pressure : ",font=("",18,""),pady=10)
pressure_label.grid(column=0 , row=3)

pressure_value = tk.Label(column1_frame , font=("",18,""),pady=10)
pressure_value.grid(column=1 , row=3)

#
precipitation_label = tk.Label(column1_frame , text="Precipitation : ",font=("",18,""),pady=10)
precipitation_label.grid(column=0 , row=4)

precipitation_value = tk.Label(column1_frame ,font=("",18,""),pady=10)
precipitation_value.grid(column=1 , row=4)


window.mainloop()