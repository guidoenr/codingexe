from sympy import per
from env import parser
from scrappers import *



if __name__ == '__main__':
    args = parser.init_parser()
    name = args.name
    age = args.age

    dateas_scrp = Dateas(name, age)
    dateas_scrp.find_data()