print("CP5")
print("In which container does it fit?")
while True:
    try:
        V = int(input("What's the capacity of V? : "))
    except:
        print('Use numbers!')
        continue
    break
print("We have: " + str(V) + "l in V.")


while True:
    try:
        area = int(input("What's the volume for V1? : "))
    except:
        print('Use numbers!')
        continue
    break
V1 = area * area * area
print("we have: " + str(V1) + "in V1.")

while True:
    try:
     R = int(input("what's the radius for V2? : "))
     H = int(input("what's the height for V2? : "))
    except :
        print('Use numbers!')
        continue
    break
V2 = 3.14 * R * R * H 
print("we have: " + str(V2) + "cm3 in V2")
if ((V1 >= V) and (V2 >= V)):
    print("both can contain")
else:
    if ((V1 > V) or (V1 == V)):
           print("V1 can contain")
    else:
        print("V2 can contain")




     


     
                  
