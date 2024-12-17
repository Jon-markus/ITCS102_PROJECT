#BSIT - 2A ----DE VILLA, JOHN MARC A.

import time


def tap():
    
    Esc = input("\n\nPress Enter to show the Examples: ")
    if Esc == "":
        print("\n\n\t\t\t---Example Code---")
        print()

def Overview():

    print("")
    time.sleep(0.02)
    print ("\n\t\t\t\t----------OVERVIEW----------")
    time.sleep(0.02)
    text = ("\n\n\tIn 2023, studying programming is not just about coding; it's about equipping\n\tyourself with the skills and mindset to thirive in an increasingly digital and\n\tinterconnected world. Wheter you aspire to become a software engineer, a data\n\tscientist, an entrepreneur, or simply a tech-savvy individual, programming is a\n\tskill that empowers you to innovate, solve problems, and seize opportunities in\n\tthe digital landscape.\n")
    for char in text:
            print(char,end="",flush=True)
            time.sleep(0.01)
    
#-------------------INTRODUCTION---------------------------
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



#-------------------PRINT FUNCTION---------------------------
def print_F():
    
    import time
    isFunction = True

    while isFunction == True:
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
            text5 = ("\t● Variables in programming are like named boxes that can store information.\n\t You can use variables to store any type of data, such as numbers,\n\t strings, lists, and objects.") 
            for char in text5:
                print(char,end="",flush=True)
                time.sleep(0.01)

            print("\n\n\t\t\t1\t---\tExamples")
            print("\t\t\t2\t---\tExit")


            ask = input("\n\n\t\tChoose in the following: ")
            if ask == '1':
                print("\n\n\t\t----Examples----")
                print("\n\t\t my_name = John \n\t\t i = 20\n\t\t isContinue = True")
                
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
            print ('''\t\t● String\t===\tstr ("Hello",'Word', "2005")''')
            print ("\t\t● Float\t\t===\tfloat (1.50,2005.20)")
            print ("\t\t● Boolean\t===\tbool (True,False)")
            
                #===Examples===
            ask_ex = input("\n\nPress Enter to show the Examples")
            if ask_ex == "":
                print("\n\n---Example Code---")

                print("\n\n\t==INPUT==")
                print('''\n\tage = 20 # ---Integer''')
                print('''\n\tprice = 19.99  # ---Float''')
                print('''\n\tname = "Marcus"  # ---String''')
                print('''\n\tisStudent = True  # ---Float\n\n''')

                print('''\tprint("Age: ", age) ''')
                print('''\tprint("Price: ", price)''')
                print('''\tprint("Name: ",name)''')
                print('''\tprint("Is Student: ", isStudent)''')

                print("\n\n\t==OUTPUT==")
                print('''\n\tAge: 20 ''')
                print('''\n\tPrice: 19.99 ''')
                print('''\n\tName:Marcu;s  ''')
                print('''\n\tIs Student: True \n\n''')
            elif ask_ex.lower()== 'x':
                print("\n\t\t\t===Exit===")
                break
            else:
                print("==Just Press Enter key on your Keyboard==")
        
        elif menu.lower() == 'd':
            print()
            print("\t\t\t\t----User Input----")
            text7 = ('''\n\n\tPython provides the input() function.input() reads what 
        the user types on the keyboard and return it as a string \n\n''')
            for char in text7:
                print(char,end="",flush=True)
                time.sleep(0.01)
            ask_ex3 = input("\n\nPress Enter to show the Examples: ")

            if ask_ex3 == "":
                print("\n\n\t\t---Example Code---")
                print()
                name = input("\tEnter your name: ")

                print("\n\tHi, ",name," Welcome to my program!")
                print("\n\n\t===================Code===========================")
                time.sleep(1)
                print("\n\t==INPUT==")

                print('''\t name = input("Enter your name: ")
                print("Hi,",name," Welcome to my program!) ''')
                time.sleep(1)
                print("\n\n\t==OUTPUT==")
                print('''Hi,(your input) Welcome to my program!''' )

            else: 
                print ("\n\t\t\t\t= Invalid Input =\n")
        
        elif menu.lower() == 'e':
            print ("\n\t\t\t\t= Exit =\n")
            break

        else:
            print ("\n\t\t\t\t= Invalid Input =\n")

