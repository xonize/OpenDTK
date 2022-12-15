'''The write module for Aurelii'''
from aurelii.utils import AureliiFile
def write_test():
    '''Random test for write'''
    print("Running write test")
    f = AureliiFile("hello.aur")
    f.write("this is a test 0109.7 true False")
    f.write("test line 2\nand three xd")
    f.__exit__(None, None, None)
