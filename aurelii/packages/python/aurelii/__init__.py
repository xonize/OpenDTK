import aurelii.read
import aurelii.write
def readme():
    '''Returns readme of the python package.'''
    with open('README.rst', 'r', encoding='utf-8') as f:
        return f.read()

def info():
    '''Prints info for Aurelii package'''
    print("This is the Python package for Aurelii.")

