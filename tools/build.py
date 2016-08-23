import os

from BeautifulSoup import BeautifulSoup as bs
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.with_'])
template = env.get_template('base.html')

working_directory = os.getcwd() + '/src'

if 'stage' not in os.listdir(os.getcwd()):
    os.mkdir('stage')

for i in os.listdir(working_directory):
    if i.endswith('.html'):
        with open('src/' + i, 'r') as content_file:
            file_contents = content_file.read()

        output_from_parsed_template = template.render(content=file_contents)
        new_template = env.from_string(output_from_parsed_template)
        final_output = new_template.render()

        soup = bs(final_output)
        pretty_final_output = soup.prettify().encode('utf-8')

        with open('stage/' + i, 'wb') as fh:
            fh.write(pretty_final_output)
