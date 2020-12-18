import jinja2 as j2
f = open('tmpl.txt', 'r')
tmpl = f.read()
f.close()
template = j2.Template(tmpl)
print(template.render(name='MEDVED'))
