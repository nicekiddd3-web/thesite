from setuptools import setup

APP = ['NiceKiddnet-winrepair.py'] # Replace 'nicekiddnet.py' with the actual name of your script
DATA_FILES = []
OPTIONS = {
    # 'iconfile': 'appicon.icns', # Comment this line out or delete it
    'argv_emulation': True,
    'packages': ['tkinter'], # Ensure tkinter is included
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)