import sys
import csv
from CSP import CSP
from Map import Map

col = ["#ffff00","#09cd00","#f71200","#0005e0","#c526ff","#800080","#FFFF00","#00FF00","#FF00FF"]

file = ""
data = ""

solution = CSP.CSP(col)

if len(sys.argv) > 1 and sys.argv[1] == "it":
    file ="Map/Italy_Regions_Blank.svg"
    data ="data/italia.csv"
elif len(sys.argv) > 2:
    file =sys.argv[1]
    data =sys.argv[2]
else:
    if len(sys.argv) > 1 and sys.argv[1] != "wd":
        raise NameError(sys.argv[1] + " isn't a valid arg!")
    file ="Map/world.svg"
    data ="data/world.csv"

with open(data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = {}
    for row in csv_reader:
        data[row[0]] = []
        for i in range(1,len(row)):
            data[row[0]].append(row[i])

sol = solution.csp_solution(data,data)


map = Map.Map(file)

text_file = open("index.html", "wt")

n = text_file.write(map.draw_html(sol))

text_file.close()

print("Check index.html! :-)")