#-------------------OPERATORS---------------------------
def operator():
    isCorrect = True
    while isCorrect == True:
        time.sleep(0.3)
        print(f"\n\n\t\t\t----Python Operators----")

        print("\n\n\t\t\t\t_option_\n\n\t\t\ta\t---\tDefinition\n\t\t\tb\t---\tTypes\n\t\t\tc\t---\tExit")
        
        time.sleep(1)
        operator = input("\n\t\tChoose in the following: ")

        if operator.lower() == 'a':
            print("\n\n\t\t\t\t----Python Operators----")
            print("")
            text8 = ('''\n\tOperators are used to perform operations on variables and values.
         ''')
            for char in text8:
                print(char,end="",flush=True)
                time.sleep(0.01)
        
        elif operator.lower() == 'b':
            text9 = ('''\n\tPython divides the operators in the following groups:''')
            for char in text9:
                print(char,end="",flush=True)
                time.sleep(0.01)

            time.sleep(0.5)

            print('''\n\t\ta\t---\tArithmetic operators
                b\t---\tAssignment operators
                c\t---\tComparison operators
                d\t---\tLogical operators
                e\t---\tExit
                    ''') 
            ask_Opera = input("\n\t\tChoose in the following: ")

            if ask_Opera.lower() == 'a':
                print ("\n\t\t\t==Arithmetic Operators==") 
                text10 = ('''\n\tArithmetic operators are used with numeric values to perform common 
                        mathematical operations:
                
               \t\tOperator\tName\n\n\t\t\t+\t\tAddition\n\t\t\t-\t\tSubtraction\n\t\t\t*\t\tMultiplication\n\t\t\t/\t\tDivision\n\t\t\t%\t\tModulus\n\t\t\t**\t\tExponentiation\n\t\t\t//\t\tFloor Division ''')
                for char in text10:
                    print(char,end="",flush=True)
                    time.sleep(0.01)
                
                print()
                tap()
                num = eval(input("\t\tEnter a number --> "))
                numb = eval(input("\t\tEnter second number --> "))

                sum = num + numb

                print("\t\tthe sum of ", num, "+",numb," = ",sum)

                print("\n\n\t\t\t==INPUT==")
                print('''\n\n\tnum = eval(input("Enter a number --> "))
        numb = eval(input("Enter second number --> "))

        sum = num + numb

        print("the sum of ", num, "+",numb," = ",sum)
''')
                print("\n\n\t===Exit===")



            elif ask_Opera.lower() == 'b':
                print ("\n\t\t\t==Assignment Operators==")
                text11 = ('''\n\tAssignment operators are used to assign values to variables:
                            =
                            +=
                            -=
                            *=
                            /=
                            %=
                            //=
                            **=  ''')
                for char in text11:
                    print(char,end="",flush=True)
                    time.sleep(0.01)
                print()
                tap()
                time.sleep(0.5)
                x = 5

                print ("\t",x)

                x+=5
                print ("\t",x)

                x += 10
                print ("\t",x)

                x += 15
                print ("\t",x)

                x +=20
                print ("\t",x)

                x += 25
                print ("\t",x)
                
                time.sleep(0.5)
                print("\n\n\t\t\t==INPUT==")
                print('''\n\n\tx = 5

        print (x)

        x+=5
        print (x)

        x += 10
        print (x)

        x += 15
        print (x)

        x +=20
        print (x)

        x += 25
        print (x)
''')
                print("\n\n\t===Exit===")

            
            elif ask_Opera.lower() == 'c':
                print ("\n\t\t\t==Comparison operators==")
                text12 = ('''\n\tComparison operators are used to compare two values:
                            ==\tEqual
                            !=\tNot Equal
                            >\tGreater Than
                            <\tLess Than
                            >=\tGreater Than or Equal to
                            <=\tLess Than or Equal to
                            ''')
                for char in text12:
                    print(char,end="",flush=True)
                    time.sleep(0.01)
                print()
                tap()
                print()
                Age = eval(input("\n\t\tEnter your age ---> "))

                #1-7 - Toddler
                #8-13 - pre teen
                #14-18 - teenager
                #19-31 - early adulthood
                #32-45 - Mid adulthood
                #46-59 - post adulthood
                #60 + - senior

                if Age <= 7:
                    print("\t\tYour age is categorized as toddler")

                elif Age <= 13 and Age >= 8:
                    print ("\t\tYour age is categorized as Pre teen")

                elif Age <=18 and Age >=14:
                    print ("\t\tYour age is categorized as Teenager")

                elif Age <=31 and Age >= 19:
                    print ("\t\tYour age is categorized as Early Adulthood")

                elif Age <=45 and Age >= 32: 
                    print ("\t\tYour age is categorized as Mid Adulthood")

                elif Age <= 59 and Age >= 46:
                    print ("\t\tYour age is categorized as Post Adulthood")

                elif Age >= 60:
                    print ("\t\tYour age is categorized as Senior")

                print("\n\n\t\t\t==INPUT==")
                print('''\n\n\tAge = eval(input(" Enter your age ---> "))

                #1-7 - Toddler
                #8-13 - pre teen
                #14-18 - teenager
                #19-31 - early adulthood
                #32-45 - Mid adulthood
                #46-59 - post adulthood
                #60 + - senior

                if Age <= 7:
                    print("Your age is categorized as toddler")

                elif Age <= 13 and Age >= 8:
                    print ("Your age is categorized as Pre teen")

                elif Age <=18 and Age >=14:
                    print ("Your age is categorized as Teenager")

                elif Age <=31 and Age >= 19:
                    print ("Your age is categorized as Early Adulthood")

                elif Age <=45 and Age >= 32: 
                    print ("Your age is categorized as Mid Adulthood")

                elif Age <= 59 and Age >= 46:
                    print ("Your age is categorized as Post Adulthood")

                elif Age >= 60:
                    print ("Your age is categorized as Senior")
''')
                print("\n\n\t===Exit===")

            elif ask_Opera.lower() == 'd':
                print ("\n\t\t\t\tLogical Operators\n")


            elif ask_Opera.lower() == 'e':
                print ("\n\t\t\t\t= Exit =\n")
            
            else:
                print ("\n\t\t\t\t= Invalid Input =\n")


    
    

def conditional_St():
    pass

def Looping():
    pass

def List():
    pass



operator()
# print_F()
# isContinue = True

# while isContinue:
#     pass
