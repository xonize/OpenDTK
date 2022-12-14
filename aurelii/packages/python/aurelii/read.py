from aurelii.utils import AureliiFile
def read_test():
    print("Running read test")
    f = AureliiFile("hello.aur")
    print(f.read())
    f.__exit__()
