#BSIT - 2A ----DE VILLA, JOHN MARC A.

import time
import os

def clear_S():
    input("\n\n-----PRESS ENTER TO PROCEED TO THE NEXT PART-----")
    os.system()

def Overview():

    print("")
    time.sleep(0.02)
    print ("\n\t\t\t\t----------OVERVIEW----------")
    time.sleep(0.02)
    text = ("\n\n\tIn 2023, studying programming is not just about coding; it's about equipping\n\tyourself with the skills and mindset to thirive in an increasingly digital and\n\tinterconnected world. Wheter you aspire to become a software engineer, a data\n\tscientist, an entrepreneur, or simply a tech-savvy individual, programming is a\n\tskill that empowers you to innovate, solve problems, and seize opportunities in\n\tthe digital landscape.\n")
    for char in text:
            print(char,end="",flush=True)
            time.sleep(0.01)
    

def Introduction():

    isContinue = True
    while isContinue == True:
        time.sleep(0.3)
        print(f"\n\n\t\t\t----Python as a Programming Language----")

        print("\n\n\t\t\t\t\t_option_\n\n\t\t\ta\t---\tWhat is Python?\n\t\t\tb\t---\tHistory of Python\n\t\t\tc\t---\tFeatures of Python\n\t\t\td\t---\tExit")
        
        time.sleep(1)
        Pili = input("\n\t\tChoose in the following: ")


        #What is Python
        if Pili.lower() == 'a':
            print ()
            print ("\t\t\t\t------What is Python?------")
            print ()

            text1 = ("\tPython is a dynamic, interpreted language without type declarations in its source code,\n\tmaking it concise and flexible. While it lacks compile-time type checking, it tracks\n\ttypes at runtime and raises errors when incompatible code is executed.\n\tPython is a versatile and beginner-friendly programming language widely used in fields\n\tlike data science and web development. Ranked among the top 10 'MOST POPULAR' and 'MOST LOVED'\n\ttechnologies, it empowers users to create almost anything.\n\n ")
            for char in text1:
                print(char,end="",flush=True)
                time.sleep(0.01)

        #History of Python
        elif Pili.lower() == 'b':
            print ()
            print ("\t\t\t\t-----History of Python-----")
            text2 = ("\n\n\tA Dutch-American computer programmer named Guido van Rossum created what is known as the Python\n\tprogramming language, first released in the early 1990s.\n\n\n\t● The development environment IDLE provided with Python comes from the name of a\n\t  member of the comic group.\n\n\t● Python has a simple syntax.\n\n\t● Python programs are clear and easy to read.\n\n\t● Python provides powerful programming features, and is widely used.\n\n\t● Companies and organizations that use Python include YouTube, Google, Yahoo, and NASA. Python is well\n\t  supported and freely available at www.python.org.\n\n")
            for char in text2:
                print(char,end="",flush=True)
                time.sleep(0.01)
            continue

        #Features of Python
        elif Pili.lower() == 'c':
            print()
            print("\t\t\t\t-----Features of Python------")
            
            text3 = ("\n\n\t\t● Object Oriented and Functional\n\t\t● Free\n\t\t● Portable \n\t\t● Powerful\n\t\t● Mixable\n\t\t● Easy to use\n\t\t● Easy to Learn\n\n")
            for char in text3:
                print(char,end="",flush=True)
                time.sleep(0.01)
            continue

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
        print("\t\t\t\t----Print Statement----")
        print()
        print("\n\t\t\t\t\t_option_")
        print("\n\t\t\ta\t---\tComment")
        print("\t\t\tb\t---\tVariables")
        print("\t\t\tc\t---\tData Types")
        print("\t\t\td\t---\tUser Input")
        print("\t\t\te\t---\tExit")
        print()
        time.sleep(0.5)
        menu= input("Choose in the Following: ")

        if menu.lower() == 'a':
            print()
            print("\t\t\t\t----Comment----")
            print("")
            text4 = ("\tComments in Python are pieces of text that are ignored by the Python interpreter. They are\n\tused to Explain the code to reader, or to disable code that you don't want to run.") 
            for char in text4:
                print(char,end="",flush=True)
                time.sleep(0.01)
            
            #Type of Comments in Python
            time.sleep(0.5)
            print ("\n\n\t\tTypes of Comments in Python")
            print("\n\t\t\t\t\t_option_")
            print("\n\t\t\t1\t---\tSingle-line Comment\n\t\t\t2\t---\tMulti-line Comment\n\t\t\t3\t---\tExamples\n\t\t\t4\t---\tExit")
            comment = input("\n\nChoose in the Following: ")

            if comment == '1':
                print("\n\n\t\t\t-----Single-Line Comment------")
                print("\t● Start with a hashtag symbol (#) and go to the end of the line.")
                

            elif comment == '2':
                print("\n\n\t\t\t-----Multi-Line Comment------")
                print('''\t● Start with three double quotes(""") and end with three double quotes''')
                
            elif comment == '3':
                print("\n\n\t\t\t-----Examples------")
                print("\n\t---Single-Line Comments---")
                print('''\t\t#This is a Single-Line Comment''')
                print("\n\t---Multi-Line Comments---")
                print('''\t\t"""
                This is a multi-line cooment.
                """ ''')

            elif comment == '4':
                print("\n\t\t\t\t\t---Exit---")
                isContinue = False
            
            else:
                print ("\n\t\t\t\t= Invalid Input =\n")
                
        
        elif menu.lower() == 'b':
            print()
            print("\t\t\t\t----Variables----")
            print("")
            text5 = ("\t● Variables in programming are like named boxes that can store information.\n\t You can use variables to store any \n\ttype of data, such as numbers, strings, lists, and objects.") 
            for char in text5:
                print(char,end="",flush=True)
                time.sleep(0.01)

            print("\n\n\t\t\t1\t---\tExamples")
            print("\t\t\t2\t---\tExit")


            ask = input("\n\n\t\tChoose in the following: ")
            if ask == '1':
                print("\n\n\t\t----Examples----")
                print("\n\t\t[ my_name = John ]\n\t\t[ i = 20 ]\n\t\t[ isContinue = True ]")
                
            elif ask == '2':
                print("\n\t\t\t\t\t---Exit---")
                
            else:
                print ("\n\t\t\t\t= Invalid Input =\n")
        
        elif menu.lower() == 'c':
            print()
            print("\t\t\t\t----Data types----")
            text6 = ("\n\n\tPython data types identify the type of data that a variable can store. ")
            for char in text6:
                print(char,end="",flush=True)
                time.sleep(0.01)
            print ("\n\tPython has the following data types built-in by default\n")
            print ("\t\t● Integers\t===\tint (123,1000)")
            print ('''● String\t===\tstr ('Hello','Word')''')



            

            






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
    
    
    



print_F()
# isContinue = True

# while isContinue:
#     pass
