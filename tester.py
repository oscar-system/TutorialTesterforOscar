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
    print(f"Grabbing {tutorial}...")
    tut = f'''https://raw.githubusercontent.com/{tutorial["repository"]}/master/{tutorial["filename"]}.ipynb'''
    nbfilename = f"notebooks/{tutorial['filename']}.ipynb"
    with open(nbfilename, 'w') as tutfile:
        r = requests.get(tut).content.decode()
        tutfile.write(r)
    
    #finally, run the stuff
    print(f"Running {tutorial}...")
    subprocess.run(f'''jupytext --set-kernel "julia-1.10" --execute {nbfilename}''', shell=True, check=True)
    print(f"{tutorial} tested successfully!")

