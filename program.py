from PIL import Image
import os
import random

#Create a letter object including all the info we need
class Character:
    def __init__(self, cap, height, path):
        self.path = path
        self.cap = cap
        self.im = Image.open(self.path)
        if self.cap == 0:
            self.width = round(self.im.width * 1)
            self.height = round(self.im.height * 1)
            self.im = self.im.resize((round(self.im.width * 1), round(self.im.height *1)))
        else:
            self.width = self.im.width
            self.height = self.im.height
        if self.im.mode != 'RGB':
            self.im = self.im.convert('RGB')

    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height  

#Function to call when checking what letter or symbol we are reading
def letterCheck(cool):
    match cool:
        case "a":
            return leta
        case "b":
            return letb
        case "c":
            return letc
        case "d":
            return letd
        case "e":
            return lete
        case "f":
            return letf
        case "g":
            return letg
        case "h":
            return leth
        case "i":
            return leti
        case "j":
            return letj
        case "k":
            return letk
        case "l":
            return letl
        case "m":
            return letm
        case "n":
            return letn
        case "o":
            return leto
        case "p":
            return letp
        case "q":
            return letq
        case "r":
            return letr
        case "s":
            return lets
        case "t":
            return lett
        case "u":
            return letu
        case "v":
            return letv
        case "w":
            return letw
        case "x":
            return letx
        case "y":
            return lety
        case "z":
            return letz
        case "A":
            return capA
        case "B":
            return capB
        case "C":
            return capC
        case "D":
            return capD
        case "E":
            return capE
        case "F":
            return capF
        case "G":
            return capG
        case "H":
            return capH
        case "I":
            return capI
        case "J":
            return capJ
        case "K":
            return capK
        case "L":
            return capL
        case "M":
            return capM
        case "N":
            return capN
        case "O":
            return capO
        case "P":
            return capP
        case "Q":
            return capQ
        case "R":
            return capR
        case "S":
            return capS
        case "T":
            return capT
        case "U":
            return capU
        case "V":
            return capV
        case "W":
            return capW
        case "X":
            return capX
        case "Y":
            return capY
        case "Z":
            return capZ
        case "!":
            return markexe
        case "?":
            return que
        case ",":
            return com
        case ".":
            return per
        case ")":
            return per
        case "-":
            return das
        case '{':
            return dquo1
        case "}":
            return dquo2
        case "[":
            return quo1
        case "]":
            return quo2
        case "'":
            return quo2
        case ":":
            return col
        case ";":
            return sem
        case "0":
            return c0
        case "1":
            return c1
        case "2":
            return c2
        case "3":
            return c3
        case "4":
            return c4
        case "5":
            return c5
        case "6":
            return c6
        case "7":
            return c7
        case "8":
            return c8
        case "9":
            return c9

#Function to call when we need to see if we have a special character that gets moved down extra, defaults to 0
def checkSpecials(cool1):
    if setting == 0:
        match cool1:
            case "q":
                return 6
            case "p":
                return 7
            case "y":
                return 5
            case "g":
                return 6
            case "j":
                return 3
            case '{':
                return -15
            case "}":
                return -15
            case "[":
                return -15
            case "]":
                return -15
            case "'":
                return -15
            case ",":
                return 12
            case _:
                return 0
    if setting == 1:
        match cool1:
            case "q":
                return 12
            case "p":
                return 11
            case "y":
                return 10
            case "g":
                return 13
            case "j":
                return 3
            case '{':
                return -15
            case "}":
                return -15
            case "[":
                return -15
            case "]":
                return -15
            case "'":
                return -15
            case ",":
                return 12
            case _:
                return 0
    if setting == 2:
        match cool1:
            case "q":
                return 12
            case "p":
                return 9
            case "y":
                return 15
            case "g":
                return 14
            case "j":
                return 3
            case '{':
                return -15
            case "}":
                return -15
            case "[":
                return -15
            case "]":
                return -15
            case "'":
                return -15
            case ",":
                return 12
            case "-":
                return -12
            case "L":
                return 5
            case _:
                return 0

#define varibles needed to work
currentx = 0
currenty = 0
spacelengthLow = 0
spacelengthHigh = 0
lineheight = 36
linewidth = 785
widthcount = 0
pageNumber = 1
setting = int(input("Chose the setting 0, 1, or 2")) 

