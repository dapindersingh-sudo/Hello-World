t_atn=input("Enter total attendence: ")
a_atn=input("Enter classes you have attended: ")
tclas=float(t_atn)
aclas=float(a_atn)
prcnt=(aclas/tclas)*100
# pr=float(prcnt)
if prcnt == 75:
    print("You'r attenence is on borer")
    print("You can skip 0 class")
elif prcnt>75:
    cnt=0
    print("You are above standard")
    while prcnt>75:
        tclas=tclas+1
        prcnt=round((aclas/tclas)*100)
        cnt=cnt+1
    print(f'You can skip {cnt} classes')
elif prcnt<75:
    cnt=0
    while prcnt<75:
        aclas = aclas+1
        prcnt=int((aclas/tclas)*100)
        cnt=cnt+1
    print(f'You have to attend {cnt} classes')
