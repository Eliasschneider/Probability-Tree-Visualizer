import turtle, random, time, sys
from phonenumbers import length_of_geographical_area_code

from scipy.fftpack import cc_diff
from sklearn.covariance import log_likelihood

args = sys.argv
args.pop(0)


redm = int(args[0])
greenm = int(args[1])
bluem = int(args[2])

print("\n Red: ", redm, "\n Green: ", greenm, "\n Blue: ", bluem)
totalm = (int(redm) + int(greenm) + int(bluem))
print("Total: ", totalm)


redp = 0
greenp = 0
bluep = 0

redt = 0
greent = 0
bluet = 0

ac = []
i = 0
while i < redm:
    ac.append("r")
    i += 1
i = 0

while i < greenm:
    ac.append("g")
    i += 1
i = 0


while i < bluem:
    ac.append("b")
    i += 1

if len(ac) != 10:
    print("please select a total of ten Marbles!")
    exit()
    
acb = ac.copy()
print(ac)
random.shuffle(ac)
print(ac)

print(ac)
print(acb)


t = turtle.Turtle()
turtle.title("Probability Tree Sim")
t.speed(2)

am1 = turtle.Turtle()

am1.speed(100)

am1.shapesize(1, 1, 1)



round = 0

cc = "rgb"
def pickNewColor():

    global cc
    global ac
    random.shuffle(ac)
    print(ac)
    if ac[0] == "r":
        cc = "r"
        ac.remove("r")
        print(ac)
    elif ac[0] == "g":
        cc = "g"
        ac.remove("g")
        print(ac)
    elif ac[0] == "b":
        cc = "b"
        ac.remove("b")
        print(ac)


t.penup()
t.right(180)
t.fd(500)
t.right(90)
t.forward(210)



i = 0
while i < redm:
    t.pendown()
    t.color("red")
    t.dot(10)
    t.penup()
    t.right(90)
    t.fd(20)
    t.left(90)
    i += 1

t.right(180)
t.forward(20)
t.right(90)
t.forward(redm * 20)
t.right(90)
i = 0
while i < greenm:
    t.pendown()
    t.color("green")
    t.dot(10)
    t.penup()
    t.right(90)
    t.fd(20)
    t.left(90)
    i += 1

t.right(180)
t.forward(20)
t.right(90)
t.forward(greenm * 20)
t.right(90)
i = 0
while i < bluem:
    t.pendown()
    t.color("blue")
    t.dot(10)
    t.penup()
    t.right(90)
    t.fd(20)
    t.left(90)
    i += 1

t.right(180)
t.fd(100)
t.right(90)
t.fd(50)
t.right(180)
t.color("red")
t.write(str(("red: ", int((ac.count("r")/len(ac)*100)), "%")))
t.right(90)
t.fd(20)
t.left(90)
t.color("green")
t.write(str(("green: ", int((ac.count("g")/len(ac)*100)), "%")))
t.right(90)
t.fd(20)
t.left(90)
t.color("blue")
t.write(str(("blue: ", int((ac.count("b")/len(ac)*100)), "%")))



t.speed(19999)

t.color("black")
t.home()  
t.pendown()


def afterh():
    am1.clear()
    am1.penup()
    am1.home()
    am1.right(180)
    am1.fd(500)
    am1.left(90)
    am1.fd(50)
    am1.left(90)
    am1.color("black")
    am1.write("until now, it has been:")
    am1.right(90)
    am1.fd(20)
    am1.left(90)
    am1.color("red")
    am1.write(str(redt) + " Red final marbles")
    am1.right(90)
    am1.fd(20)
    am1.left(90)
    am1.color("green")
    am1.write(str(greent) + " Green final marbles")
    am1.right(90)
    am1.fd(20)
    am1.left(90)
    am1.color("blue")
    am1.write(str(bluet) + " Blue final marbles")
    am1.right(90)
    am1.fd(20)
    am1.left(90)
    am1.color("black")
    am1.write("and " + str(totalt) + " total marbles")
    am1.home()
    am1.pendown()



#if len(ac) == 1:
 #       if ac[0] == "r":
  #          redt += 1
   #     elif ac[0] == "g":
    #        greent += 1
     #   elif ac[0] == "b":
      #      bluet += 1
       # totalt = (redt + greent + bluet)


def nextMove0():
    global t
    if cc == "r":
        t.color("red")
        t.left(65)
        t.fd(50)
        t.right(65)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(21.13)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(65)
        t.fd(50)
        t.left(65)
        t.right(180) 
        t.stamp() 
        t.right(180)