#define the letters
if setting == 0:
    spacelengthLow = 12
    spacelengthHigh = 22
    leta = Character(0,32,"TylerHandwriting/Letter/a.jpg")
    letb = Character(0,32,"TylerHandwriting/Letter/b.jpg")
    letc = Character(0,32,"TylerHandwriting/Letter/c.jpg")
    letd = Character(0,32,"TylerHandwriting/Letter/d.jpg")
    lete = Character(0,32,"TylerHandwriting/Letter/e.jpg")
    letf = Character(0,32,"TylerHandwriting/Letter/f.jpg")
    letg = Character(0,32,"TylerHandwriting/Letter/g.jpg")
    leth = Character(0,32,"TylerHandwriting/Letter/h.jpg")
    leti = Character(0,32,"TylerHandwriting/Letter/i.jpg")
    letj = Character(0,32,"TylerHandwriting/Letter/j.jpg")
    letk = Character(0,32,"TylerHandwriting/Letter/k.jpg")
    letl = Character(0,32,"TylerHandwriting/Letter/l.jpg")
    letm = Character(0,31,"TylerHandwriting/Letter/m.jpg")
    letn = Character(0,32,"TylerHandwriting/Letter/n.jpg")
    leto = Character(0,32,"TylerHandwriting/Letter/o.jpg")
    letp = Character(0,32,"TylerHandwriting/Letter/p.jpg")
    letq = Character(0,32,"TylerHandwriting/Letter/q.jpg")
    letr = Character(0,32,"TylerHandwriting/Letter/r.jpg")
    lets = Character(0,32,"TylerHandwriting/Letter/s.jpg")
    lett = Character(0,32,"TylerHandwriting/Letter/t.jpg")
    letu = Character(0,32,"TylerHandwriting/Letter/u.jpg")
    letv = Character(0,32,"TylerHandwriting/Letter/v.jpg")
    letw = Character(0,31,"TylerHandwriting/Letter/w.jpg")
    letx = Character(0,32,"TylerHandwriting/Letter/x.jpg")
    lety = Character(0,32,"TylerHandwriting/Letter/y.jpg")
    letz = Character(0,28,"TylerHandwriting/Letter/z.jpg")
    capA = Character(18,25,"TylerHandwriting/LetterCap/Capa.jpg")
    capB = Character(19,22,"TylerHandwriting/LetterCap/Capb.jpg")
    capC = Character(17,21,"TylerHandwriting/LetterCap/Capc.jpg")
    capD = Character(19,23,"TylerHandwriting/LetterCap/Capd.jpg")
    capE = Character(15,25,"TylerHandwriting/LetterCap/Cape.jpg")
    capF = Character(18,26,"TylerHandwriting/LetterCap/Capf.jpg")
    capG = Character(14,21,"TylerHandwriting/LetterCap/Capg.jpg")
    capH = Character(14,23,"TylerHandwriting/LetterCap/Caph.jpg")
    capI = Character(16,19,"TylerHandwriting/LetterCap/Capi.jpg")
    capJ = Character(16,27,"TylerHandwriting/LetterCap/Capj.jpg")
    capK = Character(18,27,"TylerHandwriting/LetterCap/Capk.jpg")
    capL = Character(20,26,"TylerHandwriting/LetterCap/Capl.jpg")
    capM = Character(24,25,"TylerHandwriting/LetterCap/Capm.jpg")
    capN = Character(19,23,"TylerHandwriting/LetterCap/Capn.jpg")
    capO = Character(19,20,"TylerHandwriting/LetterCap/Capo.jpg")
    capP = Character(11,28,"TylerHandwriting/LetterCap/Capp.jpg")
    capQ = Character(24,23,"TylerHandwriting/LetterCap/Capq.jpg")
    capR = Character(15,20,"TylerHandwriting/LetterCap/Capr.jpg")
    capS = Character(11,27,"TylerHandwriting/LetterCap/Caps.jpg")
    capT = Character(23,22,"TylerHandwriting/LetterCap/Capt.jpg")
    capU = Character(21,24,"TylerHandwriting/LetterCap/Capu.jpg")
    capV = Character(16,22,"TylerHandwriting/LetterCap/Capv.jpg")
    capW = Character(23,22,"TylerHandwriting/LetterCap/Capw.jpg")
    capX = Character(21,23,"TylerHandwriting/LetterCap/Capx.jpg")
    capY = Character(17,25,"TylerHandwriting/LetterCap/Capy.jpg")
    capZ = Character(23,23,"TylerHandwriting/LetterCap/Capz.jpg")
    markexe = Character(5,29,"TylerHandwriting/Symbol/exe.jpg")
    que = Character(15,27,"TylerHandwriting/Symbol/que.jpg")
    com = Character(8,14,"TylerHandwriting/Symbol/com.jpg")
    per = Character(6,7,"TylerHandwriting/Symbol/per.jpg")
    das = Character(15,18,"TylerHandwriting/Symbol/das.jpg")
    dquo1 = Character(18,10,"TylerHandwriting/Symbol/dquo1.jpg")
    dquo2 = Character(19,9,"TylerHandwriting/Symbol/dquo2.jpg")
    quo1 = Character(6,9,"TylerHandwriting/Symbol/quo1.jpg")
    quo2 = Character(8,11,"TylerHandwriting/Symbol/quo2.jpg")
    sem = Character(11,27,"TylerHandwriting/Symbol/sem.jpg")
    col = Character(10,24,"TylerHandwriting/Symbol/col.jpg")
    c1 = Character(8,26,"TylerHandwriting/Numbers/1.jpg")
    c2 = Character(30,24,"TylerHandwriting/Numbers/2.jpg")
    c3 = Character(17,22,"TylerHandwriting/Numbers/3.jpg")
    c4  = Character(17,23,"TylerHandwriting/Numbers/4.jpg")
    c5 = Character(27,23,"TylerHandwriting/Numbers/5.jpg")
    c6 = Character(16,24,"TylerHandwriting/Numbers/6.jpg")
    c7 = Character(20,20,"TylerHandwriting/Numbers/7.jpg")
    c8  = Character(19,25,"TylerHandwriting/Numbers/8.jpg")
    c9 = Character(15,25,"TylerHandwriting/Numbers/9.jpg")
    c0  = Character(19,22,"TylerHandwriting/Numbers/0.jpg")
