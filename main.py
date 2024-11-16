import json
from linecache import getline
from pynput import keyboard


with open("dictionary.json","r") as file:
    data =json.load(file)

while True:
   
   try:
    
       user_input = input("Enter Your Word: ").lower() 
       meaning= data[user_input]
       line = getline(meaning,0)
       if user_input=="q":
            print("quiting the program")
            break
       else:     
            print(line)
   except Exception:
       print("Word not exist Try another Word")
   