import sys
import requests
import subprocess

print(sys.argv)

repo = f"{sys.argv[1]}/{sys.argv[2]}"
filename = sys.argv[3]
tut = f'''https://raw.githubusercontent.com/{repo}/master/{filename}.ipynb'''
nbfilename = f"notebooks/{filename}.ipynb"
with open(nbfilename, 'w') as tutfile:
    r = requests.get(tut).content.decode()
    tutfile.write(r)

#finally, run the stuff
print(f"Running {repo}/{filename}...")
subprocess.run(f'''jupytext --set-kernel "julia-1.10" --execute {nbfilename}''', shell=True, check=True)
print(f"{repo}/{filename} tested successfully!")

