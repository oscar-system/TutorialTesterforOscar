import os
import requests
import yaml
import subprocess

url = '''https://raw.githubusercontent.com/oscar-system/oscar-website/gh-pages/_data/examples.yml'''

yamlfile = requests.get(url).content

yamlcontent = yaml.safe_load(yamlfile)

try:
    os.mkdir("notebooks")
except Exception as e:
    print(e)

for tutorial in yamlcontent:
    tut = f'''https://raw.githubusercontent.com/{tutorial["repository"]}/master/{tutorial["filename"]}.ipynb'''
    nbfilename = f"notebooks/{tutorial['filename']}.ipynb"
    with open(nbfilename, 'w') as tutfile:
        r = requests.get(tut).content.decode()
        tutfile.write(r)
    
    #finally, run the stuff
    subprocess.run(f"jupyter nbconvert --to notebook --execute {nbfilename}", shell=True, check=True)

    #for testing...
    #break after the first notebook
    break

