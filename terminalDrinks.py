import json
import requests

def api_random():
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    data = response.json()
    print('Response:',response, sep=' ')
    return data

def api_drink_name(name):
    response =requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+name)
    data = response.json()
    print('Response:',response, sep=' ')
    return data

def api_drink_first_letter(letter):
    response =requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f="+letter)
    data = response.json()
    print('Response:',response, sep=' ')
    return data

def displayDrink(data):
    x=1  
    print("\nYour Drink\n")
    for i in data['drinks']:
         
        #print("Id:", i['idDrink'])
        print("Name:", i['strDrink'], sep='\t\t')
        print("Category:", i['strCategory'], sep='\t')
        print("Alcoholic:", i['strAlcoholic'], sep='\t')
        print("Glass:", i['strGlass'],"\n", sep='\t\t')
        print('Ingredients:')
        
        x=1
        while x < 16: 
            if i['strIngredient'+str(x)] is not None:
                print('\t',i['strIngredient'+str(x)]+':\t\t',i['strMeasure'+str(x)], sep=' ')
            x=x+1
        
        print()
        if i['strInstructions'] is not None:
            print("Instructions:", i['strInstructions'],sep=' ')
            
        print('\n_____________________________________________________________________________________________________________________________________________________\n')
        


choice = input('Would you like to Get a Random Drink (type \'r\')\nIf you want drinks by name (type \'n\')\nIf you want drinks by first letter of name (type \'l\') : ')

if choice == 'n':
    name = input('Please input a drink name. : ')
    data = api_drink_name(name)
elif choice == 'l':
    letter = input('Please input the first letter of a drink. : ')
    data = api_drink_first_letter(letter)
else:
    data = api_random()

displayDrink(data)
print()
print()
    