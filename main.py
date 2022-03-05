from itertools import product
from posixpath import split
from unicodedata import name
from pyfiglet import Figlet
import qrcode

PRODUCTS=[]

def show_menu() :
    print('1: Add product')
    print('2: Edit product')
    print('3: Delet product')
    print('4: Search product')
    print('5: show list')
    print('6: Buy')
    print('7: Exit')
    print('8: Qrcode')

def load() :
    print('Loading...')
    myfile= open('database.txt', 'r')
    products_list= myfile.read().split('\n')
    
    for i in range(len(products_list)):
        mydict={}
        product_info = products_list[i].split(',')
        #PRODUCTS.append({'id': product_info[0], 'name': product_info[1], 'price': product_info[2], 'count': product_info[3]})
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        mydict['count'] = product_info[3]
        PRODUCTS.append(mydict)
    print("Welcome")

def code():
    id=int(input("Enter Product_Id: "))
    for i in range (len(PRODUCTS)):
        if PRODUCTS[i]['id']==id :
            img=qrcode.make(PRODUCTS[i]['name'] + PRODUCTS[i]['price'] + PRODUCTS[i]['count'])
            img.save('qrcode.png')

def save():
    my=open('database.txt','w')
    for i in range(len(PRODUCTS)):
        my.write(str(PRODUCTS[i]["id"]) + ',' + 
                 PRODUCTS[i]["name"] + ',' + 
                 str(PRODUCTS[i]["price"]) + ',' + 
                 str(PRODUCTS[i]["count"]) + '\n')
    
    print("changes saved successfully")        
    my.close()

def add():

    id=int(input("pls enter Product_Id: "))
    name=input("please enter Product_Name: ")
    price=int(input("pls enter Product_Price: "))
    count=int(input("pls enter Product_Count: "))
    
    PRODUCTS.append({'id': id,'name': name,'price': price,'count': count})
    
    print("new product added!")

def delet():
    x=int(input("Product_id: "))
    
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']==x:
            del PRODUCTS[i]
            print("deleted!")
            break        

def Edit():
    i=0
    n=input("write name of Product: ")
    while i < len(PRODUCTS):
        if PRODUCTS[i]['name']==n:
            y=int(input("what do you want to change: 1.ID 2.Price 3.Count: "))
            if y==1:
                x1=int(input("New id: "))
                PRODUCTS[i]['id']=x1
            elif y==2:
                x2=int(input("New Price: "))
                PRODUCTS[i]['price']=x2
            elif y==3:
                x3=int(input("New count: "))
                PRODUCTS[i]['count']=x3
            break            
        i+=1        
   
def search():

    print("Enter Product_name: ")
    n1=input()
    for i in range (len(PRODUCTS)):
        if PRODUCTS[i]['name'] ==n1 :
            print("searching done...")
            print(PRODUCTS[i])
            break
        elif i==(len(PRODUCTS)-1) and PRODUCTS[i]['name'] != n1 :
            print("in kala mojud nist")

def show_list() :

    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def Buy():

    show_list()
    a=1
    sum2=0 
    while a==1 :               
        n1=input("please enter Product_id: ")

        for i in range (len(PRODUCTS)):
            if PRODUCTS[i]['id'] ==n1 :
                print('Name: ' + PRODUCTS[i]['name'])
                print('Price: '+ PRODUCTS[i]['price'])
                c = int(input("che tedad mikhay: "))
                if c<=int(PRODUCTS[i]['count']):
                    PRODUCTS[i]['count']= int(PRODUCTS[i]['count'])-c
                    sum1=c * int(PRODUCTS[i]['price'])                       
                    sum2=sum1+sum2
                    print("kala be sabad kharid ezafe shod")
                else:
                    print("moajaz nis!!!")
                    print("mojudi anbar: ", PRODUCTS[i]['count'])

        a=int(input("1.shopping  2.payment: "))
        if a==2:  
            break          
    print('factore shoma: ')            
    print('sum: ',sum2)                      

f=Figlet(font='standard')
print(f.renderText('Atour store'))

load()
show_menu()

while True:
    n= int(input("your choice: "))

    if n==1:
        add()
    
    elif n==2:
        Edit()
        
    elif n==3:
        delet()
    
    elif n==4:
        search()
    
    elif n==5:
        show_list()
    
    elif n==6:
        Buy()
    
    elif n==7:
        save()
        exit()

    elif n==8:
        code()