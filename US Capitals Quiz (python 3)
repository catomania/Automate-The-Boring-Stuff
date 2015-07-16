#! python3
# randomQuizGenerator.py - creates quizzes w/ q's and a's
#in random order along w/ answer key

import random

#the quiz data, keys are states and values are capitals


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#generate 35 quiz files
for quizNum in range(50):
    # create the q and a key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalquiz_answers%s.txt' % (quizNum + 1), 'w')


#write out header for quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

#shuffle order of the states.
    states = list(capitals.keys()) #key = states, the first part of the :
    random.shuffle(states) #randomly shuffle the list, can you not shuffle capitals directly?


    
#loop through all 50 states, making q for each
    for questionNum in range(50): #go thru this loop 50 times
        
        #get right and wrong answers
        correctAnswer = capitals[states[questionNum]]#gets 1 city value each time of a capital
        #correctAnswer will loop from states[0] to [49] and grab the city value thru the shuffled states list      
        wrongAnswers = list(capitals.values())
        #list must be integers print (wrongAnswers[correctAnswer])
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #delete the correct answer's state from list of wrong choices
        wrongAnswers = random.sample(wrongAnswers, 3) #only pick 3
        answerOptions = wrongAnswers + [correctAnswer] #make the list options
        random.shuffle(answerOptions) #shuffle the order
        
    
        #to do: write the q and a options to quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
            states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        #write answer key to file 
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()






