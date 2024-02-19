import subprocess
import os


libs = [
    'tarfile',
    'threading',
    'time',
    'ctypes',
    'socket',
    'sys',
    'signal',
    'inspect',
    'os',
    'random',
    'typing',
    'logging',
    'pyfiglet'
]

for lib in libs:
    subprocess.run(['pip', 'install', lib])

    print(f'Installed: {lib}')

script_dir = r"C:\Users\littl\OneDrive\Desktop\Ryzen Raider v1.1"
script_path = os.path.join(script_dir, "Main.py")

subprocess.run(['python', script_path])