def nextMove1():
    global t
    if cc == "r":
        t.color("red")
        t.left(55)
        t.fd(50)
        t.right(55)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(28.68)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(55)
        t.fd(50)
        t.left(55)
        t.right(180) 
        t.stamp() 
        t.right(180)


def nextMove2():
    global t
    if cc == "r":
        t.color("red")
        t.left(45)
        t.fd(50)
        t.right(45)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(35.36)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(45)
        t.fd(50)
        t.left(45)
        t.right(180) 
        t.stamp() 
        t.right(180)


def nextMove3():
    global t
    if cc == "r":
        t.color("red")
        t.left(45)
        t.fd(50)
        t.right(45)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(35.36)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(45)
        t.fd(50)
        t.left(45)
        t.right(180) 
        t.stamp()
        t.right(180)


def nextMove4():
    global t
    if cc == "r":
        t.color("red")
        t.left(40)
        t.fd(50)
        t.right(40)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(38.3)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(40)
        t.fd(50)
        t.left(40)
        t.right(180) 
        t.stamp() 
        t.right(180)


def nextMove5():
    global t
    if cc == "r":
        t.color("red")
        t.left(35)
        t.fd(50)
        t.right(35)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(40.96)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(35)
        t.fd(50)
        t.left(35)
        t.right(180) 
        t.stamp() 
        t.right(180)


def nextMove6():
    global t
    if cc == "r":
        t.color("red")
        t.left(30)
        t.fd(50)
        t.right(30)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(43.3)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(30)
        t.fd(50)
        t.left(30)
        t.right(180) 
        t.stamp() 
        t.right(180)


def nextMove7():
    global t
    if cc == "r":
        t.color("red")
        t.left(25)
        t.fd(50)
        t.right(25)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(45.32)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(25)
        t.fd(50)
        t.left(25)
        t.right(180) 
        t.stamp() 
        t.right(180)


def nextMove8():
    global t
    if cc == "r":
        t.color("red")
        t.left(12.5)
        t.fd(50)
        t.right(12.5)
        t.right(180) 
        t.stamp() 
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(48.81)
        
        t.right(180) 
        t.stamp() 
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(12.5)
        t.fd(50)
        t.left(12.5)
        t.right(180) 
        t.stamp() 
        t.right(180)


def nextMove9():
    global t
    if cc == "r":
        t.color("red")
        t.left(5)
        t.fd(50)
        t.right(5)
        t.right(180) 
         
        t.right(180)
    if cc == "g":
        t.color("green")
        
        t.fd(49.81)
        
        t.right(180) 
         
        t.right(180)

    if cc == "b":
        t.color("blue")
        t.right(5)
        t.fd(50)
        t.left(5)
        t.right(180) 
         
        t.right(180)


# print("set a number of runs:")
# dn = input(">>> ")
i = 0
totali = 0

while len(ac) >= 0:
    print()
    print("Currently are ", ac.count("r"), " Red marbles, ", ac.count("g"), " Green marbles and ", ac.count("b"), " Blue marbles left.")
    print()
    if len(ac) > 0:
        print("The percentage for the colours are:")
        print("red: ", int((ac.count("r")/len(ac)*100)), "%")
        print("green: ", int((ac.count("g")/len(ac)*100)), "%")
        print("blue: ", int((ac.count("b")/len(ac)*100)), "%")
        pickNewColor()

        if round == 0:
            nextMove0()
            round += 1
        elif round == 1:
            nextMove1()
            round += 1
        elif round == 2:
            nextMove2()
            round += 1
        elif round == 3:
            nextMove3()
            round += 1
        elif round == 4:
            nextMove4()
            round += 1
        elif round == 5:
            nextMove5()
            round += 1
        elif round == 6:
            nextMove6()
            round += 1
        elif round == 7:
            nextMove7()
            round += 1
        elif round == 8:
            nextMove8()
            round += 1
        elif round == 9:
            nextMove9()
            round += 1
        if round == len(ac):
            i += 1           

        
        print()
    
    
    if len(ac) == 1:
        if ac[0] == "r":
            redt += 1
        elif ac[0] == "g":
            greent += 1
        elif ac[0] == "b":
            bluet += 1
        totalt = (redt + greent + bluet)
        totali += 1
        i += 1


        if totali == 5:
            afterh()
            totali = 0
    


    if len(ac) == 0:
        ac = acb.copy()
        random.shuffle(ac)
        t.color("black")
        t.penup()
        t.home()
        t.pendown()
        round = 0
    

turtle.done()

