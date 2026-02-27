# FILE NAME - grade_converter.py

# NAME: Kanna Sugiyama
# DATE: February 27, 2026 
# BRIEF DESCRIPTION: This experience will ask for a percentage and return the corresponding letter grade.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print()
print("===== Grade Converter =====")

numerical_grade = int(input("Enter a numerical grade (1-100): "))

if numerical_grade > 100:
    print("A+")
elif numerical_grade >=90:
    print("A")
elif numerical_grade >=80:
    print("B")
elif numerical_grade >=70:
    print("C")
elif numerical_grade >=65:
    print("D")
elif numerical_grade < 65:
    print("F")





########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?
I would like to tell the future students that the order matters because I remember when I did this for the first time when I was still a very beginner
of coding, almost every input became D because the order was upside down. For example, both 100 and 66 fall for the category "> 65", which is D.






'''
