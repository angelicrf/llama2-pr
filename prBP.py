import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(clientip)-15s %(user)-8s %(message)s:')

project_name = 'DLPr'

required_files = [
    ".github/documents/.gitstore",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/prutils/__init__.py",
    f"src/{project_name}/prconfig/__init__.py",
    f"src/{project_name}/prconfig/prconfiguration.py",
    f"src/{project_name}/prpipeline/__init__.py",
    f"src/{project_name}/prentity/__init__.py",
    f"src/{project_name}/constvariables/__init__.py",
    "prconfig/prconfig.yaml",
    "dataversioncontrol.yaml",
    "devenvs.yaml",
    "requirements.txt",
    "devopsetup.py",
    "pipelines/stages.ipynb",
    "prjectlayouts/index.html"
]


for stPath in required_files:
    stPath = Path(stPath)
    dirName, fileName = os.path.split(stPath)


    if dirName !="":
        os.makedirs(dirName, exist_ok=True)
        logging.info(f"Creating directory; {dirName} for the file: {fileName}")

    if (not os.path.exists(stPath)) or (os.path.getsize(stPath) == 0):
        with open(stPath, "w") as f:
            pass
            logging.info(f"Creating empty file: {stPath}")


    else:
        logging.info(f"{stPath} is already exists")