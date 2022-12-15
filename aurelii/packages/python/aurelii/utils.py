class AureliiFile:
    '''A class representing a file object that has both read and write methods.'''

    def __init__(self, fpath) -> None:
        # makes file if does not exist to avoid errors on the reading of file.
        try:
            with open(fpath, 'x', encoding="utf-8") as _:
                pass
        except FileExistsError:
            pass
        finally:
            pass

        f = open(fpath, "r", encoding="utf-8")
        self.readc = f.read()
        f.close()
        self.fwrite = open(fpath, "a", encoding="utf-8")
        self.readindex = 0
        self.fpath = fpath

    def read(self, mode="lines", **kwargs):
        '''Reads from file. Default mode is lines, but can be specified as line.\n
        Returns a list of strings with stripped newlines with default mode (lines) or a string representing the line.'''
        if mode == "lines":
            return self.readc.splitlines()
        if mode == "line":
            line = kwargs.get("line")
            c = self.read("lines")
            if line is not None:
                self.readindex = line
                try:
                    return c[line]
                except IndexError as e:
                    print("Error! Line index out of range!")
                    print(e)
                    exit()
                
            self.readindex += 1
            if self.readindex >= len(self.readc.splitlines()):
                self.readindex = len(self.readc.splitlines()-1)
            return c[self.readindex]

    def write(self, text: str):
        '''Writes to file and adds a trailing newline.'''
        self.fwrite.write(text + "\n")
        # to update the read store
        self.readc = self.readc + text + "\n"

    def __exit__(self, exception_type, exception_value, exception_traceback):
        # print(exception_type)
        # print(exception_value)
        # print(exception_traceback)
        self.fwrite.close()
