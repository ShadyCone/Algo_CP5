
print ("CP5") 
  
print ("CP5") 
print ("In which container does it fit?") 
V= int(input("what's the capacity for V? : "))
print("we have:" ,V, "l in V")

area= int(input("what's the capacity for v1? : "))
V1=area*area*area
print("We have:",V1,"m^3 in V1")

R= int(input("what's the radius for V2? : "))
H= int(input("what's the height for V2? : "))
V2=3.14*R*R*H
print("we have:", V2, "cm^3 in V2")
if((V1>=V) and (V2>=V)):
        print("both can contain")
else:
        if ((V1>V) or (V1==V)):
            print("V1 can contain")
        else: 
               ("V2 can contain")