elif setting == 1:
    spacelengthLow = 1
    spacelengthHigh = 4
    leta = Character(13,12,"TylerHandwriting2/Letter/a.jpg")
    letb = Character(14,25,"TylerHandwriting2/Letter/b.jpg")
    letc = Character(12,12,"TylerHandwriting2/Letter/c.jpg")
    letd = Character(19,30,"TylerHandwriting2/Letter/d.jpg")
    lete = Character(12,13,"TylerHandwriting2/Letter/e.jpg")
    letf = Character(18,22,"TylerHandwriting2/Letter/f.jpg")
    letg = Character(12,24,"TylerHandwriting2/Letter/g.jpg")
    leth = Character(12,20,"TylerHandwriting2/Letter/h.jpg")
    leti = Character(7,17,"TylerHandwriting2/Letter/i.jpg")
    letj = Character(17,25,"TylerHandwriting2/Letter/j.jpg")
    letk = Character(16,21,"TylerHandwriting2/Letter/k.jpg")
    letl = Character(6,28,"TylerHandwriting2/Letter/l.jpg")
    letm = Character(14,10,"TylerHandwriting2/Letter/m.jpg")
    letn = Character(14,12,"TylerHandwriting2/Letter/n.jpg")
    leto = Character(12,11,"TylerHandwriting2/Letter/o.jpg")
    letp = Character(12,22,"TylerHandwriting2/Letter/p.jpg")
    letq = Character(14,25,"TylerHandwriting2/Letter/q.jpg")
    letr = Character(11,16,"TylerHandwriting2/Letter/r.jpg")
    lets = Character(8,13,"TylerHandwriting2/Letter/s.jpg")
    lett = Character(12,22,"TylerHandwriting2/Letter/t.jpg")
    letu = Character(11,13,"TylerHandwriting2/Letter/u.jpg")
    letv = Character(12,12,"TylerHandwriting2/Letter/v.jpg")
    letw = Character(15,11,"TylerHandwriting2/Letter/w.jpg")
    letx = Character(14,12,"TylerHandwriting2/Letter/x.jpg")
    lety = Character(17,27,"TylerHandwriting2/Letter/y.jpg")
    letz = Character(15,15,"TylerHandwriting2/Letter/z.jpg")
    capA = Character(18,25,"TylerHandwriting2/LetterCap/Capa.jpg")
    capB = Character(19,22,"TylerHandwriting2/LetterCap/Capb.jpg")
    capC = Character(17,21,"TylerHandwriting2/LetterCap/Capc.jpg")
    capD = Character(19,23,"TylerHandwriting2/LetterCap/Capd.jpg")
    capE = Character(15,25,"TylerHandwriting2/LetterCap/Cape.jpg")
    capF = Character(18,26,"TylerHandwriting2/LetterCap/Capf.jpg")
    capG = Character(14,21,"TylerHandwriting2/LetterCap/Capg.jpg")
    capH = Character(14,23,"TylerHandwriting2/LetterCap/Caph.jpg")
    capI = Character(16,19,"TylerHandwriting2/LetterCap/Capi.jpg")
    capJ = Character(16,27,"TylerHandwriting2/LetterCap/Capj.jpg")
    capK = Character(18,27,"TylerHandwriting2/LetterCap/Capk.jpg")
    capL = Character(20,26,"TylerHandwriting2/LetterCap/Capl.jpg")
    capM = Character(24,25,"TylerHandwriting2/LetterCap/Capm.jpg")
    capN = Character(19,23,"TylerHandwriting2/LetterCap/Capn.jpg")
    capO = Character(19,20,"TylerHandwriting2/LetterCap/Capo.jpg")
    capP = Character(11,28,"TylerHandwriting2/LetterCap/Capp.jpg")
    capQ = Character(24,23,"TylerHandwriting2/LetterCap/Capq.jpg")
    capR = Character(15,20,"TylerHandwriting2/LetterCap/Capr.jpg")
    capS = Character(11,27,"TylerHandwriting2/LetterCap/Caps.jpg")
    capT = Character(23,22,"TylerHandwriting2/LetterCap/Capt.jpg")
    capU = Character(21,24,"TylerHandwriting2/LetterCap/Capu.jpg")
    capV = Character(16,22,"TylerHandwriting2/LetterCap/Capv.jpg")
    capW = Character(23,22,"TylerHandwriting2/LetterCap/Capw.jpg")
    capX = Character(21,23,"TylerHandwriting2/LetterCap/Capx.jpg")
    capY = Character(17,25,"TylerHandwriting2/LetterCap/Capy.jpg")
    capZ = Character(23,23,"TylerHandwriting2/LetterCap/Capz.jpg")
    c1 = Character(8,26,"TylerHandwriting2/Numbers/1.jpg")
    c2 = Character(30,24,"TylerHandwriting2/Numbers/2.jpg")
    c3 = Character(17,22,"TylerHandwriting2/Numbers/3.jpg")
    c4  = Character(17,23,"TylerHandwriting2/Numbers/4.jpg")
    c5 = Character(27,23,"TylerHandwriting2/Numbers/5.jpg")
    c6 = Character(16,24,"TylerHandwriting2/Numbers/6.jpg")
    c7 = Character(20,20,"TylerHandwriting2/Numbers/7.jpg")
    c8  = Character(19,25,"TylerHandwriting2/Numbers/8.jpg")
    c9 = Character(15,25,"TylerHandwriting2/Numbers/9.jpg")
    c0  = Character(19,22,"TylerHandwriting2/Numbers/0.jpg")
    markexe = Character(5,29,"TylerHandwriting2/Symbol/exe.jpg")
    que = Character(15,27,"TylerHandwriting2/Symbol/que.jpg")
    com = Character(8,14,"TylerHandwriting2/Symbol/com.jpg")
    per = Character(6,7,"TylerHandwriting2/Symbol/per.jpg")
    das = Character(15,18,"TylerHandwriting2/Symbol/das.jpg")
    dquo1 = Character(18,10,"TylerHandwriting2/Symbol/dquo1.jpg")
    dquo2 = Character(19,9,"TylerHandwriting2/Symbol/dquo2.jpg")
    quo1 = Character(6,9,"TylerHandwriting2/Symbol/quo1.jpg")
    quo2 = Character(8,11,"TylerHandwriting2/Symbol/quo2.jpg")
    sem = Character(11,27,"TylerHandwriting2/Symbol/sem.jpg")
    col = Character(10,24,"TylerHandwriting2/Symbol/col.jpg")

