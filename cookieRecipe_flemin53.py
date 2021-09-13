"""
Author: Your Name, flemin53@purdue.edu
Assignment: m.n - Cookie Recipe
Date: 09/13/2021

Description:
This program takes a desired amount of cookies as input and outputs required ingredients

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""


def main():
    C = float(input("How many cookies do you want to make? "))
    S = C * (1.75/48) #This line multiplies desired cookies by the ratio of cups of sugar to cookies for an exact float
    B = C * (1/48) #This formula multiplies desired cookies by the ratio of cups of butter to cookes
    F = C * (2.5/48) #And obviously this is for flour
    print (
    'To make ', C, ' cookies, you will need:\n',
    format(S,'7.2f'), " cups of sugar\n",
    format(B,'7.2f'), " cups of butter\n",
    format(F,'7.2f'), " cups of flour")

if __name__ == '__main__':
    main()
