import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
template = env.get_template('base.html')
output_from_parsed_template = template.render(content='Hello!')

with open('www/new.html', 'wb') as fh:
    fh.write(output_from_parsed_template)
