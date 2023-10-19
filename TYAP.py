import random

i = 1

rules = {

    'S': ['aA', 'bB', 'aC'],

    'A': ['bA', 'bB', 'c'],

    'B': ['aA', 'cC', 'b'],

    'C': ['bB', 'bC', 'a'],

}


def generate_random_string(start_symbol):
    if start_symbol in rules:

        production = random.choice(rules[start_symbol])
        result = ''
        print(start_symbol, "->", production, "     ", end="")
        for symbol in production:
            result += generate_random_string(symbol)

        return result
    else:
        return start_symbol


for _ in range(100):
    random_string = generate_random_string('S')
    print("")
    print(i, ')', random_string)
    i += 1

    if (random_string == 'abbbbc'):
        print('--------------------------------yes---------------------------------------')


