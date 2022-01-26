import csv

raw = ['Date_Time', 'Function_Name', 'Args', 'Kwargs', 'Result']
with open("loggs.csv", "w", newline='', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerow(raw)