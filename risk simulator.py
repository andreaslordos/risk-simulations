import time
from random import randint
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

trials=int(input("Trials (>10000 recommended, 100k optimal): "))
start_time = time.time()
print("This will take about",str((trials/20)/60),"minutes")
def risk(attack,defense,trials):
    results=[] #initializes the results list
    while len(results)<trials: #this loop will continue running the number of trials asked for by the user are complete
        attackDices=[] #resets attackDices list
        defenseDices=[] #resets the defenseDices list
        attackTroops=attack #sets the number of attackTroops to the variable attack, which keeps track of how many troops are left attacking
        defenseTroops=defense #sets the number of attackTroops to the variable attack, which keeps track of how many troops are left attacking
        while attackTroops>0 and defenseTroops>0: #while there is at least one attackTroop and at least one defense troop

            z=1 #z is the default number of dices for the defenders. 
            if defenseTroops>=2: #however, if the defenders have 2 or more troops defending, 
                z=2 #they get two dices

            w=1 #w is the default number of dices for the attackers.
            if attackTroops==2: #however, if the attackers have 2 troops attacking,
                w=2 #they get 2 dices
            elif attackTroops>=3:
                w=3
                
            for x in range(w): #repeats the loop w times
                attackDices.append(randint(1,6)) #inputs a random integer from 1 to 6 into the list attackDices
                
            for y in range(z): #repeats the loop z times
                defenseDices.append(randint(1,6)) #inputs a random integer from 1 to 6 into the list defenseDices
                    
            defenseDices.sort(reverse=True) #sorts the list defenseDices in descending order
            attackDices.sort(reverse=True) #sorts the list attackDices in descending order

            contestCounter=len(attackDices)
            if len(attackDices)>len(defenseDices):
                contestCounter=len(defenseDices)
            

            for x in range(contestCounter): #repeat the loop contestCounter times
                if attackTroops<1 or defenseTroops<1: #if there is less than one attackTroop, or less than 1 defenseTroop, end the simulation
                    break #end the loop 
                if defenseDices[x]>=attackDices[x] : #compares the biggest unused dice roll from both defenseDices and attackDices
                    attackTroops-=1 #if the defenseDice roll is equal to or larger than the attackDice roll, then attackers lose 1 troop
                else:
                    defenseTroops-=1 #otherwise, defenders lose one troop
            
            defenseDices=[] #resets the two lists
            attackDices=[] #resets the two lists
            
        if defenseTroops<=0: #if defenseTroops is less than or equal to 0
            results.append(("A",attackTroops)) #attackers win. add that to the results list along with how many attackTroops left
        else:
            results.append(("D",defenseTroops)) #else, the defenders win. add that to the results list along with how many defenseTroops left


    totalD=0 #initializes totalD, which is the variable for keeping track how many, on average, defense troops were left
    totalA=0 #initializes totalA, which is the variable for keeping track how many, on average, attack troops were left
    attackWins=0 #initializes attackWins variable which keeps track of how many times the attackers won
    defenseWins=0 #initializes the defenseWins variable which keeps track of how many times the defenders won
    for x in range(len(results)): #repeat the loop (length of results list) times
        if results[x][0]=="D": #if the x'th result says that the defenders won
            totalD+=results[x][1] #add the number of defense soldiers left alive to totalD
            defenseWins+=1 #add 1 to defenseWins
        else:
            attackWins+=1 #else add 1 to attackWins
            totalA+=results[x][1] #and add the total number of attack soldiers left alive to totalA

    return round(attackWins/trials,4)

colors=["b","c","g","r","m","y","k"]

points=[]
plt.axis([0,30,0,1])
plt.title("Attacker's winning probabiilties at various strengths")
plt.ylabel('p(attacker winning)')
plt.xlabel('number of defenders')
plotlist=[]
for u in range(29):
    points.append((u+2,u+2,risk(u+2,u+2,trials)))

points.sort()
xList=[]
yList=[]
for element in points:
    xList.append(element[0])
    yList.append(element[-1])
    
for element in points:
    plt.plot(xList,yList,colors[-1])

points=[]
for defNumb in range(30):
    for attkNumb in range(5,35,5):
        points.append((attkNumb,defNumb+1,risk(attkNumb,defNumb+1,trials)))


plotlist=[]
usedAttkNumb=[]
x=-1
points.sort()
print("--- %s seconds ---" % (time.time() - start_time))
for element in points:
    if element[0] not in usedAttkNumb:
        usedAttkNumb.append(element[0])
        plotlist.append([[],[]])
        x+=1
    plotlist[x][0].append(element[1])
    plotlist[x][1].append(element[2])




for x in range(len(plotlist)):
    plt.plot(plotlist[x][0],plotlist[x][1],colors[x])

patches=[]
x=5
for c in colors:
    patches.append(mpatches.Patch(color=c,label=str(x)+" attackers"))
    x+=5
patches.pop(-1)
patches.append(mpatches.Patch(color=colors[-1],label="30 attackers"))                        
plt.legend(handles=patches)
plt.show()
