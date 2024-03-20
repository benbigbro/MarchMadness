import sys

#BONUSES
# firstround = 1
# secondround = 2
# thirdround = 3
# fourthround = 4
# fifthround = 5
# sixthround = 6


firstround = 1
secondround = 5
thirdround = 10
fourthround = 15
fifthround = 20
sixthround = 25

#CONFIG
hardloss = True #people who are in the loss column are garunteed to be out
maxScores = True #spit out the max score to make sure I inputted correct brackets


if len(sys.argv) != 2:
    print("Please enter the year as second command line argument")
    exit(-1)
year = sys.argv[1]
print("\n\n\n")


participants = []

p_file_path = year + "/participants.txt"

with open(p_file_path) as f:
    participants = f.readlines()

participants = [name.replace("\n","") for name in participants]

participants = [name+".txt" for name in participants]

pfilename = year + "/perfect.txt"
pfile = open (pfilename, "r")
perfpicks = []
perfpicks = pfile.readlines()
perfpicks = [pick.replace("\n","") for pick in perfpicks]
pfile.close()

stillAlive = []
dead = []

for name in participants:

    topName = ""
    topScore = 0

    filename = year + "/participants/" + name
    file = open(filename, "r")
    picks = []
    picks = file.readlines()
    picks = [pick.replace("\n","") for pick in picks]
    file.close()

    teams = []

    p_firstround = []
    ideal_firstround = []
    my_firstround = []

    p_secondround = []
    ideal_secondround = []
    my_secondround = []

    p_thirdround = []
    ideal_thirdround = []
    my_thirdround = []

    p_fourthround = []
    ideal_fourthround = []
    my_fourthround = []

    p_fifthround = []
    ideal_fifthround = []
    my_fifthround = []

    p_sixthround = []
    ideal_sixthround = []
    my_sixthround = []

    iter = 0
    #collect all the teams in the tournament into initial list
    for i in range(64):
        teams.append(perfpicks[iter])

    iter = 64

    #get first round winners
    for i in range(32):
        perfect_pick = perfpicks[iter]
        my_pick = picks[iter]
        iter +=1
        my_firstround.append(my_pick)
        if perfect_pick == "NA":
            #this game has not happened yet, check to see if my team still exits in the previous round
            if my_pick in teams:
                #my team is still alive from the previous round, add them to my ideal bracket
                ideal_firstround.append(my_pick)
            else:
                if(hardloss):
                    #my team is not alive from the previous round, no body else should score points from this game
                    ideal_firstround.append("NA")
                else:
                    #on the other hand, I could pick a random team from the previous round which could advance
                    ideal_firstround.append(teams[i*2])
        else:
            #this game has happeded, add the winner to the ideal bracket
            ideal_firstround.append(perfect_pick)
            p_firstround.append(perfect_pick)

    iter = 64+32

    #get second round winners
    for i in range(16):
        perfect_pick = perfpicks[iter]
        my_pick = picks[iter]
        iter +=1
        my_secondround.append(my_pick)
        if perfect_pick == "NA":
            #this game has not happened yet, check to see if my team still exits in the previous round
            if my_pick in ideal_firstround:
                #my team is still alive from the previous round, add them to my ideal bracket
                ideal_secondround.append(my_pick)
            else:
                if(hardloss):
                    #my team is not alive from the previous round, no body else should score points from this game
                    ideal_secondround.append("NA")
                else:
                    #on the other hand, I could pick a random team from the previous round which could advance
                    #only one of these should be uncommented
                    ideal_secondround.append(ideal_firstround[i*2])
        else:
            #this game has happeded, add the winner to the ideal bracket
            ideal_secondround.append(perfect_pick)
            p_secondround.append(perfect_pick)

    iter = 64+32+16

    #get third round winners
    for i in range(8):
        perfect_pick = perfpicks[iter]
        my_pick = picks[iter]
        iter +=1
        my_thirdround.append(my_pick)
        if perfect_pick == "NA":
            #this game has not happened yet, check to see if my team still exits in the previous round
            if my_pick in ideal_secondround:
                #my team is still alive from the previous round, add them to my ideal bracket
                ideal_thirdround.append(my_pick)
            else:
                if(hardloss):
                    #my team is not alive from the previous round, no body else should score points from this game
                    ideal_thirdround.append("NA")
                else:
                    #on the other hand, I could pick a random team from the previous round which could advance
                    #only one of these should be uncommented
                    ideal_thirdround.append(ideal_secondround[i*2])
        else:
            #this game has happeded, add the winner to the ideal bracket
            ideal_thirdround.append(perfect_pick)
            p_thirdround.append(perfect_pick)

    iter = 64+32+16+8

    #get fourth round winners
    for i in range(4):
        perfect_pick = perfpicks[iter]
        my_pick = picks[iter]
        iter +=1
        my_fourthround.append(my_pick)
        if perfect_pick == "NA":
            #this game has not happened yet, check to see if my team still exits in the previous round
            if my_pick in ideal_thirdround:
                #my team is still alive from the previous round, add them to my ideal bracket
                ideal_fourthround.append(my_pick)
            else:
                if(hardloss):
                    #my team is not alive from the previous round, no body else should score points from this game
                    ideal_fourthround.append("NA")
                else:
                    #on the other hand, I could pick a random team from the previous round which could advance
                    #only one of these should be uncommented
                    ideal_fourthround.append(ideal_thirdround[i*2])
        else:
            #this game has happeded, add the winner to the ideal bracket
            ideal_fourthround.append(perfect_pick)
            p_fourthround.append(perfect_pick)

    iter = 64+32+16+8+4

    #get fifth round winners
    for i in range(2):
        perfect_pick = perfpicks[iter]
        my_pick = picks[iter]
        iter +=1
        my_fifthround.append(my_pick)
        if perfect_pick == "NA":
            #this game has not happened yet, check to see if my team still exits in the previous round
            if my_pick in ideal_fourthround:
                #my team is still alive from the previous round, add them to my ideal bracket
                ideal_fifthround.append(my_pick)
            else:
                if(hardloss):
                    #my team is not alive from the previous round, no body else should score points from this game
                    ideal_fifthround.append("NA")
                else:
                    #on the other hand, I could pick a random team from the previous round which could advance
                    #only one of these should be uncommented
                    ideal_fifthround.append(ideal_fourthround[i*2])
        else:
            #this game has happeded, add the winner to the ideal bracket
            ideal_fifthround.append(perfect_pick)
            p_fifthround.append(perfect_pick)

    iter = 64+32+16+8+4+2

    #get sixth round winners
    for i in range(1):
        perfect_pick = perfpicks[iter]
        my_pick = picks[iter]
        iter +=1
        my_sixthround.append(my_pick)
        if perfect_pick == "NA":
            #this game has not happened yet, check to see if my team still exits in the previous round
            if my_pick in ideal_fifthround:
                #my team is still alive from the previous round, add them to my ideal bracket
                ideal_sixthround.append(my_pick)
            else:
                if(hardloss):
                    #my team is not alive from the previous round, no body else should score points from this game
                    ideal_sixthround.append("NA")
                else:   
                    #on the other hand, I could pick a random team from the previous round which could advance
                    #only one of these should be uncommented
                    ideal_sixthround.append(ideal_fifthround[(i*2)+1])
        else:
            #this game has happeded, add the winner to the ideal bracket
            ideal_sixthround.append(perfect_pick)
            p_sixthround.append(perfect_pick)

    for name2 in participants:
        filename2 = year + "/participants/" + name2
        file2 = open(filename2, "r")
        picks = []
        picks = file2.readlines()
        picks = [pick.replace("\n","") for pick in picks]
        file2.close()
        my_firstround = []
        my_secondround = []
        my_thirdround = []
        my_fourthround = []
        my_fifthround = []
        my_sixthround = []
        iter = 64

        #get first round winners
        for i in range(32):
            my_pick = picks[iter]
            iter +=1
            my_firstround.append(my_pick)

        iter = 64+32

        #get second round winners
        for i in range(16):
            my_pick = picks[iter]
            iter +=1
            my_secondround.append(my_pick)

        iter = 64+32+16

        #get third round winners
        for i in range(8):
            my_pick = picks[iter]
            iter +=1
            my_thirdround.append(my_pick)

        iter = 64+32+16+8

        #get fourth round winners
        for i in range(4):
            my_pick = picks[iter]
            iter +=1
            my_fourthround.append(my_pick)

        iter = 64+32+16+8+4

        #get fifth round winners
        for i in range(2):
            my_pick = picks[iter]
            iter +=1
            my_fifthround.append(my_pick)

        iter = 64+32+16+8+4+2

        #get sixth round winners
        for i in range(1):
            my_pick = picks[iter]
            iter +=1
            my_sixthround.append(my_pick)


        points = 0
        #calculate first round points
        for ideal_pick in ideal_firstround:
            temp = ideal_pick.split()
            team = ""
            seed = 0
            if len(temp) == 2:
                team = temp[0]
                seed = int(temp[1])
            if(ideal_pick in my_firstround):
                points += seed + firstround

        #calculate second round points
        for ideal_pick in ideal_secondround:
            temp = ideal_pick.split()
            team = ""
            seed = 0
            if len(temp) == 2:
                team = temp[0]
                seed = int(temp[1])
            if(ideal_pick in my_secondround):
                points += seed + secondround

        #calculate third round points
        for ideal_pick in ideal_thirdround:
            temp = ideal_pick.split()
            team = ""
            seed = 0
            if len(temp) == 2:
                team = temp[0]
                seed = int(temp[1])
            if(ideal_pick in my_thirdround):
                points += seed + thirdround

        #calculate fourth round points
        for ideal_pick in ideal_fourthround:
            temp = ideal_pick.split()
            team = ""
            seed = 0
            if len(temp) == 2:
                team = temp[0]
                seed = int(temp[1])
            if(ideal_pick in my_fourthround):
                points += seed + fourthround

        #calculate fifth round points
        for ideal_pick in ideal_fifthround:
            temp = ideal_pick.split()
            team = ""
            seed = 0
            if len(temp) == 2:
                team = temp[0]
                seed = int(temp[1])
            if(ideal_pick in my_fifthround):
                points += seed + fifthround
            
        #calculate sixth round points
        for ideal_pick in ideal_sixthround:
            temp = ideal_pick.split()
            team = ""
            seed = 0
            if len(temp) == 2:
                team = temp[0]
                seed = int(temp[1])
            if(ideal_pick in my_sixthround):
                points += seed + sixthround
        if (points > topScore):
            topName = name2
            topScore = points
        if(name == name2 and maxScores):
            temp = name.replace(".txt","")
            temp = temp.replace("_", " ")
            print(f"{temp}'s max score is {points}\n")
    temp = name
    if name == topName:
        topName = topName.replace("_"," ")
        topName = topName.replace(".txt","")
        stillAlive.append(topName)
    else:
        temp = temp.replace("_", " ")
        temp = temp.replace(".txt", "")
        dead.append(temp)

print("\nThe family members still in the running are:\n\n")
for name in stillAlive:
    print(name)

print("\nThe family members who are mathematically eliminated are:\n")
for name in dead:
    print(name)