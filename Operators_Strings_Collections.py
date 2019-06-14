#Operators
print('Addition: '+str(1+1))
print('Division: '+str(13/2))  #Floor Division
print('Modulo Division: '+str(13//2))  # Integer Division
print('Exponental: '+str(2**6))
print('Absolute Value: '+str(abs(-5)))

#Try Catch
try:
    a=5/0
    print("Good to go")
except:
    print("Don't do that")

#String Methods
name = "  rakesh bairi  "
print ("Length "+str(len(name)))
print ("Upper "+name.upper())
print ("lower "+name.lower())
print ("Capitalize "+name.capitalize())
print ("Title "+name.title())

print(name.isalpha()) # Check only alphabets without spaces or numbers
s='Welcome '
print(s*5)

print("Strip:-"+name.strip( ))
print("Strip remove r:-"+name.strip('r'))

print("Strip count:-"+name.count())