elif setting == 2:
    spacelengthLow = 7
    spacelengthHigh = 12
    leta = Character(13,12,"TylerHandwriting3/Letter/a.jpg")
    letb = Character(14,25,"TylerHandwriting3/Letter/b.jpg")
    letc = Character(12,12,"TylerHandwriting3/Letter/c.jpg")
    letd = Character(19,30,"TylerHandwriting3/Letter/d.jpg")
    lete = Character(12,13,"TylerHandwriting3/Letter/e.jpg")
    letf = Character(18,22,"TylerHandwriting3/Letter/f.jpg")
    letg = Character(12,24,"TylerHandwriting3/Letter/g.jpg")
    leth = Character(12,20,"TylerHandwriting3/Letter/h.jpg")
    leti = Character(7,17,"TylerHandwriting3/Letter/i.jpg")
    letj = Character(17,25,"TylerHandwriting3/Letter/j.jpg")
    letk = Character(16,21,"TylerHandwriting3/Letter/k.jpg")
    letl = Character(6,28,"TylerHandwriting3/Letter/l.jpg")
    letm = Character(14,10,"TylerHandwriting3/Letter/m.jpg")
    letn = Character(14,12,"TylerHandwriting3/Letter/n.jpg")
    leto = Character(12,11,"TylerHandwriting3/Letter/o.jpg")
    letp = Character(12,22,"TylerHandwriting3/Letter/p.jpg")
    letq = Character(14,25,"TylerHandwriting3/Letter/q.jpg")
    letr = Character(11,16,"TylerHandwriting3/Letter/r.jpg")
    lets = Character(8,13,"TylerHandwriting3/Letter/s.jpg")
    lett = Character(12,22,"TylerHandwriting3/Letter/t.jpg")
    letu = Character(11,13,"TylerHandwriting3/Letter/u.jpg")
    letv = Character(12,12,"TylerHandwriting3/Letter/v.jpg")
    letw = Character(15,11,"TylerHandwriting3/Letter/w.jpg")
    letx = Character(14,12,"TylerHandwriting3/Letter/x.jpg")
    lety = Character(17,27,"TylerHandwriting3/Letter/y.jpg")
    letz = Character(15,15,"TylerHandwriting3/Letter/z.jpg")
    capA = Character(18,25,"TylerHandwriting3/LetterCap/Capa.jpg")
    capB = Character(19,22,"TylerHandwriting3/LetterCap/Capb.jpg")
    capC = Character(17,21,"TylerHandwriting3/LetterCap/Capc.jpg")
    capD = Character(19,23,"TylerHandwriting3/LetterCap/Capd.jpg")
    capE = Character(15,25,"TylerHandwriting3/LetterCap/Cape.jpg")
    capF = Character(18,26,"TylerHandwriting3/LetterCap/Capf.jpg")
    capG = Character(14,21,"TylerHandwriting3/LetterCap/Capg.jpg")
    capH = Character(14,23,"TylerHandwriting3/LetterCap/Caph.jpg")
    capI = Character(16,19,"TylerHandwriting3/LetterCap/Capi.jpg")
    capJ = Character(16,27,"TylerHandwriting3/LetterCap/Capj.jpg")
    capK = Character(18,27,"TylerHandwriting3/LetterCap/Capk.jpg")
    capL = Character(20,26,"TylerHandwriting3/LetterCap/Capl.jpg")
    capM = Character(24,25,"TylerHandwriting3/LetterCap/Capm.jpg")
    capN = Character(19,23,"TylerHandwriting3/LetterCap/Capn.jpg")
    capO = Character(19,20,"TylerHandwriting3/LetterCap/Capo.jpg")
    capP = Character(11,28,"TylerHandwriting3/LetterCap/Capp.jpg")
    capQ = Character(24,23,"TylerHandwriting3/LetterCap/Capq.jpg")
    capR = Character(15,20,"TylerHandwriting3/LetterCap/Capr.jpg")
    capS = Character(11,27,"TylerHandwriting3/LetterCap/Caps.jpg")
    capT = Character(23,22,"TylerHandwriting3/LetterCap/Capt.jpg")
    capU = Character(21,24,"TylerHandwriting3/LetterCap/Capu.jpg")
    capV = Character(16,22,"TylerHandwriting3/LetterCap/Capv.jpg")
    capW = Character(23,22,"TylerHandwriting3/LetterCap/Capw.jpg")
    capX = Character(21,23,"TylerHandwriting3/LetterCap/Capx.jpg")
    capY = Character(17,25,"TylerHandwriting3/LetterCap/Capy.jpg")
    capZ = Character(23,23,"TylerHandwriting3/LetterCap/Capz.jpg")
    c1 = Character(8,26,"TylerHandwriting3/Numbers/1.jpg")
    c2 = Character(30,24,"TylerHandwriting3/Numbers/2.jpg")
    c3 = Character(17,22,"TylerHandwriting3/Numbers/3.jpg")
    c4  = Character(17,23,"TylerHandwriting3/Numbers/4.jpg")
    c5 = Character(27,23,"TylerHandwriting3/Numbers/5.jpg")
    c6 = Character(16,24,"TylerHandwriting3/Numbers/6.jpg")
    c7 = Character(20,20,"TylerHandwriting3/Numbers/7.jpg")
    c8  = Character(19,25,"TylerHandwriting3/Numbers/8.jpg")
    c9 = Character(15,25,"TylerHandwriting3/Numbers/9.jpg")
    c0  = Character(19,22,"TylerHandwriting3/Numbers/0.jpg")
    markexe = Character(5,29,"TylerHandwriting3/Symbol/exe.jpg")
    que = Character(15,27,"TylerHandwriting3/Symbol/que.jpg")
    com = Character(8,14,"TylerHandwriting3/Symbol/com.jpg")
    per = Character(6,7,"TylerHandwriting3/Symbol/per.jpg")
    das = Character(15,18,"TylerHandwriting3/Symbol/das.jpg")
    dquo1 = Character(18,10,"TylerHandwriting3/Symbol/dquo1.jpg")
    dquo2 = Character(19,9,"TylerHandwriting3/Symbol/dquo2.jpg")
    quo1 = Character(6,9,"TylerHandwriting3/Symbol/quo1.jpg")
    quo2 = Character(8,11,"TylerHandwriting3/Symbol/quo2.jpg")
    sem = Character(11,27,"TylerHandwriting3/Symbol/sem.jpg")
    col = Character(10,24,"TylerHandwriting3/Symbol/col.jpg")


