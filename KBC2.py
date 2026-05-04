print("WELCOME TO KBC")
Questions = [
    ["International Literacy Day is observed on:", "Sep 8", "Nov 28", "May 2", "Sep 22", 1],
    ["The language of Lakshadweep, a Union Territory of India, is:", "Tamil", "Hindi", "Malayalam", "Telugu", 3],
    ["In which group of places is the Kumbha Mela held every twelve years?", "Ujjain, Puri, Prayag, Haridwar", "Prayag, Haridwar, Ujjain, Nasik", "Rameshwaram, Puri, Badrinath, Dwarika", "None of These", 2],
    ["Bahubali festival is related to:", "Islam", "Hinduism", "Buddhism", "Jainism", 4],
    ["Which day is observed as the World Standards Day?", "June 26", "Oct 14", "Nov 15", "Dec 2", 2],
    ["Which of the following was the theme of the World Red Cross and Red Crescent Day?", "Dignity for all-focus on women", "Dignity for all-focus on Children", "Focus on health for all", "Nourishment for all-focus on children", 2],
    ["September 27 is celebrated every year as:", "Teachers' Day", "National Integration Day", "World Tourism Day", "International Literacy Day", 3],
    ["Who is the author of 'Manas Ka-Hans'?", "Khushwant Singh", "Prem Chand", "Jayashankar Prasad", "Amrit Lal Nagar", 4],
    ["The death anniversary of which of the following leaders is observed as Martyrs' Day?", "Smt. Indira Gandhi", "Pt. Jawaharlal Nehru", "Mahatma Gandhi", "Lal Bahadur Shastri", 3],
    ["Who is the author of the epic 'Meghdoot'?", "Vishakadatta", "Valmiki", "Banabhatta", "Kalidas", 4]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(len(Questions)):
    question = Questions[i]
    print(f"\nQuestion for Rs. {levels[i]}\n",i+1,question[0])
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")
    
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    
    if reply == 0:
        print(f"You quit the game. You take home Rs. {money}")
        break
    
    if reply == question[5]:
        money = levels[i]
        print(f"Correct answer! You have won Rs. {money}")
    else:
        print("Wrong answer!")
        print(f"You take home Rs. {money}")
        break