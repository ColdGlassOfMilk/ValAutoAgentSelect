import subprocess
import sys
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "python"])

libraries = ['time', 'tkinter', 'pygubu', 'pyautogui', 'keyboard']

for package in libraries:
    install(package)

def install(packages):
    subprocess.call([sys.executable, "-m", "pip", "install", packages])

lib = ['time', 'tkinter', 'pygubu', 'pyautogui', 'keyboard']

for packages in lib:
    install(packages)

print('\n\n~~~~\n\nHopefully everything is updated, and is working. If not good luck figuring it out. Or just manually install the libraries yourself\n\n~~~~\n\n')