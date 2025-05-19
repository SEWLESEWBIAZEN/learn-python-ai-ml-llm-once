def load_file():
    try:
        with open("recipes.txt",'r') as file:
            content=file.read()
            recipes=content.split("\n\n")            
            recipe_dict={}
            for recipe in recipes:
                lines=recipe.split("\n")
                if len(lines)>=3:
                    name=lines[0].strip()
                    ingredients=lines[1].replace("ingredients:","").strip()
                    instructions = lines[2].replace("instructions:","").strip()
                    recipe_dict[name]={"ingredients":ingredients, "instructions":instructions}
        return recipe_dict    
    except:
        print("File is not found!")
        return {}   

def main():
    print("\n----------------START--------------------")
    reciepes=load_file()
    for name in reciepes:
        print(f"\n----Recipe {name} Details------")  
        print(f"Ingredients")
        current_recipe_ingredients=reciepes[name]['ingredients'].strip().split(',')
        current_recipe_instructions=reciepes[name]['instructions'].strip().split(',')
        for ingredient  in current_recipe_ingredients:
            print(f"- {ingredient.strip()}")            
        print(f"Instructions")    
        for instruction in current_recipe_instructions:
            print(f"- {instruction.strip()}")
    print ("\n-----------------END--------------------\n")

main()
    



