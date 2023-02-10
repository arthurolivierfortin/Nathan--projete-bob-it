import machine
import utime
import random
from Memoire import Memoire



dicti = {"pin" : 0, "score" : 0, "reponse" : 0, "debut" : False, "gameover" : False, "record" : 0, "lumiere" : {"pin13" : 16, "pin14" : 17, "pin15" : 18}}
debuter_partie11 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
led_raspberry25 = machine.Pin(25, machine.Pin.OUT) #led_raspberry pi
led_raspberry25.value(1)
debuter_partie11.value(0)


while True:
    if dicti["debut"] == True: 
        while dicti["gameover"] == False:
            def hasard(dicti):
                led_pin12 = machine.Pin(12, machine.Pin.OUT)
                led_pin12.value(1) #led indiquant qu<une partie est en jeu
                
                pin = ['pin13', 'pin14', 'pin15']
                import random
                x = random.randint(0, 2)
                dicti["reponse"] = pin[x]

                
            def timer(dicti):
                lumiere_pin15 = machine.Pin(18, machine.Pin.OUT) #bouton pin
                lumiere_pin14 = machine.Pin(17, machine.Pin.OUT)
                lumiere_pin13 = machine.Pin(16, machine.Pin.OUT)
                bouton_pin15 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN) #bouton pin
                bouton_pin14 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
                bouton_pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
                led_pin12 = machine.Pin(12, machine.Pin.OUT) #led_pin12
                 #led_raspberry pi

                arret = False
                sec = 3
                
                utime.sleep(1)
                print(dicti["reponse"])
                no_pin = dicti["lumiere"][dicti["reponse"]]
                print(no_pin)
                machine.Pin(no_pin, machine.Pin.OUT).value(1)
                
                while sec > 0 and arret != True:
                    if bouton_pin15.value() or bouton_pin14.value() or bouton_pin13.value():
                        if bouton_pin15.value():
                            led_pin12.value(0) # 1 pour que la lumiere s'allume)
                            
                            print('x')
                            utime.sleep(0.25)
                            dicti["pin"] = "pin15"
                            machine.Pin(no_pin, machine.Pin.OUT).value(0)
                            arret = True

                        
                        if bouton_pin14.value():
                            led_pin12.value(0.25) # 1 pour que la lumiere s'allume)
                            
                            print('x')
                            utime.sleep(1)
                            dicti["pin"] = "pin14"
                            machine.Pin(no_pin, machine.Pin.OUT).value(0)
                            arret = True

                        
                        if bouton_pin13.value():
                            led_pin12.value(0.25) # 1 pour que la lumiere s'allume)
                            
                            print('x')
                            utime.sleep(1)
                            dicti["pin"] = "pin13"
                            machine.Pin(no_pin, machine.Pin.OUT).value(0)
                            arret = True

                    else:
                        
                        print(sec)
                        utime.sleep(0.25)
                        sec -= (0.25 + (0.01*int(dicti["score"])))
                    

                led_pin12.value(0) # 1 pour que la lumiere s'allume)
                
                if sec == 0:
                    print('game over : temps ecoule')
                    print(f"score : {dicti["score"]}")
                    dicti["gameover"] = True
                    dicti["debut"] = False
                    if dicti["score"] > dicti["record"]:
                        dicti["record"] = dicti["score"]
                        Memoire.ecrire_memoire_txt(dicti["record"])
                        print(f"NOUVEAU RECORD : {dicti["record"]}")
                    dicti["score"] = 0
                    led_off()

            def correction(dict):
                if dicti["reponse"] == dicti["pin"]:
                    print('correct')
                    dicti["score"] += 1
                else:
                    if dicti["gameover"] != True:
                        print('game over : mauvais bouton')
                        print(dicti["pin"], dicti["reponse"])
                        print(f"score : {dicti["score"]}")
                        dicti["gameover"] = True
                        dicti["debut"] = False
                        
                        if dicti["score"] > dicti["record"]:
                            dicti["record"] = dicti["score"]
                            print(f"NOUVEAU RECORD : {dicti["record"]}")
                            Memoire.ecrire_memoire_txt(dicti["record"])
                        dicti["score"] = 0
                    led_off()
                    
            def led_off():
                machine.Pin(18, machine.Pin.OUT).value(0)
                machine.Pin(17, machine.Pin.OUT).value(0)
                machine.Pin(16, machine.Pin.OUT).value(0)
                    
                    
            hasard(dicti)
            timer(dicti)
            correction(dicti)

    def debuter_partie(dicti):
            arret = False
            if dicti["record"] == 0:    
                dicti["record"] = (int(Memoire.lire_memoire_txt()))
            print("pret a debuter")
            print(f"record : {dicti["record"]}")
            while arret != True:
                if debuter_partie11.value():
                    print("%%%")
                    dicti["debut"] = True
                    arret = True
                utime.sleep(0.5)
            depart = False
            

    if dicti["debut"] == False:
        if dicti["gameover"] == True:
            dicti["gameover"] = False
        debuter_partie(dicti)
