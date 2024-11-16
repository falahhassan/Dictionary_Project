import json
from pynput import keyboard


with open("dictionary.json","r") as file:
    data =json.load(file)

while True:
    
   
   try:
       user_input = input("Enter Your Word: ").lower()    
       print(data[user_input])    
   except Exception:
       print("Word not exist Try another Word")
   if keyboard.Events.Press("esc"):
       print("quiting the program")
       break