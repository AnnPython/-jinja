import jinja2 as j2
name = ['DED', 'MEDVED', 'NE_MEDVED', 'MEDVED-1', 'MEDVED-2']
template = j2.Template(open('tmpl1.txt').read())
print(template.render(medveds = name))
