from jinja2 import Template
f = open('weather.log', 'r')
w = f.readlines()
f.close()

weather = []
for i in w:
    weather.append(i[:25].strip().split())
    
        
#print(weather)
html = open('weth.txt').read()
template = Template(html)
render = template.render(weather = weather)

f = open('weather.html', 'w')
f.write(render)
f.close()
