import json
from tkinter import *
from tkinter import ttk
import requests

root = Tk()
root.title('Drink DB')
root.geometry('1200x400')

# Create a main frame
frame = LabelFrame(root,padx=250,pady=10)
frame.pack(side=BOTTOM,fill=BOTH, expand=1)

randomBtn = Button(frame, text='Random Drink',command=lambda: randomClick()).grid(row=0, column =0)
nameBtn = Button(frame, text='Drink by Name',command=lambda: nameClick()).grid(row=0, column =1)
letterBtn = Button(frame, text='Drink by First Letter',command=lambda: call_drink()).grid(row=0, column =2)
ingredientBtn = Button(frame, text='Drink by Ingredient',command=lambda: api_drink_first_letter()).grid(row=0, column =3)



# Create a canvas
app_canvas = Canvas(frame)
app_canvas.grid(row=2, column =0, columnspan=4)

# Add a Scroll bar
v_scroll=ttk.Scrollbar(frame, orient=VERTICAL, command=app_canvas.yview)
v_scroll.grid(row=2, column =4)

# configure the canvas
app_canvas.configure(yscrollcommand=v_scroll.set)
app_canvas.bind('<Configure>', lambda e: app_canvas.configure(scrollregion=app_canvas.bbox('all')))

# create ANOTHER frame inside the Canvas
inner_frame = Frame(app_canvas)

# add new frame to the canvas 
app_canvas.create_window((0,0), window=inner_frame, anchor='nw')


#v = Scrollbar(root, orient=VERTICAL)
#v.grid(row=3,column=2,sticky='ns')


varinput=StringVar()

def api_random():
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    data = response.json()
    #print('Response:',response, sep=' ')
    return data

def api_drink_name(name):
    response =requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+name)
    data = response.json()
    #print('Response:',response, sep=' ')
    return data

def api_drink_first_letter(letter):
    response =requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f="+letter)
    data = response.json()
    #print('Response:',response, sep=' ')
    return data

def api_search_ingredient(ingredient):
    response =requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+ingredient)
    data = response.json()
    #print('Response:',response, sep=' ')
    return data

def api_drink_by_id(id):
    #print('Id ',id)
    response =requests.get("https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="+id)
    data = response.json()
    #print('Response:',response, sep=' ')
    displayDrink(data)
    

def processIngredient(data):
    
    for i in data['drinks']:
        api_drink_by_id(i['idDrink'])

def randomClick():
    print('Was Clicked')
    data = api_random()
    clear_frame()
    displayDrink(data)
    
def nameClick():
    #varinput.get()
    nameLabel1=Label(frame, text="Drink Name",justify=LEFT).grid(row=1,column=0,sticky=W)
    nameInput=Entry(frame,textvariable=varinput,justify=LEFT,width=47).grid(row=1,column=1,columnspan=4,sticky=W)
    buttonDrink = Button(frame, text="Get My Drink", command=lambda: call_drink(varinput.get())).grid(row=1, column=4,sticky=W)
    
def call_drink(name):
    print(name)
    data = api_drink_name(name)
    print(data)
    clear_frame()
    displayDrink(data)
    
def clear_frame():
    exists=inner_frame.winfo_exists()
    if exists == 1:
        for widget in inner_frame.winfo_children():
            widget.destroy()
        
    

def displayDrink(data):
    x=1 
    rowNum =2 
    #print("\nYour Drink\n")
    for i in data['drinks']:
        
        #print("Id:", i['idDrink'])
        nameLabel=Label(inner_frame,text="Name:",justify=LEFT).grid(row=rowNum,column=0,sticky=W)            
        name2Label=Label(inner_frame,text=i['strDrink'],justify=LEFT).grid(row=rowNum,column=1,sticky=W)
        rowNum+=1
        categoryLabel=Label(inner_frame,text="Category:",justify=LEFT).grid(row=rowNum,column=0,sticky=W)
        category2Label=Label(inner_frame,text=i['strCategory'],justify=LEFT).grid(row=rowNum,column=1,sticky=W)
        rowNum+=1
        alcoholicLabel=Label(inner_frame,text="Alcoholic:",justify=LEFT).grid(row=rowNum,column=0,sticky=W)
        alcoholic2Label=Label(inner_frame,text=i['strAlcoholic'],justify=LEFT,padx=15).grid(row=3,column=1,sticky=W)
        rowNum+=1
        glassLabel=Label(inner_frame,text="Glass:",justify=LEFT).grid(row=rowNum,column=0,sticky=W)
        glass2Label=Label(inner_frame,text=i['strGlass'],justify=LEFT).grid(row=rowNum,column=1,sticky=W)
        rowNum+=1 
        space1=Label(inner_frame,text="   ").grid(row=rowNum,column=0,sticky=W)
        rowNum+=1 
        ingredientsLabel=Label(inner_frame,text='Ingredients:',justify=LEFT).grid(row=rowNum,column=0,sticky=W) 
        rowNum+=1
        
        
        while x < 16: 
            if i['strIngredient'+str(x)] is not None:
                ingredient=Label(inner_frame,text=i['strIngredient'+str(x)],justify=LEFT).grid(row=rowNum,column=0,sticky=W)
                measure=Label(inner_frame,text=i['strMeasure'+str(x)],justify=LEFT).grid(row=rowNum,column=1,sticky=W)
                rowNum+=1
            x=x+1
        
        if i['strInstructions'] is not None:
            space2=Label(inner_frame,text="   ").grid(row=rowNum,column=0,sticky=W) 
            rowNum+=1
            measure=Label(inner_frame,text="Instructions:").grid(row=rowNum,column=0,sticky=W)
            rowNum+=1
            measure=Label(inner_frame,text= i['strInstructions'],justify=LEFT,wraplength=220).grid(row=rowNum,column=0,sticky=W)
            
        brLine=Label(inner_frame,text='   ').grid(row=x+11,column=0,sticky=W)
        rowNum+=2
        


root.mainloop()

'''
choice = input('Would you like to Get a Random Drink (type \'r\')\nIf you want drinks by name (type \'n\')\nIf you want drinks by first letter of name (type \'l\')\nIf you want drinks by ingredient (type \'i\') : ')

if choice == 'n':
    name = input('Please input a drink name. : ')
    data = api_drink_name(name)
    displayDrink(data)
elif choice == 'l':
    letter = input('Please input the first letter of a drink. : ')
    data = api_drink_first_letter(letter)
    displayDrink(data)
elif choice == 'i':
    ingredient = input('Please input the drink ingredient. : ')
    data = api_search_ingredient(ingredient)
    processIngredient(data)
else:
    data = api_random()
    displayDrink(data)
'''