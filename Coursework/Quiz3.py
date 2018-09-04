global topic_list
topic_list = ["computing", "biology"]
difficulty_list= ["easy","medium","hard"]

def file_list(file):
    open_file=open(file+".txt","r")
    list = []
    for line in open_file:
        line = line.strip("\n")
        list.append(line.split(","))
    open_file.close()
    return list

def rewritefile(file,list):
    open_file=open(file+".txt","w").close()
    open_file = open(file+".txt","a")
    for a in range(len(list)):
        for b in range(len(list[a])-1):
            open_file.write(str((list[a][b])) + ",")
        open_file.write("\n")
    open_file.close()

def num_range(number,lower,upper):
    print(number,lower,upper)
    try:
        number=int(number)
        if lower <= number <= upper:
            valid="true"
        else:
            valid="false"
    except ValueError:
        valid = "false"
    return valid

def adduser():
    name = ""
    while len(name) == 0:
        name = input("Name:  ")
    valid = "false"
    while valid == "false":
        age = input("Age:  ").strip(",")
        valid = num_range(age, 4, 18)
    valid = "false"
    while valid == "false":
        year = input("Year:  ").strip(",")
        valid = num_range(year, 4, 18)
    username = name[:3] + str(age)
    print("Your username is:  ", username)
    password = ""
    while len(password) == 0:
        password = input("Password:  ").strip(",")
    details_file = open("details.txt", "a")
    details_file.write(username + "," + password + "," + name + "," + str(age) + "," + (stryear) + ",-,-,-,-,-,-" + "\n")
    details_file.close()

def login():
    details_list = file_list("details")
    a = 0
    while a != len(details_list) + 1:
        username = ""
        password = ""
        a = 0
        while a < len(details_list):
            username = input("Username:  ")
            password = input("Password:  ")
            if details_list[a][0] == username and details_list[a][1] == password:
                a = len(details_list)
            elif username == "Fer40" and password == "Password123":
                a = len(details_list)
            a = a + 1
    return username

def quiz(username):
    details_list = file_list("details")
    for a in range(len(details_list)):
        if details_list[a][0] == username:
            username_place=a
    done_before="0"
    while done_before != "-":
        topic_choice=""
        while topic_choice not in topic_list:
            topic_choice=input("Computing or Biology:  ").lower()
        topic_number = topic_list.index(topic_choice)
        difficulty=input("Easy, Medium or Hard:  ").lower()
        difficulty_no=difficulty_list.index(difficulty)
        done_before=details_list[username_place][5+topic_number+difficulty_no]
        if done_before != "-":
            print("You have done this quiz before")
    questions = file_list(topic_choice)
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
    details_list[username_place][5+topic_number+difficulty_no] = correct
    rewritefile("details",details_list)
    questions[3][difficulty_no*2]=(int(questions[3][difficulty_no*2]))+correct
    questions[3][(difficulty_no * 2)+1]=int(questions[3][(difficulty_no * 2)+1])+1
    if int(questions[difficulty_no+4][0]) < correct:
        questions[difficulty_no+4][0] = correct
        questions[difficulty_no+4][1] = username
    rewritefile(topic_choice,questions)

def report():
    report=""
    while report not in ("user","quiz"):
        report = input("User or Quiz:  ").lower()
    if report == "user":
        details_list = file_list("details")
        username_place=""
        while username_place == "":
            username = input("User:  ")
            for a in range(len(details_list)):
                if details_list[a][0] == username:
                    username_place = a
        for b in range(len(topic_list)):
            print("--------------------\n",(topic_list[b])[0].upper()+(topic_list[b])[1:],"\n--------------------")
            for c in range(len(difficulty_list)):
                if details_list[username_place][5+(b*3)+c] == "-":
                    print((difficulty_list[c])[0].upper()+(difficulty_list[c])[1:],":\t\tNot taken yet")
                else:
                    correct = int(details_list[username_place][5 + (b*3) + c])
                    print((difficulty_list[c])[0].upper()+(difficulty_list[c])[1:],":\t\t",correct,"correct of 5. Thats",correct*20,"% and a grade: ",chr((5-correct)+65))

    elif report == "quiz":
        topic_choice=""
        while topic_choice not in topic_list:
            topic_choice=input("Topic:  ").lower()
        questions = file_list(topic_choice)
        for a in range(len(difficulty_list)):
            print("--------------------\n",(difficulty_list[a])[0].upper()+(difficulty_list[a])[1:],"\n--------------------")
            if int(questions[3][a * 2]) != 0:
                average = int(int(questions[3][a*2])/ int(questions[3][(a*2)+1]))
                print("Average:\t\t",average,"correct of 5. Thats",average*20,"% and a grade: ",chr((5-average)+65))
            else:
                print("Average:\t\tNot Taken")
            if questions[4+a][1] != "-":
                highscore=int(questions[4+a][0])
                print("Highscore:\t\t",highscore,"correct of 5 by ",questions[4+a][1],". Thats",highscore*20,"% and a grade: ",chr((5-highscore)+65))
            else:
                print("Highscore:\t\tNot Taken")
x = 0
y = 0
while x == 0:
    option = ""
    while option not in ("add user", "login", "exit"):
        option = input("Add User, Login or Exit:  ").lower()
    if option == "add user":
        adduser()
    elif option == "login":
        username = login()
        x = x + 1
    elif option == "exit":
        x = x + 1
        y = y + 1

while y == 0:
    function = ""
    while function not in ("quiz", "report", "exit"):
        function = input("Quiz, Report or exit:  ").lower()
    if function == "quiz":
        quiz(username)
    elif function == "report":
        if username == "Fer40":
            report()
        else:
            print("Not Accessible")
    elif function == "exit":
        y = y + 1