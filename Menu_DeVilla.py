#-----------MENU----------------

def Overview():

    print("")
    print ("\n\t\t\t\t----------OVERVIEW----------")
    print ("\n\n\tIn 2023, studying programming is not just about coding; it's about equipping")
    print ("\tyourself with the skills and mindset to thirive in an increasingly digital and")
    print ("\tinterconnected world. Wheter you aspire to become a software engineer, a data")
    print ("\tscientist, an entrepreneur, or simply a tech-savvy individual, programming is a")
    print ("\tskill that empowers you to innovate, solve problems, and seize opportunities in")
    print ("\tthe digital landscape.\n\n") 

def Introduction():

    import time

    isContinue = True
    while isContinue == True:
         
        print ("")
        print("\t\t\t----Python as a Programming Language----")
        time.sleep(0.5)
        print("\t       _option_")
        print("\n\ta\t---\tWhat is Python?")
        print("\tb\t---\tHistory of Python")
        print("\tc\t---\tFeatures of Python")
        print("\td\t---\tBack")
        print ("")
        print("")

        time.sleep(1)
        Pili = input("\t\tChoose in the following: ")
        if Pili.lower() == 'a':
            print ()
            print ("\t\t\t\t------What is Python?------")
            print ()

            print ("\tPython is a dynamic, interpreted language without type declarations in its source code,")
            print ("\tmaking it concise and flexible. While it lacks compile-time type checking, it tracks")
            print ("\ttypes at runtime and raises errors when incompatible code is executed.")
            print ()
            print("\tPython is a versatile and beginner-friendly programming language widely used in fields ")
            print("\tlike data science and web development. Ranked among the top 10 'MOST POPULAR' and 'MOST LOVED'")
            print("\ttechnologies, it empowers users to create almost anything.\n\n")

        
        elif Pili.lower() == 'b':
            print ()
            print ("\t\t\t\t-----History of Python-----")
            print ("\n\n\tA Dutch-American computer programmer named Guido van Rossum created what is known as the Python")
            print ("\tprogramming language, first released in the early 1990s.")
            print ("\n\n\t● The development environment IDLE provided with Python (discussed below) comes from the name of a")
            print ("\t  member of the comic group.")
            print ("\n\t● Python has a simple syntax.")
            print ("\n\t● Python programs are clear and easy to read.")
            print ("\n\t● Python provides powerful programming features, and is widely used.")
            print("\n\t● Companies and organizations that use Python include YouTube, Google, Yahoo, and NASA. Python is well")
            print("\t  supported and freely available at www.python.org.\n\n")

        
        elif Pili.lower() == 'c':
            print()
            print("\t\t\t\t-----Features of Python------")
            
            print ("\n\n\t\t● Object Oriented and Functional\n\t\t● Free\n\t\t● Portable \n\t\t● Powerful\n\t\t● Mixable\n\t\t● Easy to use\n\t\t● Easy to Learn\n\n")

        elif Pili.lower() == 'd':
            print("\n\t\t\t\t\t---Exit---")
            isContinue = False
        
        else:
            print ("\n\t\t\t\t= Invalid Input =\n")




def print_F():
    
    import time
    isContinue = True

    while isContinue == True:
        print()
        print("\t\t----Print Statement----")
        print()
        print("\t\t_option_")
        print("\t\t\ta\t---\tComment")
        print("\t\t\tb\t---\tVariables")
        print("\t\t\tc\t---\tData Types")
        print("\t\t\td\t---\tUser Input")
        print("\t\t\te\t---\tBack")
        print()
        time.sleep(0.5)
        menu= input("Choose in the Following: ")

        if menu.lower() == 'a':
            print()
            print("\t\t----Comment----")
            print("")
            print("\t")


def d():
    pass

def e():
    pass

def f():
    pass

def g():
    pass

def h():
    pass

Overview()
Introduction()
print_F()
# isContinue = True

# while isContinue:
#     pass
