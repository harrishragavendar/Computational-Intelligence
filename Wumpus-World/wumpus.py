def gen_matrix():
    world=[]
    space=" "
    for i in range(0,4):
        l1=[[space,space,space] for j in range(0,4)]
        world.append(l1)
    return world

def index_to_be_placed(l1):
    space=" "
    for i in range(len(l1)):
            if(l1[i]==space):
                return i

def mark_adjacent(x,y,marking,place):
    if(x<3):
        if(marking not in place[x+1][y]):
            place[x+1][y][index_to_be_placed(place[x+1][y])]=marking
    if(y<3):
        if(marking not in place[x][y+1]):
            place[x][y+1][index_to_be_placed(place[x][y+1])]=marking
    if(x>0):
        if(marking not in place[x-1][y]):
            place[x-1][y][index_to_be_placed(place[x-1][y])]=marking
    if(y>0):
        if(marking not in place[x][y-1]):
            place[x][y-1][index_to_be_placed(place[x][y-1])]=marking
    return place

def add_wumpus(x,y,world):
    pit="P"
    stench="S"
    if(x==0 and y==0):
        print("Wumpus should not be placed in initial state")
        return world
    else:
        if(pit not in world[x][y]):
            world[x][y][index_to_be_placed(world[x][y])]="W"
        else:
            print("There is pit in position(",x,",",y,")")
            return world
        world=mark_adjacent(x,y,stench,world)
        return world
    
def add_pit(x,y,world):
    wumpus="W"
    breeze="B"
    if(x==0 and y==0):
        print("Pit should not be placed in initial state")
        return world
    else:
        if(wumpus not in world[x][y]):
            world[x][y][index_to_be_placed(world[x][y])]="P"
        else:
            print("There is wumpus in position(",x,",",y,")")
            return world
        world=mark_adjacent(x,y,breeze,world)
        return world
    
def add_gold(x,y,world):
    pit="P"
    if(pit not in world[x][y]):
        world[x][y][index_to_be_placed(world[x][y])]="G"
    else:
        print("There is pit in the position(",x,",",y,")")
    return world

def display_world(world):
    print("DETAILS: B=Breeze | S=Stench | P=Pit | W=Wumpus | G=Gold")
    i=3
    while(i>=0):
        print("====================")
        for j in range(0,4):
            print("|",world[i][j][0],"|",end="")
        print()
        for j in range(0,4):
            print("|",world[i][j][1],"|",end="")
        print()
        for j in range(0,4):
            print("|",world[i][j][2],"|",end="")
        print()
        i=i-1
    print("====================")

def display_env(env):
    print("DETAILS: V=Visted | O=Safe Place | A=Agent | B=Breeze | S=Stench")
    i=3
    while(i>=0):
        print("====================")
        for k in range(0,5):
            for j in range(0,4):
                print("|",env[i][j][k],"|",end="")
            print()
        i=i-1
    print("====================")

def move_agent(x,y,env):
    safe_place="O"
    visited="V"
    for i in range(len(env)):
        for j in range(len(env[i])):
            if(safe_place in env[i][j] and visited not in env[i][j] ):
                if((i==x+1 and j==y)or(i==x and j==y+1)or(i==x-1 and j==y)or(i==x and j==y-1)):
                    return i,j
    for i in range(len(env)):
        for j in range(len(env[i])):
           if(safe_place in env[i][j]):
              if((i==x+1 and j==y)or(i==x and j==y+1)or(i==x-1 and j==y)or(i==x and j==y-1)):
                   return i,j
                
def mark_agent(x,y,env):
    env[x][y][index_to_be_placed(env[x][y])]="A"
    if("V" not in env[x][y]):
        env[x][y][index_to_be_placed(env[x][y])]="V"
    display_env(env)
    return env

def gen_percept_seq(x,y,world,shooted):
    percept_seq=[None for i in range(0,5)]
    stench="S"
    breeze="B"
    gold="G"
    wumpus="W"
    if(stench in world[x][y]):
        percept_seq[0]="Stench"
    if(breeze in world[x][y]):
        percept_seq[1]="Breeze"
    if(gold in world[x][y]):
        percept_seq[2]="Glitter"
    if(shooted==False and wumpus in world[x][y]):
        percept_seq[4]="Scream"
    return percept_seq

