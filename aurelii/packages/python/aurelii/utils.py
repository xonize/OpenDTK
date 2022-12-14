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

        f = open(fpath, "rb")
        self.readc:bytes = f.read()
        f.close()
        self.fwrite = open(fpath, "ab")

        self.readindex = 0
    
    def read(self, mode="lines", **kwargs):
        if mode == "lines":
            return self.readc.decode().splitlines()
        elif mode == "line":
            line = kwargs.get("line")
            c = self.read("lines")
            if line is not None:
                self.readindex = line
                return c[line]
            else:
                return c[self.readindex]
    
    def write(self, text:str):
        et = text.encode()
        print(et)
        self.fwrite.write(et)
    
    def __exit__(self):
        self.fwrite.close()
    
