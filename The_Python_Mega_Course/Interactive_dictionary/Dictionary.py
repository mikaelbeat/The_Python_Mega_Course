import json
from difflib import get_close_matches
   
data = json.load(open("data.json"))
   
def dictionary():
    
    def get_definition():
           
        word = input("Give word to search: ").lower()
           
        if word in data:
            print(f"\nDefinition for word {word} is:")
            return data[word]
        elif word.title() in data:
            print(f"\nDefinition for word {word} is:")
            return data[word.title()]
        elif word.upper() in data:
            print(f"\nDefinition for word {word} is:")
            return data[word.upper()]
        elif len(get_close_matches(word,data.keys())) > 0:
            result = get_close_matches(word, data.keys())
            result = result[0]
            decision = input(f"\nDid you mean {result}, y, n? ").lower()
            if decision == "y":
                print(f"\nDefinition for word {result} is:")
                return data[result]
            else:
                return f"\nDefinition for word {word} not found."
        else:
            return f"\nWord {word} not found!"
            
    result = get_definition()
       
    def convert_result_printout(data):
        if type(data) == list:
            for value in data:
                print(value)
        else:
            print(data)
                        
    convert_result_printout(result)
       
       
dictionary()