from jinja2 import Environment, FileSystemLoader
from BeautifulSoup import BeautifulSoup as bs

env = Environment(loader=FileSystemLoader('templates'),
                  extensions=['jinja2.ext.with_'])
template = env.get_template('base.html')

with open('src/test.html', 'r') as content_file:
    file_contents = content_file.read()

output_from_parsed_template = template.render(content=file_contents)
new_template = env.from_string(output_from_parsed_template)
final_output = new_template.render()

soup = bs(final_output)
pretty_final_output = soup.prettify().encode('utf-8')

with open('stage/new.html', 'wb') as fh:
    fh.write(pretty_final_output)
