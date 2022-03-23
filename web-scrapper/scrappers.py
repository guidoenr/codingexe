from bs4 import BeautifulSoup
import requests
import cfscrape
import filters

scraper = cfscrape.create_scraper()




class Person():
    def __init__(self, name:str, dni:str):
        self.name = name.upper()
        self.dni = dni
        self.age = 'not setted'
        self.possible_emails = []
        self.address = 'not found'
    
  

class Scrapper():
    def __init__(self, name:str, age:str):
        self.name = name
        self.age = age
        self.best_choices = []

    def find_data(self):
        ...


class Dateas(Scrapper):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.url = 'https://dateas.com/es/consulta_cuit_cuil?page={page}&name={name}&cuit=&tipo=personas-fisicas'


    def best_guess(self, name_guess:str, dni_guess:int):
        minn = data[self.age][0]
        maxx = data[self.age][1]
        dnis_range = range(minn, maxx)
        name_to_match = self.parse_person_name(self.name)
        name_input = self.parse_person_name(name_guess)
        len_input = len(name_input)
        len_match = len(name_to_match)
        if len_input == len_match:
            if dni_guess in dnis_range:
                if name_to_match.intersection(name_input) == len_input:
                    return 


    def find_data(self):
        parsed_name = self.name.replace(' ', '+')
        url = self.url.format(name=parsed_name, page=0)
        response = scraper.get(url)
        html = response.content
        soup = BeautifulSoup(html, 'lxml')
        tags = soup.find_all('td')

        clean = [tag for tag in tags if tag.text != 'Ver Más']
        dnis = [tag for tag in clean if tag.text[0].isdigit()]
        names = [tag for tag in clean if not tag.text[0].isdigit()]
        
        for name, dni in zip(names, dnis):
            parsed_dni = self.parse_dni(dni.text)
            best_guess = self.best_guess(name.text, parsed_dni)
            if best_guess:
                person_guess = Person(name.text, dni.text)
                self.best_choices.append(person_guess)
        for p in (self.best_choices):
            print(p.name, p.dni)


            
if __name__ == '__main__':
    asd = range(40000, 42000)
    if 41706212 in asd:
        print('in range')