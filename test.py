from main import Memoire

class Bop_it(Memoire):

    def record(self):
        self.record = 3
        print(self.record)
        return self.record
        
    def record2(self):
        print(self.record)

    

Bop_it.record(Memoire)
Bop_it.record2(Memoire)

