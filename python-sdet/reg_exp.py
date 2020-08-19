import re
if(re.search(r"A..l","Aopline")!=None): # each . represents a single character
    print("Dot Pattern found")
else:
    print("Dot Pattern not found")

if(re.search(r"A\dl","A2line")!=None):  #Digit after A
    print("Digit Pattern found")
else:
    print("Digit Pattern not found")

if(re.search(r"A\d*","A2234line")!=None): #Zero or more occurence
    print("Star Pattern found")
else:
    print("Star Pattern not found")

if(re.search(r"A\d+","Airline")!=None): #One or more occurences
    print("Plus Pattern found")
else:
    print("Plus Pattern not found")

if(re.search(r"A\d?i","Airline")!=None): #Zero or one occurence
    print("Question mark Pattern found")
else:
    print("Question mark Pattern not found")

if(re.search(r"A\d{3}i","A223irline")!=None):   #{n} no of occurences or not
    print("{n} Pattern found")
else:
    print("{n} Pattern not found")

if(re.search(r"A[4-8]l","A2line")!=None):   # elements within the square braces are present in the actual string or not
    print("Sq braces Pattern found")
else:
    print("Sq braces Pattern not found")

if(re.search(r"^A","Airline")!=None):   #String starts with the specified character or not
    print("^ Pattern found")
else:
    print("^ Pattern not found")

if(re.search(r"e$","Airline")!=None):   #String ends with the specified character or not
    print("$ Pattern found")
else:
    print("$ Pattern not found")

if(re.search(r"\w$","Airline%")!=None): #alphanumeric character present or not. includes A-Z, a-z, 0-9 and _
    print("alpha-num Pattern found")
else:
    print("alpha-num Pattern not found")

if(re.search(r"Air\s","Airline")!=None):    #Air is followed by a space or not
    print("Space Pattern found")
else:
    print("Space Pattern not found")

if(re.search(r"Hell|Fell","Fellow")!=None): #Either side of the | operator consists of a part of the given string
    print("Pipe Pattern found")
else:
    print("Pipe Pattern not found")

# Substitution using regex
import re
flight_details="Flight Savana Airlines a2134"
print(flight_details)
print(re.sub(r"Flight",r"Plane",flight_details))


