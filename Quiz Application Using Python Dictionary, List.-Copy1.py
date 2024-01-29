#!/usr/bin/env python
# coding: utf-8

# In[65]:


questions = ("Who is the Prime Minister Of India?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Up Ram Mandir Prana Prathisthapana Date?: ")



# In[66]:


feedback = ("How Was your Experience Give a Value Feedback")
            


# In[67]:


options_1= ("A.Excellent", "B.Good"," C.Minute Mistake", "D.Bad")



# In[69]:


options = (("A. Modi", "B. Rahul Gandhi", "C.Atal Bihari Vajpayee ", "D.Chandrashekhar"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A.20th Dec 2023","B.21 Dec 2023", "C.22nd jan 2024","D.21rst jan 2024"))


# In[70]:


answers = ("A", "D", "A", "A", "C")
guesses = []
score = 0
question_num = 0
Feedback_no = 0
Feedback_answer = ("A","B","C","D")
guesses_1=[]


# In[71]:


for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

print("----------------------")
print("     Feedback         ")
print("----------------------")

for feedbacks in feedback:
    print("----------------------")
    print(feedback)
    for option in options_1 [Feedback_no]:
        print(options_1)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses_1.append(guess)
    if guess == Feedback_answer[Feedback_no]:
    
        print("Thank You For Your Feedback!")
    else:
        print(f"{Feedback_answer[Feedback_no]} Thank You For Your Feedback!")
    
    Feedback_no =feedback


# In[ ]:





# In[ ]:




