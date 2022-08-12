import re

class Config:
    def __init__(self, filename="cfg.txt"):
        self.dict_info = dict()
        self.filename = filename

    def read(self):
        f = open(self.filename)
        for line in f:
            line = line.replace("\n", "")
            #return re.split(" = ", line)[0]
            self.dict_info.update({re.split(" = ", line)[0] : re.split(" = ", line)[1]})

    def get(self):
        self.read()
        return self.dict_info
