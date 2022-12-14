from aurelii.utils import AureliiFile
def write_test():
    print("Running write test")
    f = AureliiFile("hello.aur")
    f.write("this is a test 0109.7 true False")
    f.write("test line 2\nand three xd")
    f.__exit__()
