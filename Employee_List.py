idlist = [1, 2, 3, 4]
name_list = ["ahmed ali", "ali ahmed", "amr ahmed", 'ali mahmoud']
sal_list = [2000, 3000, 4000, 5000]
dep_list = ['finance', "HR", 'Eng', 'HR']

employees_list = [{"Name": "ahmed ali", "id": 1, "sal": 300, "dep": "finance"},
                  {"Name": "ali ahmed ", "id": 2, "sal": 400, "dep": "HR"},
                  {"Name": "amr ahmed", "id": 3, "sal": 500, "dep": "ENG"},
                  {"Name": "ali mahmoud", "id": 4, "sal": 600, "dep": "HR"}]

print("1-new\n2-search\n3-delete\n4-show all\n4-quit\n ")
while (1):
    try:
        process = int(input("choose process : "))
    except ValueError:
        print("please enter numbers")
        continue

    if (process == 1):
        new = input("Enter name , salary , dep:").lower() #to store all data lower
        newlist = new.split(",")
        new_name=newlist[0].split()
        for name in new_name:
            if not name.isalpha() :
                print("your name must be characters only")

        new_dep = newlist[2].split()
        for dep in new_name:
            if not dep.isalpha():
                print("your name must be characters only")



        newdic={"Name": newlist[0], "id": employees_list[-1]["id"]+1, "sal": newlist[1], "dep": newlist[2]}

        employees_list.append(newdic)
        print("all employees :")
        for index in range(len(employees_list)):
            print(employees_list[index])

    elif (process == 2):
        new = input("search by first name ").lower()
        if not new.isalpha() :
            print("your search must be with characters only")
            continue

        flag=0;  #to give a message for user if his search doesn't exist

        for dic in employees_list:
            if dic["Name"].split()[0]==new :
                print(dic)
                flag=1

        if flag==0:
            print("this employee doesn't exist")



    elif (process == 3):

        new = input("delete which by first name: ").lower()

        if not new.isalpha():
            print("your search must be with characters only")
            continue

        flag = 0;  # to give a message for user if his search doesn't exist

        for dic in (employees_list):

            if dic["Name"].split()[0]== new:
                print("you deleted this employee successfully", dic)
                employees_list.remove(dic)
                flag = 1
                print("list of employees become now :")

                for index in range(len(employees_list)):
                    print(employees_list[index])


        if flag == 0:
            print("this employee doesn't exist")


    elif (process == 4):

        print("all employees :")

        for index in range(len(employees_list)):
            print(employees_list[index])


    elif (process == 5):
        print("thanks our best expert")
        break