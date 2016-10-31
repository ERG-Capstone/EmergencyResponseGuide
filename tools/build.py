# This file is responsible for building all the files in
# the src directory and replacing the old ones in stage.

import os
import shutil

from BeautifulSoup import BeautifulSoup as bs
from jinja2 import Environment, FileSystemLoader
from sys import stdout

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
dir_list = os.listdir(working_directory)
for index, i in enumerate(dir_list):
    srci = 'src/' + i
    dsti = 'stage/' + i
    stdout.write('\r\033[92mProcessing %d of %d items...\033[0m' % (index + 1, len(dir_list)))
    stdout.flush()

    if i.endswith('.html'):
        with open(srci, 'r') as content_file:
            file_contents = content_file.read()

        # Render can fail occasionally, log filename and exception if it does
        try:
            output_from_parsed_template = template.render(content=file_contents)
        except Exception as e:
            print('\nProblem with file: %s' % i)
            print(e)
            exit()

        new_template = env.from_string(output_from_parsed_template)
        final_output = new_template.render()

        # soup = bs(final_output)
        # pretty_final_output = soup.prettify().encode('utf-8')

        with open(dsti, 'wb') as fh:
            fh.write(final_output)
    else:
        # Copy the rest of the files and directories
        if '.' not in i:
            try:
                shutil.copytree(srci, dsti)  # Is directory without "." in name
            except Exception:
                shutil.copy2(srci, dsti)  # Is actually a file
        else:
            shutil.copy2(srci, dsti)  # Is a directory with "." in name

print('\n')  # Newline for cleanliness
