def search_by_name(filename: str, word: str):
    recipetitle = []
    wordlist = []
    previouswrd = None
    with open(filename) as new_file :
        for line in new_file : 
            line = line.replace("\n" , "")
            wordlist.append(str(line))
        for words in wordlist :
            if word.lower() in words.lower() and (previouswrd == "" or previouswrd == None): 
                recipetitle.append(str(words))
            previouswrd = words
    return recipetitle
def search_by_time(filename: str, prep_time: int):
    recipes = []
    results = []
    with open(filename) as new_file :
        for line in new_file:
            line = line.replace("\n","")
            recipes.append(str(line))
        idx = 0
        recipes.append("")
        while idx < len(recipes):
            index = recipes.index("" , idx)
            if prep_time >= int(recipes[(idx + 1)]):
                theresult = (f"{recipes[idx]}, preparation time {recipes[(idx + 1)]} min")
                results.append(theresult)
            idx = index + 1
    return results
def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as new_file:
        recipes = []
        final = []
        for line in new_file : 
            line = line.replace("\n","")
            recipes.append(line)
        recipes.append("")
        idx = 0
        while idx < len(recipes) : 
            index = recipes.index("" , idx)
            for word in recipes[idx + 2 : index] : 
                if ingredient.lower() in str(word).lower() :
                    meow =(f"{recipes[idx]}, preparation time {recipes[idx + 1]} min")
                    final.append(meow)
            idx = index + 1
        return final

            