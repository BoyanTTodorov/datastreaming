from string import ascii_lowercase
import numpy as np

class inputGenerator:
    def __init__(self, seed=0):
        self.randomseed = seed

    def generate_badge(self):
        return np.random.randint(1000, 10000, 1)[0]
        
    def generate_name(self):
        length = np.random.randint(5,10)
        return "".join(np.random.choice(list(ascii_lowercase), length)).capitalize()
    
    def generate_email(self):
        name = self.generate_name()
        return f"{name}@email.com"

inp = inputGenerator(5)
print(inp.generate_badge())
print(inp.generate_name())
print(inp.generate_email())