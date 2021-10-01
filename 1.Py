
print ("CP5") 
print ("how many ingredients do we have ?") 

axe=int(input("Do you have axe?:"))
if axe>0 and axe<=1:
    print("We have:",axe,"axe")
    a="we have axe+"
else:
    print("We have:",axe,"axes")
    a="we have axe+"
    
water=int(input("Do you have water?:"))
if water>0:
    print("We have:",water,"L of water")
    w="water,"
else:
    w=" "
    
salt=int(input("Do you have salt?:"))
if salt>0:
    print("We have:",salt,"kg of salt") 
    s="salt,"
else:
    s=" "    
butter=int(input("Do you have butter?:"))    
if butter>0:
    print("We have:",butter,"gm of butter")    
    b="butter,"
else:
    b=" "   
    
oats=int(input("Do you have oats?:"))    
if oats>0:
    print("We have:",oats,"kg of oats")
    o="oats"
else:
    o=" "  

print("for porridge",a,w,s,b,o) 
