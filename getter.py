import os
import requests
import yaml

url = '''https://raw.githubusercontent.com/oscar-system/oscar-website/gh-pages/_data/examples.yml'''

yamlfile = requests.get(url).content

yamlcontent = yaml.safe_load(yamlfile)

try:
    os.mkdir("notebooks")
except Exception as e:
    pass
    #print(e)

outstring=""

for tut in yamlcontent:
    outstring += f"""'{tut["repository"]} {tut["filename"]}', """

outstring = outstring[0:-2]

print(outstring)
