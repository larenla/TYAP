import random 

i=1 

rules={ 

    'S':['aA','bB','aC'], 

    'A':['bA','bB','c'], 

    'B':['aA','cC','b'], 

    'C':['bB','bC','a'], 

    } 

     

def generate_random_string(start_symbol): 

     

    if start_symbol in rules: 

        production=random.choice(rules[start_symbol]) 
        result='' 
        for symbol in production: 
            result+=generate_random_string(symbol) 
            print(production," -> ",end="")
        return result 
    else: 
        return start_symbol 
        
        
for _ in range (10): 
    random_string=generate_random_string('S') 
    print("")
    print(i, ')',random_string) 
    i+=1 




    if (random_string=='abbbbc'): 
        print('--------------yes--------------------------------------------------------------------') 
         

         