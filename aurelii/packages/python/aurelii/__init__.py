'''Aurelii file parsing package'''
import aurelii.textmode.read
import aurelii.textmode.write
from aurelii.utils import AureliiFile
def readme():
    '''Returns readme of the python package.'''
    with open('README.rst', 'r', encoding='utf-8') as f:
        return f.read()

def info():
    '''Prints info for Aurelii package'''
    print("This is the Python package for Aurelii.")

def aopen(fpath:str):
    '''Returns an AureliiFile with read and write modes.'''
    f = AureliiFile(fpath)
    return f
