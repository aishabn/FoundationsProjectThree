# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!

        self.name = name
        self.bio = bio
        self.age = age
        


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.members = []
        self.president = " "


    def assign_president(self, person):
        # your code goes here!

        if person not in self.members:
            self.president.append(person)


    def recruit_member(self, person):
        # your code goes here!

        if person not in self.members:
            self.members.append(person)


    def print_member_list(self):
        # your code goes here!

            print ("Members: \n")
            for mem in self.members:
                if mem == self.president:
                    print("- %s (%s years old, President) - %s" % (mem.name, mem.age, mem.bio)) 
                else:
                    print("- %s (%s years old) - %s" % (mem.name, mem.age, mem.bio))
                print()

            sum_age = 0
            total = len(self.members)
            for person in self.members:
                sum_age += mem.age

            avg = sum_age/total

            print("Average age in this club: %s" % avg)




