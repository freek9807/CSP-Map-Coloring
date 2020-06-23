from RESTCountries import RESTCountries
from CSP import CSP
from Map import Map

col = ["#ffff00","#09cd00","#f71200","#0005e0","#c526ff","#800080","#FFFF00","#00FF00","#FF00FF"]

borders = RESTCountries.RESTCountries()

solution = CSP.CSP(col)

sol = solution.csp_solution(borders.getAdjMatrix(),borders.getAdjMatrix())

code2name = borders.getCode2name()

map = Map.Map()

traspose = { code2name[key] : value for (key,value) in sol.items() }

text_file = open("index.html", "wt")

n = text_file.write(map.draw_html(traspose))

text_file.close()

print("Check index.html! :-)")