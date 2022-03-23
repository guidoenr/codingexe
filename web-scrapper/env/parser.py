import argparse
from datetime import datetime

desc = """[SCRAP-THE-PEOPLE] - A tool to scrap the people data from the web
"""

def init_parser():
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "-n", "--name",
        help="The person name (e.g 'John Thomas Fredderick Gonzales)", 
        required=True,
    )
    parser.add_argument(
        "-a", "--age",
        help="The person ESTIMATED age (e.g 24)", 
        required=True,
    )
    args = parser.parse_args()
    return args
