import tkinter as tk
from tkinter import messagebox
import requests


# Function to fetch weather details
def get_weather():
    city = city_entry.get()
    api_key = 'your_api_key_here'  # Replace with your actual OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_desc = weather_data["weather"][0]["description"]

        weather_info = (
            f"Temperature: {temperature}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Description: {weather_desc}"
        )
    else:
        weather_info = "City Not Found"

    messagebox.showinfo("Weather Information", weather_info)


# Set up the main window
root = tk.Tk()
root.title("Weather Application")
root.geometry("300x200")

# Create and place the widgets
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=20)

# Run the application
root.mainloop()
