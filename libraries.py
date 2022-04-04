import os


def update():
    os.system("pip install --upgrade pip")
    os.system("pip freeze > requirements.txt")
    requirements = open('requirements.txt', 'r')
    for requirement in requirements.read().split('\n'):
        library = requirement.split("==")
        os.system(f"pip install {library[0]} --upgrade")
    os.system("pip freeze > requirements.txt")

