import os
import time 
import random

a=time.localtime()
b=time.strftime("%H",a)
standard_time=int(b)

"""------------------------------------     grocery item     -------------------------------------"""
main_storage={1:"shopping",2:"checking price"}   
items1={1:"soap",2:"vegetables",3:"biscuits",4:"rice",5:"flour",6:"chocolates",7:"snack"}

soap={"lux":10,"detol":10,"no.1":10,"pears":30,"life boy":10}    
vegetables={"coliflower":40,"potato":30,"tomato":50,"cabbage":40}
biscuits={"good day":20,"dark fantasy":50,"hide & seek":50,"jim-jam":30,"cadbury choco bar":70,"treat burst":20}
rice={"small rice":40,"biryani rice":70,"long rice":50,"basmati rice":60,"jeera samba":60}
flour={"whole wheat flour":210,"refined wheat flour(maida)":20,"semolina(suji)":30,"gram flour(besan)":60}
chocolates={"kit_kat":20,"dairy milk":40,"dark chocolate":60,"amul 70% dark":100,"ferrero rocher":240}
snack={"kurkure":20,"lays":20,"kerala banana chips":40,"pringles potato chips":100}

""""-------------------------------        defining functions        ----------------------------"""
 
l3=list()
quantity3=list()
def soap_():
    print(soap)
    while True:
        inp=input("enter item :").strip().lower()
        l3.append(inp)
        if(inp=="") : 
            l3.pop()
            break
        elif inp not in soap:
            print("sorry item is not available")
            l3.pop()
    for item in l3:
        qnt=int(input(f"enter no of packets of {item} :"))
        quantity3.append(qnt)
    for a,b in zip(l3,quantity3):   
        print(a,b)   
    print("\n")
    time.sleep(1)

l4=list()
quantity4=list()
def vegetables_():
    print(vegetables)
    while True:
        inp=input("enter item :").strip().lower()
        l4.append(inp)
        if(inp==""):
            l4.pop()
            break
        elif inp not in vegetables:
            print("sorry item is not available")
            l4.pop()
    for item in l4:
        qnt=int(input(f"enter no of packets of {item} :"))    
        quantity4.append(qnt) 
    for a,b in zip(l4,quantity4):   
        print(a,b)       
    print(l4,quantity4)   
    print("\n") 
    time.sleep(1)

l5=list()
quantity5=list()
def biscuits_():
    print(biscuits)  
    while True:
        inp=input("enter item :").strip().lower()    
        l5.append(inp)
        if(inp==""):
            l5.pop()
            break
        elif inp not in biscuits:
            print("sorry item is not available")
            l5.pop()
    for item in l5:
        qnt=int(input(f"enter no of packets of {item} :"))  
        quantity5.append(qnt) 
    for a,b in zip(quantity5,l5) :
        print(a,b)
    print("\n")
    time.sleep(1)

l6=list()
quantity6=list()
def rice_():
    print(rice)
    while True:
        inp=input("enter item :").strip().lower()
        l6.append(inp)
        if(inp==""):
            l6.pop()
            break
        elif inp not in rice:
            print("sorry item is not available")
            l6.pop()
    for item in l6:
        qnt=int(input(f"enter no of packets of {item} :")) 
        quantity6.append(qnt)       
    for a,b in zip(quantity6,l6) :            
        print(a,b) 
    print("\n")  
    time.sleep(1)        

l7=list()
quantity7=list()
def flour_():
    print(flour)
    while True:
        inp=input("enter item :").strip().lower()
        l7.append(inp)
        if(inp==""):
            l7.pop()
            break
        elif inp not in flour:
            print("sorry item is not available")
            l7.pop()
    for item in l7:
        qnt=int(input(f"enter no of packets of {item} :")) 
        quantity7.append(qnt)
    for a,b in zip(quantity7,l7):                  
        print(a,b)
    print("\n")
    time.sleep(1)

l8=list()
quantity8=list()
def chocolates_():
    print(chocolates)  
    while True:
        inp=input("enter item :").strip().lower()
        l8.append(inp)
        if(inp==""):
            l8.pop()
            break
        elif inp not in chocolates:
            print("sorry item is not available")
            l8.pop()
    
    for item in (l8):             
        qnt=int(input(f"enter no of packets of {item} :")) 
        quantity8.append(qnt)   
    for a,b in zip(quantity8,l8): 
        print(a,b)   
    print("\n")
    time.sleep(1) 

l9=list()
quantity9=list()
def snack_():
    print(snack)
    while True:
        inp=input("enter item :").strip().lower()
        l9.append(inp)
        if(inp==""):
            l9.pop()
            break
        elif inp not in snack:
            print("sorry item is not available")
            l9.pop()
    for item in l9:
        qnt=int(input(f"enter no of packets of {item} :")) 
        quantity9.append(qnt)   
    for a,b in zip(quantity9,l9) :            
        print(a,b)
    print("\n")    
    time.sleep(1)

