import json

db = open('db.json', "r")
database = json.load(db)
users_info = database["log_pass"]
admin_info = database["admin"]
students_info = database["students"]
teachers_info = database["teachers"]
courses_info = database["courses"]
free_c_info = database["free courses"]


class Teacher:
    def __init__(self, t_login, t_password):
        self.t_login = t_login
        self.t_password = t_password

    def teacher_can(self, t_login, t_password):
        t = Teacher(t_login, t_password)
        t_do = input('What you want to do? Please, choose number:\n' +
                     '1. See my leading courses\n' +
                     '2. Mark students(attendance)\n' +
                     '3. Add student to the course\n' +
                     '4. Delete student from the course\n' +
                     '5. Rate students(grade)\n' +
                     '6. Exit'
                     )
        if t_do == '1':
            t.t_lead_course()
        elif t_do == "2":
            t.mark_student()
        elif t_do == "3":
            t.add_stud_course()
        elif t_do == "4":
            t.del_sfrom_course()
        elif t_do == "5":
            t.rate_student()
        elif t_do == '6':
            print('You exit the program. Goodbye!')
        else:
            print("Wrong input! Try again!")
            t.teacher_can(t_login, t_password)

    def t_lead_course(self):
        for key, value in users_info["teachers"].items():
            if value["login"] == self.t_login and value["password"] == self.t_password:
                for key1, value1 in teachers_info.items():
                    if key1 == value["id"]:
                        fullname = value1["name"][0] + ". " + value1["surname"]
                        print("You are leading the course(s):")
                        for key2, value2 in courses_info.items():
                            if value2["lecturer"] == fullname or value2["practice teacher"] == fullname:
                                print("{}".format(value2["name"]))
        t = Teacher(self.t_login, self.t_password)
        t.teacher_can(self.t_login, self.t_password)

    def mark_student(self):
        for key, value in users_info["teachers"].items():
            if value["login"] == self.t_login and value["password"] == self.t_password:
                for key1, value1 in teachers_info.items():
                    if key1 == value["id"]:
                        fullname = value1["name"][0] + ". " + value1["surname"]
                        print("You are leading the course(s):")
                        for key2, value2 in courses_info.items():
                            if value2["lecturer"] == fullname or value2["practice teacher"] == fullname:
                                print("{}".format(value2["name"]))
        which = input("Choose from which course you want to mark students(write name of course):")
        for key2, value2 in courses_info.items():
            if which != value2["name"]:
                print("The course hasn't got any participants.")
                break
            elif which == value2["name"]:
                print('{}'.format(value2["participants"]))
                attend_stid = input('Choose student you want to attend(by id):')
                for k, valu in value2["participants"].items():
                    if attend_stid == k:
                        print(str(1) + '. Present\n' +
                              str(2) + '. Late\n' +
                              str(3) + '. Absent')
                        typ_attend = input('Choose option of attend:')
                        if typ_attend == '1':
                            value2["participants"][attend_stid]["attendance"]["{}-lesson".format(
                                str(len(value2["participants"][attend_stid]["attendance"]) + 1))] = "present"
                            courses_info.update()
                        elif typ_attend == '2':
                            value2["participants"][attend_stid]["attendance"]["{}-lesson".format(
                                str(len(value2["participants"][attend_stid]["attendance"]) + 1))] = "late"
                            courses_info.update()
                        elif typ_attend == '3':
                            value2["participants"][attend_stid]["attendance"]["{}-lesson".format(
                                str(len(value2["participants"][attend_stid]["attendance"]) + 1))] = "absent"
                            courses_info.update()
                        print('Attendance in this session has been recorded.')
                    else:
                        print("not working")
            with open("db.json", "w") as attach:
                json.dump(database, attach, indent=4, separators=(',', ': '))
        t = Teacher(self.t_login, self.t_password)
        t.teacher_can(self.t_login, self.t_password)

    def add_stud_course(self):
        list_course = []
        try:
            for key, value in users_info["teachers"].items():
                if value["login"] == self.t_login and value["password"] == self.t_password:
                    for key1, value1 in teachers_info.items():
                        if key1 == value["id"]:
                            fullname = value1["name"][0] + ". " + value1["surname"]
                            print("You are leading the course(s):")
                            for key2, value2 in courses_info.items():
                                if value2["lecturer"] == fullname or value2["practice teacher"] == fullname:
                                    print("{}".format(value2["name"]))
                                    list_course.append(value2["name"])
            choose = input("Name of the course: ")
            for i in range(len(list_course)):
                if list_course[i] == choose:
                    for key, value in courses_info.items():
                        if value["name"] == choose:
                            count = input("How many students do you want to add to course: ")
                            for key1, value1 in students_info.items():
                                print(key1, value1)
                            for j in range(int(count)):
                                inp = input("Enter {}-student id: ".format(str(j + 1)))
                                new_key = {inp: students_info[inp]}
                                new_key[inp]["attendance"] = {}
                                new_key[inp]["grades"] = {}
                                new_info = {
                                    key: {
                                        "name": courses_info[key]["name"],
                                        "credits": courses_info[key]["credits"],
                                        "course_type": courses_info[key]["course_type"],
                                        "lecturer": courses_info[key]["lecturer"],
                                        "practice teacher": courses_info[key]["practice teacher"],
                                        "participants": new_key
                                    }
                                }
                                courses_info[key]["participants"].update(new_info[key]["participants"])
                                with open("db.json", "w") as attach:
                                    json.dump(database, attach, indent=4, separators=(',', ': '))
                    t = Teacher(self.t_login, self.t_password)
                    t.teacher_can(self.t_login, self.t_password)
                else:
                    print("Wrong input")
                    t = Teacher(self.t_login, self.t_password)
                    t.teacher_can(self.t_login, self.t_password)
        except KeyError:
            print(KeyError)
            t = Teacher(self.t_login, self.t_password)
            t.teacher_can(self.t_login, self.t_password)

    def del_sfrom_course(self):
        list_course = []
        try:
            for key, value in users_info["teachers"].items():
                if value["login"] == self.t_login and value["password"] == self.t_password:
                    for key1, value1 in teachers_info.items():
                        if key1 == value["id"]:
                            fullname = {
                                "name": value1["name"],
                                "surname": value1["surname"]
                            }
                            print("You are leading the course(s):")
                            for key2, value2 in courses_info.items():
                                if value2["lecturer"] == fullname or value2["practice teacher"] == fullname:
                                    print("{}".format(value2["name"]))
                                    list_course.append(value2["name"])
            choose = input("Name of the course: ")
            for i in range(len(list_course)):
                if list_course[i] == choose:
                    for key, value in courses_info.items():
                        if value["name"] == choose:
                            print(value["participants"])
                            count = input("How many students do you want to delete from course: ")
                            for j in range(int(count)):
                                inp = input("Enter {}-student id: ".format(str(j + 1)))
                                del courses_info[key]["participants"][inp]
                                database.update(students_info)
                                with open("db.json", "w") as delete:
                                    json.dump(database, delete, indent=4, separators=(',', ': '))
                            print('The students are successfully  deleted.')
                else:
                    print('There is no course with this name.')
                    t = Teacher(self.t_login, self.t_password)
                    t.teacher_can(self.t_login, self.t_password)
        except ValueError:
            print(ValueError)
            t = Teacher(self.t_login, self.t_password)
            t.teacher_can(self.t_login, self.t_password)

    def rate_student(self):
        for key, value in users_info["teachers"].items():
            if value["login"] == self.t_login and value["password"] == self.t_password:
                for key1, value1 in teachers_info.items():
                    if key1 == value["id"]:
                        fullname = value1["name"][0] + ". " + value1["surname"]
                        print("You are leading the course(s):")
                        for key2, value2 in courses_info.items():
                            if value2["lecturer"] == fullname or value2["practice teacher"] == fullname:
                                print("{}".format(value2["name"]))
        which = input("Choose from which course you want to rate students(write name of course):")
        for key2, value2 in courses_info.items():
            if which == value2["name"]:
                print('{}'.format(value2["participants"]))
                attend_stid = input('Choose student you want to rate(by id):')
                for k, valu in value2["participants"].items():
                    if attend_stid == k:
                        to_what = input("For what you want to grade: ")
                        grade = int(input('Grade(0-100): '))
                        value2["participants"][attend_stid]["grades"]["{}".format(to_what)] = grade
                        courses_info.update()
                        print('Grade in this session has been recorded.')
                    with open("db.json", "w") as attach:
                        json.dump(database, attach, indent=4, separators=(',', ': '))
        else:
            print('There is no course with this name.')
        t = Teacher(self.t_login, self.t_password)
        t.teacher_can(self.t_login, self.t_password)
