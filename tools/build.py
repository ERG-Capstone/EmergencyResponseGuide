# This file is responsible for building all the files in
# the src directory and replacing the old ones in stage.

import os
import shutil

from BeautifulSoup import BeautifulSoup as bs
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.with_'])
template = env.get_template('base.html')

working_directory = os.getcwd() + '/src'

# Create stage directory if it does not exist
if 'stage' not in os.listdir(os.getcwd()):
    os.mkdir('stage')
else:
    shutil.rmtree('stage')
    os.mkdir('stage')

# Template-ize each html in src and copy it to stage
for i in os.listdir(working_directory):
    srci = 'src/' + i
    dsti = 'stage/' + i
    if i.endswith('.html'):
        with open(srci, 'r') as content_file:
            file_contents = content_file.read()

        output_from_parsed_template = template.render(content=file_contents)
        new_template = env.from_string(output_from_parsed_template)
        final_output = new_template.render()

        soup = bs(final_output)
        pretty_final_output = soup.prettify().encode('utf-8')

        with open(dsti, 'wb') as fh:
            fh.write(pretty_final_output)
    else:
        if '.' not in i:
            try:
                shutil.copytree(srci, dsti)
            except Exception:
                shutil.copy2(srci, dsti)
        else:
            shutil.copy2(srci, dsti)