"""--------------------------        function for bill calculation       --------------------------"""
def bill_calculation():

    bill1=0
    for qnt,items in zip(quantity3,l3):
        bill1=bill1+(soap[items]*qnt)
        print(f"{qnt}*{items} :{soap[items]*qnt}")
        if items not in soap:
            print("not in store")

    bill2=0
    for qnt,items in zip(quantity4,l4):
        bill2=bill2+(vegetables[items]*qnt)
        print(f"{items} :{vegetables[items]*qnt}")
        if items not in vegetables:
            print("not in store") 
    bill3=0
    for qnt,items in zip(quantity5,l5):
        bill3=bill3+(biscuits[items]*qnt)
        print(f"{items} :{biscuits[items]*qnt}")
        if items not in biscuits:
            print('not in store')
    
    bill4=0
    for qnt,items in zip(quantity6,l6):
        bill4=bill4+(rice[items]*qnt)
        print(f"{items} :{rice[items]*qnt}")
        if items not in rice:
            print('not in store')
        
        
    bill5=0
    for qnt,items in zip(quantity7,l7):
        bill5=bill5+(flour[items]*qnt)
        print(f"{items} :{flour[items]*qnt}") 
        if items not in flour:
            print('not in store')
        
    
    bill6=0
    for qnt,items in zip(quantity8,l8):
        bill6=bill6+(chocolates[items]*qnt)
        print(f"{items} :{chocolates[items]*qnt}") 
        
    bill7=0
    for qnt,items in zip(quantity9,l9):
        bill7=bill7+(snack[items]*qnt)
        print(f"{items} :{snack[items]*qnt}")

    final_bill=bill1+bill2+bill3+bill4+bill5+bill6+bill7

    return final_bill
    
a1=bill_calculation()  
"""----------------------------------       calling functions(main programm)     ----------------------------------"""

name=input("sir please enter your good name :")

"""  ---------------------------------       greatings       ---------------------------------  """

if  16>standard_time>=12:
    print(f"Good afternoon {name}")
elif 19>=standard_time>16:
    print(f"Good evening {name}")    
elif 22>=standard_time>19 :  
    print(f"good night sir{name}")
elif 24>= standard_time>22:
    print(f"good night sir{name}")  
    print("actually the store is closed but you can place your order")
elif 5>=standard_time>1:
    print(f"good night {name}")  
    print("actually the store is closed, but you can place your order")  
else:    
    print(f"Good morning {name}")


"""---------------------------      item adding function      ---------------------------"""
def item_adding():
        while True:
            print(items1)
            input2=input("enter the category you want to buy from (press enter to stop) :").strip().lower()
            if(input2==""):
                break
            if(input2=="soap"):
                soap_()
            elif(input2=="vegetables"):
                vegetables_()   
            elif(input2=="biscuits"):
                biscuits_()     
            elif(input2=="rice"):
                rice_()
            elif(input2=="flour"):
                flour_()
            elif(input2=="chocolates"):
                chocolates_()
            elif(input2=="snack"):
                snack_()
            else:
                print("item is not in list")   
                
        """---------------------------     bill generation      ---------------------------"""     
        
        print(f"your total bill is :{bill_calculation()}\n")
        time.sleep(3)


print(main_storage)
input1=input("sir choose one of them :").strip().lower()
if(input1=="shopping"):
   item_adding()

"""----------------------------    discount in bill     ---------------------------"""

print("due to diwali fastival we are giving additional discount of 10% on shopping above 300 rs")
if(bill_calculation()<300):
    print(f"sir add item of atleast {300-bill_calculation()} to get discount\n")
    
    inp=int(input("do you want to add more items yes(1)/no(0) :"))
    if (inp==1):       
        while True:
            print(items1)
            input2=input("enter the category you want to buy from (press enter to stop) :").strip().lower()
            item_adding()

if bill_calculation()>300:
    final_bill=bill_calculation()-(bill_calculation()*10/100)
    print(f"your final bill after discount is :{final_bill}\n")


"""------------------------------      ---file handling---       --------------------------------"""
c=time.strftime("%D",a)

dir=os.getcwd()
destination_folder=os.path.join(dir,"GROSORY_STORE")
destination_file=os.path.join(destination_folder,f"{name}.txt")
if not os.path.exists(destination_file):

    all_lists=[l3,l4,l5,l6,l7,l8,l9]
    if any(all_lists):
        with open(f"GROSORY_STORE\{name}.txt","w") as f:
            f.write("Hi,")
            f.write(f"\n{name}     date:{c}")
            f.write(f"\n your order is\n{all_lists}")
            f.write(f"\n your bill is :{bill_calculation()}\n") 

elif  os.path.exists(destination_file):
    all_lists=[l3,l4,l5,l6,l7,l8,l9]
    if any(all_lists):
        print(f"{all_lists}")
        print(f"{bill_calculation()}")

                

               