#Read what the text file says and save it to a string
textfile = open("texttohandwriting.txt", "r")
text = textfile.read()
splittext = text.split()
textfile.close()

#Open the Template image
templatereal = Image.open("Template/template.png")
if templatereal.mode != 'RGB':
    templatereal = templatereal.convert('RGB')
template = templatereal.copy()


#Begin the main loop of the program
for word in splittext:
    if word == "%":   #check if we are starting a new line, represented by the percent sign
        currentx = 0
        currenty = currenty + lineheight
        if currenty >= 1152:
            template.save("Done/Page" + str(pageNumber) + ".jpg", quality=95)
            pageNumber = pageNumber + 1
            template = templatereal.copy()
            currentx = 0
            currenty = 0
            widthcount = 0
        continue
    for element in word:
        widthcount = widthcount + letterCheck(element).getWidth() 
    if (widthcount + currentx) < linewidth:
        for element in word:
            template.paste(letterCheck(element).im, (currentx, currenty + (lineheight - letterCheck(element).getHeight() + checkSpecials(element) + random.randint(-1,1))))
            currentx = currentx + letterCheck(element).getWidth()    
    else:
        currentx = 0
        currenty = currenty + lineheight
        if currenty >= 1152:
            template.save("Done/Page" + str(pageNumber) + ".jpg", quality=95)
            pageNumber = pageNumber + 1
            template = templatereal.copy()
            currentx = 0
            currenty = 0
            widthcount = 0
        for element in word:
            template.paste(letterCheck(element).im, (currentx, currenty + (lineheight - letterCheck(element).getHeight() + checkSpecials(element) + random.randint(-1,1))))
            currentx = currentx + letterCheck(element).getWidth()
    currentx = currentx + random.randint(spacelengthLow,spacelengthHigh)
    widthcount = 0
                              
template.save("Done/Page" + str(pageNumber) + ".jpg", quality=95)




