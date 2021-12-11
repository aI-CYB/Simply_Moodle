import json

db = open('db.json', "r")
database = json.load(db)
users_info = database["log_pass"]
admin_info = database["admin"]
students_info = database["students"]
teachers_info = database["teachers"]
courses_info = database["courses"]
free_c_info = database["free courses"]


class Student:
    def __init__(self, s_login, s_password):
        self.s_login = s_login
        self.s_password = s_password

    def student_can(self):
        s = Student(self.s_login, self.s_password)
        s_do = input('What you want to do? Please, choose number:\n' +
                     '1. Enroll to free courses\n' +
                     '2. Unenroll from free courses\n' +
                     '3. see all marks\n' +
                     '4. see specific subject mark\n' +
                     '5. See teachers\n' +
                     '6. See free courses to enroll\n' +
                     '7. Rate teacher (can be done only once)\n' +
                     '8. Exit'
                     )
        for key, value in users_info["students"].items():
            if s_do == '1':
                s.enroll_for_freecourse(value["id"])
            elif s_do == "2":
                s.unenroll_for_freecourse(value["id"])
            elif s_do == "3":
                s.see_all_marks(value["id"])
            elif s_do == "4":
                s.see_specific_course_mark(value["id"])
            elif s_do == "5":
                s.see_teacher(value["id"])
            elif s_do == "6":
                s.see_freecourses()
            elif s_do == "7":
                s.rate_teachers(value["id"])
            elif s_do == '8':
                print('You exit the program. Goodbye!')
            else:
                print("Wrong input!")
                s = Student(self.s_login, self.s_password)
                s.student_can()

    # def s_signin(self, s_login, s_password):
    #     for key, value in users_info["students"].items():
    #         if s_login == value["login"] and s_password == value["password"]:
    #             return True
    #         else:
    #             return False

    def enroll_for_freecourse(self, st_id):
        for key, value in free_c_info.items():
            left = int(value["number of places"]) - len(value["participants"])
            print(key, value, " Left places to enroll: ", left)
        choose_c_id = input("Choose course id: ")
        new_key = {st_id: students_info[st_id]}
        new_info = {
            choose_c_id: {
                "name": free_c_info[choose_c_id]["name"],
                "number of places": free_c_info[choose_c_id]["number of places"],
                "author": free_c_info[choose_c_id]["author"],
                "participants": new_key
            }}
        if len(free_c_info[choose_c_id]["participants"]) <= int(free_c_info[choose_c_id]["number of places"]):
            free_c_info[choose_c_id]["participants"].update(new_info[choose_c_id]["participants"])
            with open("db.json", "w") as attach:
                json.dump(database, attach, indent=4, separators=(',', ': '))
        else:
            print("There is limit to enroll to this course")
            s = Student(self.s_login, self.s_password)
            s.student_can()

    def unenroll_for_freecourse(self, st_id):
        print("My courses: ")
        for key, value in free_c_info.items():
            for key1 in value["participants"]:
                if key1 == st_id:
                    print(key, value["name"])
        choose = input("ID of course:")
        del free_c_info[choose]["participants"][st_id]
        free_c_info[choose]["participants"].update(free_c_info[choose]["participants"])
        with open("db.json", "w") as attach:
            json.dump(database, attach, indent=4, separators=(',', ': '))
        s = Student(self.s_login, self.s_password)
        s.student_can()

    def see_all_marks(self, st_id):
        for key, value in courses_info.items():
            for key1 in value["participants"]:
                if key1 == st_id:
                    print(key, value["name"], courses_info[key]["participants"][st_id]["grades"])
        else:
            s = Student(self.s_login, self.s_password)
            s.student_can()

    def see_specific_course_mark(self, st_id):
        for key, value in courses_info.items():
            for key1 in value["participants"]:
                if key1 == st_id:
                    print(key, value["name"])
        choose = input("Course ID: ")
        print(courses_info[choose]["participants"][st_id]["grades"])
        s = Student(self.s_login, self.s_password)
        s.student_can()

    def see_teacher(self, st_id):
        for key, value in courses_info.items():
            for key1 in value["participants"]:
                if key1 == st_id:
                    print(key, value["name"], "Lecturer: ", value["lecturer"], "Practicioner: ",
                          value["practice teacher"])
                else:
                    s = Student(self.s_login, self.s_password)
                    s.student_can()

    def see_freecourses(self):
        for key, value in free_c_info.items():
            left = int(value["number of places"]) - len(value["participants"])
            print(key, value, " Left places to enroll: ", left)
        s = Student(self.s_login, self.s_password)
        s.student_can()

    def rate_teachers(self, st_id):
        for key, value in courses_info.items():
            for key1 in value["participants"]:
                if key1 == st_id:
                    print(key, value["name"], "Lecturer: ", value["lecturer"]["name"],
                          value["lecturer"]["surname"])
                    for key2, value2 in teachers_info.items():
                        lec_name = value["lecturer"]["name"]
                        lec_surname = value["lecturer"]["surname"]
                        if value2["name"] == lec_name and value2["surname"] == lec_surname:
                            if bool(value2["rates"]) is False:
                                quality = input("How do you evaluate quality of teach methods of {}".format(
                                    value["lecturer"]["name"],
                                    value["lecturer"]["surname"]))
                                comment = input("Comments: ")
                                new_rate = {
                                    st_id: {
                                        "author": students_info[st_id]["name"] + " " + students_info[st_id][
                                            "surname"],
                                        "quality": quality,
                                        "comment": comment
                                    }
                                }
                                new = {
                                    key2: {
                                        "name": teachers_info[key2]["name"],
                                        "surname": teachers_info[key2]["surname"],
                                        "subject": teachers_info[key2]["subject"],
                                        "email": teachers_info[key2]["email"],
                                        "gender": teachers_info[key2]["gender"],
                                        "rates": new_rate
                                    }
                                }
                                teachers_info.update(new)
                                database.update(teachers_info)
                                with open("db.json", "w") as attach:
                                    json.dump(database, attach, indent=4, separators=(',', ': '))
                            elif bool(value2["rates"]) is True:
                                for key3 in value2["rates"]:
                                    if key3 == st_id:
                                        print("Your rate for this teacher is already saved to database."
                                              "You had only one permission to rate each teacher.")
                                        s = Student(self.s_login, self.s_password)
                                        s.student_can()
