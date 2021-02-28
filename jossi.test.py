import tkinter as tk
import time
from datetime import date
from time import * 
import os

x = date.today()
d = x.weekday()
day =["måndagar", "tisdagar", "onsdagar", "torsdagar", "fredagar", "lördagar", "söndagar"]

#import winsound
#frequency = 800  # Set Frequency To 2500 Hertz
#duration = 10  # Set Duration To 1000 ms == 1 second

#Textfunktion, en bokstav i taget
def slow(text):
    for letters in text:
#        winsound.Beep(frequency, duration)
        print(letters, end = "") 
        sleep(0.08) 


while True:
    slow("Hallå? \n")
    sleep(1)
    slow("Hallå... Är det någon där...?\n")
    answer = input("")
    slow("Åh hej! Kände av din närvaro! ...")
    sleep(1)
    slow("\nVem är du? ... Jag menar ... vad heter du?")
    name = input("\n")
    sleep(1)
    slow("Hej {}! ".format(name)) 
    sleep(1)
    slow("Brukar du hänga här på ")
    slow(day[d])
    slow("?\n")
    answer = input("")
    sleep(1)
    slow("Jag borde gå hit oftare... ")
    sleep(1)
    slow("Vad fin du är förresten...\n")
    answer = input("")
    sleep(1)
    slow("Vad är ditt favoritplagg?")
    plagg = input("\n")
    sleep(1)
    slow("Mmmmm {}!" .format(plagg)) 
    slow(" Kan föreställa mig att du vill ha dom riktigt tighta!\n") 
    sleep(1.5)
    print(" HAHA")
    sleep(0.1)
    print(" HAHA")
    sleep(0.1)
    print(" HAHA")
    sleep(0.1)
    print(" HAHA")
    sleep(0.1)
    print(" HAHA")
    sleep(0.1)
    print(" HAHA")
    sleep(0.1)
    print(" HAHA")
    sleep(0.1)
    print(" HAHA")
    sleep(2)
    slow("Jag vill ge dig nåt...") 
    answer = input("\n")
    print("        .-~~-.--.")
    sleep(0.2)
    print("       :         )")
    sleep(0.2)
    print(" .~ ~ -.\       /.- ~~ .")
    sleep(0.2)
    print(" >       `.   .'       < ")
    sleep(0.2)
    print("(         .- -.         )")
    sleep(0.2)
    print(" `- -.-~  `- -'  ~-.- -'")
    sleep(0.2)
    print("   (        :        )           _ _ .-:")
    sleep(0.2)
    print("    ~--.    :    .--~        .-~  .-~  }")
    sleep(0.2)
    print("        ~-.-^-.-~ \_      .~  .-~   .~")
    sleep(0.2)
    print("                 \ \'     \ '_ _ -~")
    sleep(0.2)
    print("                  `.`.    //")
    sleep(0.2)
    print("         . - ~ ~-.__`.`-.//")                  
    sleep(0.2)
    print("     .-~   . - ~  }~ ~ ~-.~-.")                  
    sleep(0.2)
    print("   .' .-~      .-~       :/~-.~-./:")                  
    sleep(0.2)
    print("  /_~_ _ . - ~                 ~-.~-._")                  
    sleep(0.2)
    print("                                   ~-.<")  
    slow("Blev du glad nu?") 
    answer = input("\n")
    sleep(1)
    slow("Känns som vi har nåt, du och jag. Känner du samma som jag?") 
    while True:
        answer = input("\n")
        if answer.lower().strip() == "ja":
            root = tk.Tk()
            root.title('JAG <3 <3 <3!!!!!!!')
            image1 = tk.PhotoImage(file="kar1.gif")
            tk.Label(root, image=image1).pack()
            root.mainloop()
            root = tk.Tk()
            root.title('ÄR <3 <3 <3!!!!!!!')
            image2 = tk.PhotoImage(file="kar3.gif")
            tk.Label(root, image=image2).pack()
            root.mainloop()
            root = tk.Tk()
            root.title('KÄR <3 <3 <3!!!!!!!')
            image3 = tk.PhotoImage(file="kar2.gif")
            tk.Label(root, image=image3).pack()
            root.mainloop()
            break
        if answer.lower().strip() == "nej":
            root = tk.Tk()
            root.title('=´( Neeeeeeej!')
            image4 = tk.PhotoImage(file="ledsen.gif")
            tk.Label(root, image=image4).pack()
            root.mainloop()
            break
        else:
            slow("Jag förstod inte. Kan du svara ja eller nej? Känner du samma som jag... att vi hör ihop?")
    break

print("THE END. GAME OVER")
exit()

