import time
print("--------------------------------------------------")
#Welcome the user
print("Welcome to Know Your Country Game!")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("You have to pick", chances,"correct answer.\nYou will get 1 score if you pick a correct answer.\n")
time.sleep(2)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) WHO IS OUR FIRST PRIME MINISTER?\n(A) NAJIB RAZAK\n(B) MAHATHIR MOHAMAD\n(C) ABDUL RAHMAN\n(D) ABDUL RAZAK\n\n")
answer_1= "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2)WHAT IS OUR NATIONAL SONG?\n(A) JALUR GEMILANG\n(B) NEGARAKU\n(C) NEGERIKU\n(D) MERDEKA\n\n")  
answer_2 = "b"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3)  HOW MANY STATES IN MALAYSIA?\n(A) 15\n(B) 16\n(C) 14\n(D) 12\n\n")
answer_3= "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  WHEN DID WE CELEBRATE NATIONAL DAY?\n(A) 16 SEPTEMBER\n(B) 12 MARCH\n(C) 31 DECEMBER\n(D) 31 OGOS\n\n")
answer_4= "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  WHO IS THE CREATOR OF JALUR GEMILANG?\n(A) MOHAMED BIN HAMZAH\n(B) ANUAR BIN IBRAHIM\n(C) HASSAN BIN ALI\n(D) SOFIAN BIN ADAM\n\n")
answer_5= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("well done! Your Score was", score)
    break

while score <2:
    print("Better luck next time! Your score was",score)
    break

#Goobye message
print("Thank you for playing the Music Quiz Game!")
