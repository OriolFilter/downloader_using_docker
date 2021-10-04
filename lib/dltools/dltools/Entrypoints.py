""" This classes are used to return the corresponding entry points in case they need to be used """

class Megatools:
    base_folder = "/usr/local/bin"
    @classmethod
    def megadf(self): return f"{self.base_folder}/megadf"
    @classmethod
    def megals(self): return f"{self.base_folder}/megals"
    @classmethod
    def megaput(self): return f"{self.base_folder}/megaput"
    @classmethod
    def megamkdir(self): return f"{self.base_folder}/megamkdir"
    @classmethod
    def megaget(self): return f"{self.base_folder}/megaget"
    @classmethod
    def megarm(self): return f"{self.base_folder}/megarm"
    @classmethod
    def megadl(self): return f"{self.base_folder}/megadl"
    @classmethod
    def megareg(self): return f"{self.base_folder}/megareg"