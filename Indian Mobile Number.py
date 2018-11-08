import re
import random
import string
import csv

exp = r"^(?:0|\+91)?[789]\d{9}$"

def validateNumber(number):
    number.replace("-","").replace(" ","")
    if re.search(exp, number):
        return True
    else:
        return False

def getNumber():
    number = ""
    for i in range(10):
        number = number + random.choice(string.digits)
    return number

with open("numbers.csv",'w') as csv_file:
    csv_file.write("Mobile Numbers" + "\n")
totalnumbers = 0
while totalnumbers < 200:
    number = getNumber()
    if validateNumber(number):
        totalnumbers = totalnumbers + 1
        with open("numbers.csv",'a') as csv_file:
            csv_file.write(number[:5] + "\n")
