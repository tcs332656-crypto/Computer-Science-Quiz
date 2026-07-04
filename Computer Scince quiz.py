
print("Welcome to a simple quiz game made by Noor to test your knowledge about computer science")
print("let the quiz begin.")
print("Important!!! Make sure do not use short forms.")
#This gives all the instructions to user before starting quiz

questions=[
    ("1. What is the denary value of 10101110?", "174"),
    ("2. What does CPU stand for?", "Central processing unit"),
    ("3. What type of software is Windows , Operating software or Application software?", "Operating software"),
    ("4. What is the first part of a data packet" , "Header"),
    ("5. What is the smallest unit of data?", "Bit"),
    ("6. What type of network usually covers a small area(be precise)?", "Local area network"),
    ("7. Which one has volatile memory Random access memory or Read only memory?", "Random access memory"),
    ("8. What software helps browse the internet? ", "Browser"),
    ("9. What input device helps in typing?", "Keyboard"),
    ("10. What output device produces printed documents?", "Printer"),
]
#list of all questions and their answers

def Quiz(question, answer):
    userinput = input(question + "  What is you answer: ")
    if userinput.lower() == answer.lower():
        print("Good job,you were correct!")
        return 1
    else:
        print("Seems like you made a mistake,the answer should have been:", answer)
        return 0
#creates a function Quiz that will work once the function is called
#this will give one mark when the user gives correct answer to the question and 0 otherwise

MARKS = 0
#this sets the initial marks to 0

for q in questions:
    MARKS += Quiz(q[0], q[1])
print("Your marks are",MARKS, "/", len(questions))
#this places questions and answers from list in q one by one
#each time it runs the if statement and according to returned value of 1 or 0 it adds it in the marks

if MARKS == 10:
    print("Brilliant! You know you computer science very well!")
elif MARKS >= 5:
    print("Good job! Try to learn from your mistakes , I am sure you will do even better next time.")
else:
    print("You need to practice more !")
#this uses if loop to give feedback about the marks obtained
