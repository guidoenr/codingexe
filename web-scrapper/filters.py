from conf.dniranges import data

class Filter():
    def __init__(self):
        ...

    def apply(self):
        ...

class DniRange(Filter):
    def __init__(self, age:str, dni:str):
        super().__init__()
        self.age = age
        self.dni = dni

    def parse_dni(self, dni:str):
        self.dni = int(self.dni.split('-')[1])

    def apply(self):
        min_range, max_range = data[self.age]
        rang = range(min_range, max_range)
        return self.dni in rang

class ExactName(Filter):
    def __init__(self, name:str, guess:str):
        super().__init__()
        self.name = name
        self.guess = guess 


    def parse_name(self, name:str):
        return set(name.upper().split(' '))
        

   
    def apply(self):
        name = self.parse_name(self.name)
        guess = self.parse_name(self.guess)
        return name == guess



if __name__ == '__main__':

    filt = DniRange('25', 41686484)
    filt2 = ExactName('guido enrique', 'enrique guido')
    
    filtes = [filt, filt2]
    results = []
    for filt in filtes:
        results.append(filt.apply())

    print(results)