import os
import requests
import yaml

url = '''https://raw.githubusercontent.com/oscar-system/oscar-website/gh-pages/_data/examples.yml'''

yamlfile = requests.get(url).content

yamlcontent = yaml.safe_load(yamlfile)

outstring=""

for tut in yamlcontent:
    splstring = tut["repository"].split('/')
    outstring += f"""'{splstring[0]} {splstring[1]} {tut["filename"]}', """

outstring = outstring[0:-2]

print(outstring)
