import json
import requests
from urlImageFrame import ImageFrame
import tkinter as tk
from tkinter import ttk

rowNum= 0

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

def on_button_click(button):
    varinput=tk.StringVar()
    clear_frame()
    print(f"You clicked {button['text']} button")
    if button == button1:
        randomClick()
    elif button == button2:
        button5 = tk.Button(row2_frame, text=button['text'], command=lambda: call_drink(varinput.get()))
        entry = tk.Entry(row2_frame,textvariable=varinput)

        button5.pack(side="left")
        entry.pack(side="left", fill="x", expand=True)
    
    elif button == button3:
        
        button5 = tk.Button(row2_frame, text=button['text'], command=lambda: api_drink_first_letter(varinput.get()))
        entry = tk.Entry(row2_frame,textvariable=varinput)

        button5.pack(side="left")
        entry.pack(side="left", fill="x", expand=True)
        
    else:
        button5 = tk.Button(row2_frame, text=button['text'], command=lambda: api_search_ingredient(varinput.get()))
        entry = tk.Entry(row2_frame,textvariable=varinput)

        button5.pack(side="left")
        entry.pack(side="left", fill="x", expand=True)
 
    
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
    displayDrink(data)

def api_search_ingredient(ingredient):
    response =requests.get("https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="+ingredient)
    data = response.json()
    #print('Response:',response, sep=' ')
    processIngredient(data)

def api_drink_by_id(id):
    #print('Id ',id)
    response =requests.get("https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="+id)
    data = response.json()
    #print('Response:',response, sep=' ')
    displayDrink(data)
    

def processIngredient(data):
    row_reset()
    for i in data['drinks']:
        api_drink_by_id(i['idDrink'])

def randomClick():
    data = api_random()
    displayDrink(data)
    
    
def call_drink(name):
    #print(name)
    data = api_drink_name(name)
    #print(data)
    displayDrink(data)
    
def clear_frame():
    row_reset()
    for widget in inner_frame.winfo_children():
        widget.destroy()
    for widget in row2_frame.winfo_children():
        widget.destroy()
    

def displayDrink(data):
    x=1 
        #print("\nYour Drink\n")
    for i in data['drinks']:
        global rowNum
        #print("Id:", i['idDrink'])
        rowNum+=1
        print(rowNum)
        name=tk.Label(inner_frame,text="Name:").grid(row=rowNum,column=0)            
        name=tk.Label(inner_frame,text=i['strDrink']).grid(row=rowNum,column=1)
        rowNum+=1
        print(rowNum)
        categoryLabel=tk.Label(inner_frame,text="Category:").grid(row=rowNum,column=0)
        category2Label=tk.Label(inner_frame,text=i['strCategory']).grid(row=rowNum,column=1)
        rowNum+=1
        print(rowNum)
        alcoholicLabel=tk.Label(inner_frame,text="Alcoholic:").grid(row=rowNum,column=0)
        alcoholic2Label=tk.Label(inner_frame,text=i['strAlcoholic'],padx=15).grid(row=3,column=1)
        rowNum+=1
        print(rowNum)
        glassLabel=tk.Label(inner_frame,text="Glass:").grid(row=rowNum,column=0)
        glass2Label=tk.Label(inner_frame,text=i['strGlass']).grid(row=rowNum,column=1)
        rowNum+=1
        print(rowNum)
        iframe = ImageFrame(inner_frame, i['strDrinkThumb']+'/preview')
        iframe.grid(row=rowNum, column=0)
        rowNum+=1
        space1=tk.Label(inner_frame,text="   ").grid(row=rowNum,column=0)
        rowNum+=1
        print(rowNum)
        ingredientsLabel=tk.Label(inner_frame,text='Ingredients:').grid(row=rowNum,column=0) 
        rowNum+=1
        print(rowNum)
        
        
        while x < 16: 
            if i['strIngredient'+str(x)] is not None:
                ingredient=tk.Label(inner_frame,text=i['strIngredient'+str(x)]).grid(row=rowNum,column=0)
                measure=tk.Label(inner_frame,text=i['strMeasure'+str(x)]).grid(row=rowNum,column=1)
                rowNum+=1
                print(rowNum)
            x=x+1
        
        if i['strInstructions'] is not None:
            space2=tk.Label(inner_frame,text="   ").grid(row=rowNum,column=0) 
            rowNum+=1
            print(rowNum)
            measure=tk.Label(inner_frame,text="Instructions:").grid(row=rowNum,column=0)
            rowNum+=1
            print(rowNum)
            measure=tk.Label(inner_frame,text= i['strInstructions'],wraplength=220).grid(row=rowNum,column=0)
            rowNum+=1
            
        brLine=tk.Label(inner_frame,text="*********************************************************").grid(row=rowNum,column=0,columnspan=2)
        rowNum+=2
        print(rowNum)
         
def row_reset():
    global rowNum
    rowNum = 0
    

root = tk.Tk()
root.geometry("450x600")

# Row 1
row1_frame = tk.Frame(root)
row1_frame.pack(fill="x")

button1 = tk.Button(row1_frame, text="Random Drink", command=lambda: on_button_click(button1))
button2 = tk.Button(row1_frame, text="Drink by Name", command=lambda: on_button_click(button2))
button3 = tk.Button(row1_frame, text="Drink by First Letter", command=lambda: on_button_click(button3))
button4 = tk.Button(row1_frame, text="Drink by Ingredient", command=lambda: on_button_click(button4))

button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="left")
button4.pack(side="left")

# Row 2
row2_frame = tk.Frame(root)
row2_frame.pack(fill="x")

# Row 3
row3_frame = tk.Frame(root)
row3_frame.pack(fill="both", expand=True)

scrollable_frame = ScrollableFrame(row3_frame)
scrollable_frame.pack(side="top", fill="both", expand=True)

inner_frame= tk.Frame(scrollable_frame.scrollable_frame)
inner_frame.pack(expand=True)





'''
for i in range(50):
    label = tk.Label(scrollable_frame.scrollable_frame, text=f"Label {i}")
    label.pack()
'''
root.mainloop()