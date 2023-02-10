import utime

class Memoire:

    def reset_memoire():
        Memoire_txt = open("Memoire.txt", "w")
        Memoire_txt.write("0")
        Memoire_txt.close
        
        
    def ecrire_memoire_txt(record=0):
        
        Memoire_txt = open('Memoire.txt')
        record_memoire = int(Memoire_txt.read())
        #print(f"{record_memoire} record memoire 1")
        Memoire_txt.close()
        #print("***")
        #print(f"{record} rec")

        if record > record_memoire:
            #print("&&&")
            Memoire_txt2 = open("Memoire.txt", "w")
            Memoire_txt2.write(f"{record}")
            Memoire_txt2.close
        
        

    
    def lire_memoire_txt():    
        Memoire_txt = open('Memoire.txt', "r")
        record_memoire = Memoire_txt.read()
        Memoire_txt.close()
        return record_memoire
        #print(f"{record_memoire} memoire lu")

#Memoire.ecrire_memoire_txt(3)
#utime.sleep(5)
#Memoire.lire_memoire_txt()
#Memoire.lire_memoire_txt()
#Memoire.reset_memoire()