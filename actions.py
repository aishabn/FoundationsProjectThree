# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Aisha"
my_age = 25
my_bio = " "
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!

    print ("Would you like to: \n")
    print ("1) Create a new club. \n or: \n 2) Browse and join clubs. \n or: \n 3) View existing clubs. \n or: \n 4) Display members of a club. \n or: \n -1) Close application. \n")
    inpt = input()

    return inpt

def create_club():
    # your code goes here!

    print ("Pick a name for your awesome new club: ")
    club_name = input()
    print ("What is your club about?")
    des = input()

    new_club = Club(club_name, des)

    return new_club
    

def view_clubs():
    # your code goes here!

    for club in clubs:
    	print ("\t NAME: %s \n \tDESCRIPTION: %s \n \tMEMBERS: %s \n\n" % (club.name, club.description, len(club.members)))

    
    

def view_club_members():
    # your code goes here!
    print ("Enter the name of the club whose members you'd like to see: ")
    inpt = input()

    for c in clubs:
        if c.name == inpt:
            c.print_member_list()
    	
    

def join_clubs():
    # your code goes here!


    inpt = input("Enter the name of the club you'd like to join: ")
    club_name = inpt

    for c in clubs:
        if c.name == inpt:
            club_name.recruit_member(my_name)

    print (" %s just joined %s!" %(my_name, club_name))
    

def application():
    introduction()
    # your code goes here!
    op = options()
    

    if op == '1':
        new_club = create_club()
            
        print("Enter the numbers of the people you would like to recruit (-1 to stop)")
            
        counter = 1
        for i in population:
            print ("[%s] %s \n" % (counter, i.name))
            counter+=1

        inpt = input()
        while inpt != '-1':
            new_club.recruit_member(inpt)
            inpt = input()

        print ("Here's your club: \n %s \n %s \n" %(new_club.name, new_club.description))

    elif op == '2':
        view_clubs()
        join_clubs()

    elif op == '3':
        view_clubs()

    elif op == '4':
        view_clubs()
        view_club_members()

    else:
        if op == '-1':
            print ("END")

    
        



    
