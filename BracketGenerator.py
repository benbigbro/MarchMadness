import sys
print()

if len(sys.argv) != 3:
    print("Please enter the year as second command line argument")
    print("Please enter the type of bracket creation: \"perfect\" or \"all\" as the third command line argument")
    exit(-1)

year = sys.argv[1]

perfect = False
if sys.argv[2] == "perfect":
    print("Perfect")
    perfect = True
if sys.argv[2] == "all":
    print("all")
    perfect = False

print(f"The year will be {year}")
teams = []
t_file_path = year + "/teams.txt"

with open(t_file_path) as f:
    teams = f.readlines()

teams = [name.replace("\n","") for name in teams]

participants = []

p_file_path = year + "/participants.txt"

with open(p_file_path) as f:
    participants = f.readlines()

participants = [name.replace("\n","") for name in participants]

teams32 = []
teams16 = []
teams8 = []
teams4 = []
teams2 = []
winner = []

na = "NA"

if(perfect):
    filename = year + "/perfect.txt"
    file = open(filename, "w")
    for i in range(len(teams)):
        file.write(teams[i]+"\n")
        if i%2 == 1:
            continue
        temp = int(input(f"\n{teams[i]} or {teams[i+1]}?\n"))
        if temp == 1:
            teams32.append(teams[i])
        if temp == 2:
            teams32.append(teams[i+1])
        if temp == 3:
            teams32.append(na)

    print("\n\n\nend of first round\n\n\n")

    for i in range(len(teams32)):
        file.write(teams32[i]+"\n")
        if i%2 == 1:
            continue
        temp = int(input(f"\n{teams32[i]} or {teams32[i+1]}?\n"))
        if temp == 1:
            teams16.append(teams32[i])
        if temp == 2:
            teams16.append(teams32[i+1])
        if temp == 3:
            teams16.append(na)

    print("\n\n\nend of second round\n\n\n")

    for i in range(len(teams16)):
        file.write(teams16[i]+"\n")
        if i%2 == 1:
            continue
        temp = int(input(f"\n{teams16[i]} or {teams16[i+1]}?\n"))
        if temp == 1:
            teams8.append(teams16[i])
        if temp == 2:
            teams8.append(teams16[i+1])
        if temp == 3:
            teams8.append(na)

    print("\n\n\nend of sweet sixteen\n\n\n")

    for i in range(len(teams8)):
        file.write(teams8[i]+"\n")
        if i%2 == 1:
            continue
        temp = int(input(f"\n{teams8[i]} or {teams8[i+1]}?\n"))
        if temp == 1:
            teams4.append(teams8[i])
        if temp == 2:
            teams4.append(teams8[i+1])
        if temp == 3:
            teams4.append(na)

    print("\n\n\nend of elite eight\n\n\n")

    for i in range(len(teams4)):
        file.write(teams4[i]+"\n")
        if i%2 == 1:
            continue
        temp = int(input(f"\n{teams4[i]} or {teams4[i+1]}?\n"))
        if temp == 1:
            teams2.append(teams4[i])
        if temp == 2:
            teams2.append(teams4[i+1])
        if temp == 3:
            teams2.append(na)

    print("\n\n\nend of final four\n\n\n")

    for i in range(len(teams2)):
        file.write(teams2[i]+"\n")
        if i%2 == 1:
            continue
        temp = int(input(f"\n{teams2[i]} or {teams2[i+1]}?\n"))
        if temp == 1:
            winner.append(teams2[i])
        if temp == 2:
            winner.append(teams2[i+1])
        if temp == 3:
            winner.append(na)

    print("\n\n\nend of championship\n\n\n")
    file.write(winner[0]+"\n")
    file.close()
else:
    for participant in participants:
        filename = year + "/participants/" + participant + ".txt"
        print(filename)
        test = input("continue?\n")
        if test == "n":
            continue
        file = open(filename, "w")
        for i in range(len(teams)):
            file.write(teams[i]+"\n")
            if i%2 == 1:
                continue
            temp = int(input(f"\n{teams[i]} or {teams[i+1]}?\n"))
            if temp == 1:
                teams32.append(teams[i])
            if temp == 2:
                teams32.append(teams[i+1])
            if temp == 3:
                teams32.append(na)

        print("\n\n\nend of first round\n\n\n")

        for i in range(len(teams32)):
            file.write(teams32[i]+"\n")
            if i%2 == 1:
                continue
            temp = int(input(f"\n{teams32[i]} or {teams32[i+1]}?\n"))
            if temp == 1:
                teams16.append(teams32[i])
            if temp == 2:
                teams16.append(teams32[i+1])
            if temp == 3:
                teams16.append(na)

        print("\n\n\nend of second round\n\n\n")

        for i in range(len(teams16)):
            file.write(teams16[i]+"\n")
            if i%2 == 1:
                continue
            temp = int(input(f"\n{teams16[i]} or {teams16[i+1]}?\n"))
            if temp == 1:
                teams8.append(teams16[i])
            if temp == 2:
                teams8.append(teams16[i+1])
            if temp == 3:
                teams8.append(na)

        print("\n\n\nend of sweet sixteen\n\n\n")

        for i in range(len(teams8)):
            file.write(teams8[i]+"\n")
            if i%2 == 1:
                continue
            temp = int(input(f"\n{teams8[i]} or {teams8[i+1]}?\n"))
            if temp == 1:
                teams4.append(teams8[i])
            if temp == 2:
                teams4.append(teams8[i+1])
            if temp == 3:
                teams4.append(na)

        print("\n\n\nend of elite eight\n\n\n")

        for i in range(len(teams4)):
            file.write(teams4[i]+"\n")
            if i%2 == 1:
                continue
            temp = int(input(f"\n{teams4[i]} or {teams4[i+1]}?\n"))
            if temp == 1:
                teams2.append(teams4[i])
            if temp == 2:
                teams2.append(teams4[i+1])
            if temp == 3:
                teams2.append(na)

        print("\n\n\nend of final four\n\n\n")

        for i in range(len(teams2)):
            file.write(teams2[i]+"\n")
            if i%2 == 1:
                continue
            temp = int(input(f"\n{teams2[i]} or {teams2[i+1]}?\n"))
            if temp == 1:
                winner.append(teams2[i])
            if temp == 2:
                winner.append(teams2[i+1])
            if temp == 3:
                winner.append(na)

        print("\n\n\nend of championship\n\n\n")
        file.write(winner[0]+"\n")
        file.close()