# phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
# for name, number in phonebook.items():
    # print("Phone number of %s is %d" % (name, number))
# CODE ABOVE is for iterating through a dictionary

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
phonebook["Jake"] = 938273443
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  

