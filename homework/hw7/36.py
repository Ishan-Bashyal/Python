#removal bad characters from the given string. 
#Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  
#Expected output = pythonpython

bad_chars = [';', ':', '!', '*', ' ']
string = "py;th* o:n ! ;py * t*h:o !n"
i=0
while i < len(bad_chars):
    string = string.replace(bad_chars[i], "")
    i+=1
print(string)