def mark_safe_place(percept_seq,x,y,env):
    sw=[]
    nw=[]
    se=[]
    ne=[]
    stench="S"
    breeze="B"
    visted="V"
    safe_place="O"
    if(x>0):
        if(y>0):
            sw=env[x-1][y-1]
        if(y<3):
            nw=env[x-1][y+1]
    if(x<3):
        if(y>0):
            se=env[x+1][y-1]
        if(y<3):
            ne=env[x+1][y+1]
    if(percept_seq[0]=="Stench"):
        if(stench not in ne or stench not in sw):
            if(x<3):
                if(safe_place not in env[x+1][y]):
                    env[x+1][y][index_to_be_placed(env[x+1][y])]=safe_place
        if(stench not in se or stench not in nw):
            if(x>0):
                if(safe_place not in env[x-1][y]):
                    env[x-1][y][index_to_be_placed(env[x-1][y])]=safe_place
        if(stench not in se or stench not in sw):
            if(y>0):
                if(safe_place not in env[x][y-1]):
                    env[x][y-1][index_to_be_placed(env[x][y-1])]=safe_place
        if(stench not in ne or stench not in nw):
            if(y<3):
                if(safe_place not in env[x][y+1]):
                    env[x][y+1][index_to_be_placed(env[x][y+1])]=safe_place
    if(percept_seq[0]=="Breeze"):
        if(breeze not in ne or breeze not in sw):
            if(x<3):
                if(safe_place not in env[x+1][y]):
                    env[x+1][y][index_to_be_placed(env[x+1][y])]=safe_place
        if(breeze not in se or breeze not in nw):
            if(x>0):
                if(safe_place not in env[x-1][y]):
                    env[x-1][y][index_to_be_placed(env[x-1][y])]=safe_place
        if(breeze not in se or breeze not in sw):
            if(y>0):
                if(safe_place not in env[x][y-1]):
                    env[x][y-1][index_to_be_placed(env[x][y-1])]=safe_place
        if(breeze not in ne or breeze not in nw):
            if(y<3):
                if(safe_place not in env[x][y+1]):
                    env[x][y+1][index_to_be_placed(env[x][y+1])]=safe_place
        
    if((all(element == percept_seq[0] for element in percept_seq))or "Scream" in percept_seq):
        mark_adjacent(x,y,safe_place,env)
    return env  
     
def play(x,y,world):
    env=[]
    space=" "
    for i in range(0,4):
        l1=[[space,space,space,space,space] for j in range(0,4)]
        env.append(l1)
    notfoundGold=True
    shooted=False
    breeze="B"
    stench="S"
    safe_place="O"
    cnt=0
    flag=1
    env[x][y][index_to_be_placed(env[x][y])]=safe_place
    while(notfoundGold):
        percept_seq=gen_percept_seq(x,y,world,shooted)
        print(f"\n======Move {cnt}: Percept Sequence = {percept_seq}======")
        if("Glitter" in percept_seq):
            notfoundGold=False
            print(f"Gold found in position: {(x,y)}")
            flag=0
        if("Scream" in percept_seq):
            print("Wumpus killed!!")
        if("Stench" in percept_seq):
            if(stench not in env[x][y]):
                env[x][y][index_to_be_placed(env[x][y])]=stench
        if("Breeze" in percept_seq):
            if(breeze not in env[x][y]):
                env[x][y][index_to_be_placed(env[x][y])]=breeze
        if(flag==1):
            mark_safe_place(percept_seq,x,y,env)
        mark_agent(x,y,env)
        env[x][y]= list(map(lambda x: x.replace('A', space), env[x][y]))
        x,y=move_agent(x,y,env)
        cnt=cnt+1

w=gen_matrix()
#Defining the world
# For image, refer testcase.png
add_wumpus(2,1,w)
add_gold(2,2,w)
add_pit(1,3,w)
add_pit(3,0,w)
add_pit(3,3,w)

print("============INITIAL WORLD============")
print("Pits are at:\t(1,3), (3,0), (3,3)")
print("Wumpus is at:\t(2,1)")
print("Gold is at:\t(2,2)")
print("Agent is at:\t(0,0)\n")

display_world(w)

print("\n==========GAME STARTS============")
play(0,0,w)
