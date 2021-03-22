import os
import argparse

# arguments python
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the prefix wanted")
ap.add_argument("-d", "--directory", required=True,
	help="path to directory containing images file")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")
args = vars(ap.parse_args())

directory = args["directory"]
name = args["name"]
[os.rename(directory+f, str(name) + str(f)) for f in os.listdir(directory) 
if (f.endswith(".jpg"))]

### a revoir : les fichiers sont bien renommés mais sont déplacés dans le dossier où se situe annotation.py
