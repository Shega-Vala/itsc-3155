def two_end_string(str):
    
    if len(str)>2:
        return str[0:2] + str[-2:]
    else:
        return "This string is too short!"
    
name = input("Please enter a string: ")    
print(two_end_string(name))