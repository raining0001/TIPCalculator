class Main:
    def __init__(self, total=0, people=0, percent=0):
        self.total = total
        self.people = people
        self.percent = percent
        self.total_w = 0
        self.final_total = 0  # Added instance variable for final total
        self.tip_yn = ""  # Added instance variable for tip yes/no

    def ask_user(self):
        self.total = float(input("What was the total bill?  "))
        self.tip_yn = input("Would you like to leave a tip? Type Y or N: ")
        self.total_w += self.total

    def no_tip(self):
        self.people = int(input("How many people to split the bill?  "))
        self.final_total = self.total_w / self.people

    def tip_calculator(self):
        self.percent = int(input("What percentage would you like to give? 10, 12, or 15? "))
        self.people = int(input("How many people to split the bill?  "))
        self.total_p = (self.total * self.percent) / 100
        self.total_f = (self.total + self.total_p) / self.people
