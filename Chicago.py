try:
    from colorama import Fore,Back,Style,init
except:
    print("No Colorama ;(")
    exit()
import os,sys,time,platform,random,keyboard
init()
hrac = 0
ai = 0





def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def logo():
    clear()
    print(f"""{Fore.CYAN}
   ________    _                      
  / ____/ /_  (_)________ _____ _____ 
 / /   / __ \/ / ___/ __ `/ __ `/ __ \\
/ /___/ / / / / /__/ /_/ / /_/ / /_/ /
\____/_/ /_/_/\___/\__,_/\__, /\____/ 
                        /____/      {Style.RESET_ALL}""")
    

        
        
        
def getfinalvalue():
    list = []
    for x in range(3):
        list.append(getnumbers())       
    return list, sum(list)
        
        
        
        
def getnumbers():
    number = random.randint(1,6)
    
    if number == 1:
        number = 100
    elif number == 6:
        number = 60
    return number
        

def animatedtext(text, color=Fore.BLUE):
    temp = 0
    temp1 = ""
    speed = 0.015
    text = list(text)
    text.append(" ")
    print(color,end="\r")
    for x in text:
        print(f"{temp1}    ",end="\r")
        if temp > 100:
            temp = 0
            temp1 = ""
            print("")
        temp1 += x
        temp += 1
        time.sleep(speed)
        if keyboard.is_pressed(" "):
            speed = 0
    print(Style.RESET_ALL)
        


while True:
    logo()
    animatedtext(f"Každý hráč hází třikrát za sebou, má tři kostky. Snaží se získat co nejvíce bodů, přičemž jednička jeza 100, šestka za 60, ostatní čísla mají svou hodnotu. Po každém hodu může hráč kostky s jejichž hodnotou je spokojen nechat ležet nebo házet se všemi. Dosažný počet bodů se zapíše, hráč který má po sedmi kolech nejvíce bodů, vyhrál. {Style.RESET_ALL}",Fore.RED)
    ans = input("Chceš začít ? (Y/N): ")
    if ans == "Y" or ans == "y":
        break
    elif ans == "N" or ans == "n":
        print("OK :(")
        exit()
        
animatedtext(f"Dobře Budeš Hrát Proti AI bo proč ne?",Fore.GREEN)
while True:
    while True:
        animatedtext(f"Nastav Obtížnost (Easy,Normal,Hard)",Fore.GREEN)
        ans = input("")
        if ans == "Easy":
            diffnum = 0
            break
        elif ans == "Normal":
            diffnum = 60
            break
        elif ans == "Hard":
            diffnum = 120
            break

        for x in range(3,0,-1):
            print(f"Starting In {x}",end="\r")
            time.sleep(1)

    def bar():
        logo()
        print(f"PLAYER:{hrac} AI: {ai}")
        if ai > hrac:
            print(Fore.RED+"*"*15,f"KOLO {kolo}/7","*"*15,Style.RESET_ALL)
        else:
            print(Fore.GREEN+"*"*15,f"KOLO {kolo}/7","*"*15,Style.RESET_ALL)
    for kolo in range(1,8):
        for x in range(3):
            bar()
            print("Hraješ TY")
            numlist, number = getfinalvalue()
            print(numlist)
            print(number + hrac)
            animatedtext(f"Libí se ti tyto kostky? (Y/N) ",Fore.RED)
            ans = input("")
            if ans == "Y" or ans == "y":
                break
        hrac += number
        for x in range(3):
            bar()
            print("Hraje AI")
            numlist, number = getfinalvalue()
            if ai > hrac or number > diffnum:
                break
            time.sleep(0.5)
        ai += number
            
    logo()
    animatedtext(f"Hodnota AI: {ai}",Fore.RED)
    animatedtext(f"Tvoje Hodnota: {hrac}",Fore.GREEN)
    if ai > hrac:
        animatedtext(f"YOU LOSE",Fore.RED)
    elif ai == hrac:
        animatedtext(f"DRAW",Fore.YELLOW)
    else:
        animatedtext(f"YOU WIN",Fore.GREEN)
    
    
    
    
    
    
    animatedtext(f"Chceš znova hrát? (Y/N) ")
    ans = input("")
    if ans == "N" or ans == "n":
        break
    ai = 0
    hrac = 0

logo()
animatedtext("Děkuji za hraní Chicago")
animatedtext("Dělal Jsem to 3.5h")






