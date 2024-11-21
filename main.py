import json
import useful_functions

#opining the dictionary file
with open("dictionary.json","r") as file:
    data =json.load(file)
#Variables Global
word_list =[]
word_dict ={}
dict = {}



#Starting the dictionary    
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
       print("\n\nWord not exist Try another Word Maybe You mean:\n")
       print(useful_functions.close_match(user_input, data))


#adding words to dictionary list

   if user_input in data:
       print("\n\nExist!!!!!!!!!!")
       word_list.append(user_input)
       if user_input in word_list:

           word_occurance = word_list.count(user_input)
           word_dict.update({user_input : word_occurance})

   print(word_list)  
   print(word_dict)     

