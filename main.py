import os


th = 0
file = open(input("Enter the address of the file to be imported>>"), "w")
print("__________")
strs = {}    #head


def h(a):
    s = input(str(a) + " ")
    strs[a] = s
    return 0


while True:
    th += 1
    n = input(str(th) + ">>")
    if n == "&QUIT":
        break
    elif n[0:5] == "&CHANGE":
        h(n[1:])
        th -= 1
    elif n == "&GAME":
        os.system("python3 game.py")
    elif n[0] == "|":
        strs[str(th)] = n[1:] 
    else:
        strs[str(th)] = n  #main


for a in strs:
    file.write(strs[a])
    file.write("\r")    #write
