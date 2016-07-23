from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('base.html')
args = {
    'content': 'Hello World!',
    'title': 'Sup'
}
output_from_parsed_template = template.render(args)

with open('www/new.html', 'wb') as fh:
    fh.write(output_from_parsed_template)
