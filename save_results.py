# save results
import json
import os

class save_res:
    def save_name(name):
        name = input('Input your name')

        if os.path.exists('results.json'): # checking exist result.json
            with open('results.json') as res:
                results = json.load(res)
        else:
            results = {}    
        
        if name != results[name]: # checking exist name
            score = 0
            results.update({name: score})
        
        with open('results.json', 'w', encoding='utf-8') as res:
            json.dump(results, res, indent=4)




