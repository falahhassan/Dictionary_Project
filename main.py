import json
import useful_functions


with open("dictionary.json","r") as file:
    data =json.load(file)
print("T H I S  I S  M Y  F I R S T  D I C T I O N A R Y")
print("=================================================\n\n")

while True:
   
   try:
    
       user_input = input("Enter Your Word: ").lower() 
       meaning= data[user_input]
       if user_input=="q":
            print("quiting the program")
            break
       else:     
            print(meaning)
   except Exception:
       print("Word not exist Try another Word Maybe You mean:\n")
       print(useful_functions.close_match(user_input, data))
   