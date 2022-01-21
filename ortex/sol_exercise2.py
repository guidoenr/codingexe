from cgi import test
from datetime import datetime
'''
This task is to fix this code to write out a simple monthly report. The report should look professional.
The aim of the exercise is to:
- Ensure that the code works as specified including date formats
- Make sure the code will work correctly for any month
- Make sure the code is efficient
- Ensure adherence to PEP-8 and good coding standards for readability
- No need to add comments unless you wish to
- No need to add features to improve the output, but it should be sensible given the constraints of the exercise.
Code should display a dummy sales report
'''
### Do not change anything in the section below, it is just setting up some sample data
# test_data is a dictionary keyed on day number containing the date and sales figures for that day
month = "02"
test_data = {f"{x}": {"date": datetime.strptime(f"2021{month}{x:02d}", "%Y%m%d"),
                      'sales': float(x ** 2 / 7)} for x in range(1, 29)}
### Do not change anything in the section above, it is just setting up some sample data

start = test_data["1"]
end = test_data["27"]

report_template = """
Sales Report
-----------------
Report start date: {} 
Starting Value: {} 

Report end date: {} 
Total sales: {} 
"""

def DateToDisplayDate(date):
    # E.g. Monday 8th February, 2021
    return (f"""{date.strftime("%a")} {date.strftime("%d")}th {date.strftime("%B")}, {date.strftime("%Y")}""")

start["date"] = DateToDisplayDate(start["date"])
end["date"] = DateToDisplayDate(end["date"])

#print(report_template.format(start["date"], str(start["sales"]), end["date"], str(end["sales"])))

report_tmp = """
Month: {} 
Date: {}
Total sales: {}
"""

def create_report():
    total=0
    for el in test_data:
        if month == "2" and el == "29":
            print("Leap year")
        date = test_data[el]['date']
        sales = test_data[el]['sales']
        total = test_data[el]['sales'] + total
    print(report_tmp.format(month, date, total))

create_report()