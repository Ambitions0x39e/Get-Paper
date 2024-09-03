"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['src/central.py', 'src/write_pdf.py', 'src/info.py', 'assets/icon.icns']
OPTIONS = {
    'iconfile':'assets/icon.icns',
    'plist': {
        'CFBundleName': 'Get Paper',     
        'CFBundleDisplayName': 'Get Paper', 
        'CFBundleVersion': '1.0.1',      
        'CFBundleIdentifier' : 'Get Paper', 
        'NSHumanReadableCopyright': 'Copyright © 2024 Ambitions0x39e. All rights reserved.', 
        'includes': ['sys', 'time', 'os', 'PySide6']
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)