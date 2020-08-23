#Made by: John Mai
#Date: 8/23/2020
#Project Description: In my AMS20 Linear Algebra class, our overall grade was based on
#the highest of the following FOUR options below. I've created a program to calculate
#which option provides them the highest final grade based off their 3 midterm scores
#and final score.

#Option 1: Midterm Exam 1 (15%), Midterm Exam 2 (15%), Midterm Exam 3 (15%), Final Exam (55%)
#Option 2: Midterm Exam 1 (25%), Midterm Exam 2 (25%), Midterm Exam 3 (25%), Final Exam (25%)
#Option 3: Final Exam (100%)
#Option 4: The average of the three midterm exams if the average score of the three midterm exams is higher than or equal to 75%.

def option_one(me_one, me_two, me_three, final):
    one_end_result = (0.15 * me_one) + (0.15 * me_two) + (0.15 * me_three) + (0.55 * final)
    return one_end_result

def option_two(me_one, me_two, me_three, final):
    two_end_result = (0.25 * me_one) + (0.25 * me_two) + (0.25 * me_three) + (0.25 * final)
    return two_end_result

def option_three(final):
    three_end_result = final
    return three_end_result

def option_four(me_one, me_two, me_three):
    four_end_result = (me_one + me_two + me_three)/3
    return four_end_result

calculating = True

while calculating:

    print("Input your test scores")

    me_one = float(input("Enter the score of your midterm 1: "))
    me_two = float(input("Enter the score of your midterm 2: "))
    me_three = float(input("Enter the score of your midterm 3: "))
    final = float(input("Enter the score of your final: "))

    print("---------------------------------------------------------")

    a = option_one(me_one, me_two, me_three, final)
    print("Option One gives you a final grade of: ", a)

    b = option_two(me_one, me_two, me_three, final)
    print("Option Two gives you a final grade of: ", b)

    c = option_three(final)
    print("Option Three gives you a final grade of: ", c)

    d = option_four(me_one, me_two, me_three)
    print("Option Four gives you a final grade of: ", d)

    print("---------------------------------------------------------")

    if a > b and a > c and a > d:
        print("Option 1 gives you the highest final grade")

    elif b > a and b > c and b > d:
        print("Option 2 gives you the highest final grade")

    elif c > a and c > b and c > d:
        print("Option 3 gives you the highest final score")

    elif d > a and d > b and d > c:
        print("Option 4 gives you the highest final score")

    print("---------------------------------------------------------")

    calculate_again=str(input("Do you want to calculate again? Type Y or N: "))
    if calculate_again == "N":
        calculating = False



