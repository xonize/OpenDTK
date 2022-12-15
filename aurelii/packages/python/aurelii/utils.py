class AureliiFile:
    def __init__(self, fpath) -> None:
        # makes file if does not exist to avoid errors on the reading of file.
        try:
            with open(fpath, 'x') as _:
                pass
        except FileExistsError:
            pass
        finally:
            pass

        f = open(fpath, "r", encoding="utf-8")
        self.readc:bytes = f.read()
        f.close()
        self.fwrite = open(fpath, "a", encoding="utf-8")
        self.readindex = 0
    
    def read(self, mode="lines", **kwargs):
        if mode == "lines":
            return self.readc.splitlines()
        elif mode == "line":
            line = kwargs.get("line")
            c = self.read("lines")
            if line is not None:
                self.readindex = line
                return c[line]
            else:
                self.readindex += 1
                return c[self.readindex]
    
    def write(self, text:str):
        self.fwrite.write(text)
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        print(exception_type)
        print(exception_value)
        print(exception_traceback)
        self.fwrite.close()
    
