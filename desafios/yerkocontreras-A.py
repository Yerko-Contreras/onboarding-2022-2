from random_word import RandomWords
import pprint as p
r = RandomWords()
def generate_list(a):
    a_List = [] 
    for _ in range(a):
        a_List.append(r.get_random_word())
    return a_List


def suma(a, b):
    list_a = generate_list(int(a))
    list_b = generate_list(int(b))
    text = ""
    while len(list_a) > 0 and len(list_b) > 0:
        text += list_a.pop() + " "
        text += list_b.pop() + " "
    if a > b:
        while len(list_a) > 0:
            text += list_a.pop() + " "
    else: 
        while len(list_b) > 0:
            text += list_b.pop() + " "
    p.pprint(text)
    print(f"by the way, the value of the sum is: {text.count(' ') + a%1 + b%1}")

suma(5.1,7)   