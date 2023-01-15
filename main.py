class Item:
    def __init__(self, case, time, priority):
        """Initializing class attributes"""
        self.case = case
        self.time = time
        self.priority = priority

    def change_case(self, new_name):
        """Changing the case name attribute"""
        self.case = new_name

    def change_time(self, new_time):
        """Changing the case name attribute"""
        self.time = new_time

    def change_priority(self, new_priority):
        """Changing the period of execution attribute"""
        self.priority = new_priority

    def print_case(self):
        """Output of information about the case"""
        print(f"Case: {self.case}")
        print(f"Period of execution: {self.time}")
        print(f"Case priority: {self.priority}")


class ItemList(Item):
    def __init__(self, case, time, priority):
        super().__init__(case, time, priority)
    case_list = {}

    def add_case(self):
        """Adding a new case to the list from the Item class"""
        self.case_list[self.case] = [self.time, self.priority]

    def add_new_case(self, case, time, priority):
        """Adding a new case to the list"""
        self.case_list[case] = [time, priority]

    def del_case(self, case):
        """Deleting a case"""
        del self.case_list[case]
        print(f"Case: {self.case_list[case]} was deleted")

    def print_all(self):
        """Output a list of all cases"""
        number = 0
        for key, value in self.case_list.items():
            number += 1
            if number == 1:
                print('-' * max(len(key), len(value[0]), len(value[1]) + len("Period of execution: ")))
            print(f"Case №{number}: {key}")
            print(f"Period of execution: {value[0]}")
            print(f"Case priority: {value[1]}")
            print('-' * max(len(key), len(value[0]), len(value[1]) + len("Period of execution: ")))

    def get_by_date(self, *date):
        """Getting cases by date"""
        for t in date:
            for key, value in self.case_list.items():
                if value[0] == t:
                    print(f"Case: {key}")
                    print(f"Period of execution: {value[0]}")
                    print(f"Case priority: {value[1]}")
                    print('-' * max(len(key), len(value[0]), len(value[1]) + len("Period of execution: ")))

    def get_by_priority(self):
        """Getting cases by priority"""
        minn = 1000000
        try:
            for key, value in self.case_list.items():
                minn = min(int(value[1]), minn)
        except:
            print("Error. The priority of the case should be in the form of a number in string format.")

        for key, value in self.case_list.items():
            try:
                if int(value[0]) == minn:
                    print(f"Case: {key}")
                    print(f"Period of execution: {value[0]}")
                    print(f"Case priority: {value[1]}")
                    print('-' * max(len(key), len(value[0]), len(value[1]) + len("Period of execution: ")))
            except:
                print("")

    def change_attribute(self, case, attribute, new_attribute):
        """Changing attributes of a specific case"""
        attribute = str(attribute)
        attribute.lower()
        try:
            if attribute == "case":
                value = self.case_list[case]
                del self.case_list[case]
                self.case_list[new_attribute] = value

            elif attribute == "period of execution":
                value = self.case_list[case]
                value[0] = new_attribute
                self.case_list[case] = value

            else:
                value = self.case_list[case]
                value[1] = new_attribute
                self.case_list[case] = value
        except:
            print("Check the spelling of the selected argument (Case, period of execution, priority).")


case_count = int(input("Enter the number of cases: "))
if case_count > 0:
    print("Enter: case name, period of execution, case priority")
    print("Example: Exams, Jun 20, 1")
try:
    for i in range(case_count):
        case_name = input()
        case_time = input()
        case_priority = input()
        myCase = ItemList(case_name, case_time, case_priority)
        ItemList.add_case(myCase)
        myCase.change_attribute("Abra", "case", "Jun 100")
    else:
        myCase.print_all()
except:
    print("Error")
