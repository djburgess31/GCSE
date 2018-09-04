global topic_list
topic_list = ["computing","biology"]

def adduser():
    name=""
    while len(name) == 0:
        name=input("Name:  ")
    age_correct = 0
    while age_correct == 0:
        age_correct = 1
        try:
            age = int(input("Age:  "))
        except ValueError:
            print("Not Valid")
            age_correct = 0
    age=str(age)
    year_correct = 0
    while year_correct == 0:
        year_correct = 1
        year=0
        try:
            while year > 13 or year < 1:
                year = int(input("Year:  "))
        except ValueError:
            print("Not valid")
            year_correct = 0
    year = str(year)
    username=name[:3]+age
    print("Your username is:  ",username)
    password=""
    while len(password) == 0:
        password=input("Password:  ")
    password=password.strip(",")
    details_file=open("details.txt","a")
    details_file.write(username+","+password+","+name+","+age+","+year+",-,-,-,-,-,-"+"\n")
    details_file.close()

def login():
    details_file = open("details.txt", "r")
    details_list = []
    for line in details_file:
        line = line.strip("\n")
        details_list.append(line.split(","))
    details_file.close()

    a = 0
    while a != len(details_list) + 1:
        username = ""
        password = ""
        a = 0
        while a < len(details_list):
            while len(username) == 0:
                username = input("Username:  ")
            while len(password) == 0:
                password = input("Password:  ")
            if details_list[a][0] == username and details_list[a][1] == password:
                a = len(details_list)
            elif username == "Fer40" and password == "Password123":
                a = len(details_list)
            a = a + 1

    return username

def quiz(username):
    topic_choice=""
    while topic_choice not in topic_list:
        topic_choice=input("Computing or Biology:  ").lower()
    topic_file=open((topic_choice+".txt"),"r")
    questions=[]
    for line in topic_file:
        line = line.strip("\n")
        questions.append(line.split(","))
    topic_file.close()

    difficulty=input("Easy, Medium or Hard:  ").lower()
    if difficulty == "easy":
        difficulty_no=0
    elif difficulty == "medium":
        difficulty_no=1
    elif difficulty == "hard":
        difficulty_no=2

    y=0
    correct=0
    for i in range(int(len(questions[difficulty_no])/(difficulty_no+4))):
        print("--------------------\n",questions[difficulty_no][0+y],"\n--------------------")
        for l in range(difficulty_no+2):
            print(questions[difficulty_no][1+y+l])
        question_answer=input("Answer:  ").lower()
        if question_answer == questions[difficulty_no][y+difficulty_no+3]:
            correct=correct+1
        y = y + difficulty_no + 4
    print("You got",correct,"of 5, Thats",(correct*20),"% and a grade",chr((5-correct)+65))

    details_file = open("details.txt", "r")
    details_list = []
    for line in details_file:
        line = line.strip("\n")
        details_list.append(line.split(","))
    details_file.close()

    topic_number=0
    while topic_choice != topic_list[topic_number]:
        topic_number+=1
    for o in range(len(details_list)):
        if details_list[o][0] == username:
            details_list[o][5+topic_number+difficulty_no] = correct


    open("details.txt", "w").close()
    details_file = open("details.txt", "a")
    for a in range(len(details_list)):
        for b in range(len(details_list[a]) - 1):
            details_file.write(str((details_list[a][b])) + ",")
        details_file.write("\n")
    details_file.close()

    questions[3][difficulty_no*2]=(int(questions[3][difficulty_no*2]))+correct
    questions[3][(difficulty_no * 2)+1]=int(questions[3][(difficulty_no * 2)+1])+1

    if int(questions[difficulty_no+4][0]) < correct:
        questions[difficulty_no+4][0] = correct
        questions[difficulty_no+4][1] = username

    open(topic_choice+".txt", "w").close()
    topic_file = open(topic_choice+".txt", "a")
    for a in range(len(questions)):
        for b in range(len(questions[a])):
            topic_file.write(str((questions[a][b])) + ",")
        topic_file.write("\n")
    topic_file.close()

def report():

    report=input("User or Quiz:  ").lower()


    if report == "user":
        details_file = open("details.txt", "r")
        details_list = []
        for line in details_file:
            line = line.strip("\n")
            details_list.append(line.split(","))
        details_file.close()

        username=input("User:  ")
        for o in range(len(details_list)):
            if details_list[o][0] == username:
                b=o

        for a in range(len(topic_list)):
            topic=topic_list[a]
            topic=topic[0].upper()+topic[1:]
            print("--------------------\n",topic,"\n--------------------")
            print(details_list[b][5+(a*3)])
            print(details_list[b][6 + (a * 3)])
            print(details_list[b][7 + (a * 3)])
            if details_list[b][5+(a*3)] != "-":
                correct=details_list[b][5+(a*3)]
                print("Easy:  ",correct,"of 5, Thats",(correct*20),"% and a grade",chr((5-correct)+65))
            else:
                print("Easy:  Not Taken")

            if details_list[b][6+(a*3)] != "-":
                correct=details_list[b][6+(a*3)]
                print(correct)
                #print("Medium:  ",correct,"of 5, Thats",(correct*20),"% and a grade",chr((5-correct)+65) )
            else:
                print("Medium: Not Taken")
            if details_list[b][7+(a*3)] != "-":
                correct=details_list[b][7+(a*3)]
                print("Hard:  ",correct,"of 5, Thats",(correct*20),"% and a grade",chr((5-correct)+65) )
            else:
                print("Hard:  Not Taken")



    elif report == "quiz":
        topic_choice=input("Topic:  ")
        topic_file = open((topic_choice + ".txt"), "r")
        questions = []
        for line in topic_file:
            line = line.strip("\n")
            questions.append(line.split(","))
        topic_file.close()

        if int(questions[3][1]) > 0:
            print("--------------------\nEasy\n--------------------")
            print("Average:  ",int(int(questions[3][0])/int(questions[3][1])*20),"%")
            print("Highscore: ",questions[4][0],"By user: ",questions[4][1])
        else:
            print("No one has taken this quiz yet")
        if int(questions[3][3]) > 0:
            print("--------------------\nMedium\n--------------------")
            print("Average:  ",int(int(questions[3][2])/int(questions[3][3])*20),"%")
            print("Highscore: ",questions[5][0],"By user: ",questions[5][1])
        else:
            print("No one has taken the medium quiz yet")
        if int(questions[3][5]) > 0:
            print("--------------------\nHard\n--------------------")
            print("Average:  ", int(int(questions[3][4]) / int(questions[3][5])*20), "%")
            print("Highscore: ",questions[6][0],"By user: ",questions[6][1])
        else:
            print("No one has taken the hard quiz yet")


x=0
y=0
while x==0:
    option=""
    while option not in ("add user","login","exit"):
        option=input("Add User, Login or Exit:  ").lower()
    if option =="add user":
        adduser()
    elif option == "login":
        username=login()
        x=x+1
    elif option == "exit":
        x=x+1
        y=y+1
    else:
        print("Not Valid")

while y==0:
    function=""
    while function not in ("quiz","report","exit"):
        function=input("Quiz, Report or exit:  ").lower()
    if function == "quiz":
        quiz(username)
    elif function == "report":
        if username == "Fer40":
            report()
        else:
            print("Not valid")
    elif function == "exit":
        y=y+1
    else:
        print("Not valid")
