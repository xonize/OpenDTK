'''Read package for Aurelii'''
from aurelii.utils import AureliiFile
def read_test():
    '''Random test'''
    print("Running read test")
    f = AureliiFile("hello.aur")
    print(f.read())
    f.__exit__(None, None, None)    
