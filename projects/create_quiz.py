"""Creates a quiz asking for capitals of 50 states for 35 students."""

import random
import os

NUMSTUDENTS = 35  # Number of students
NUMQUESTIONS = 50  # Number of questions

# The quiz data. Keys are states and values are their capitals.
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord',
    'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
    'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}


def newquestion(state):
    """Generate a question. Returns [[answers], numright]."""
    rightanswer = capitals[state]
    wrongstates = []

    for i in range(0, 3):
        while True:
            new = random.choice(list(capitals.keys()))
            if new not in wrongstates and new != state:
                wrongstates.append(new)
                break
            else:
                continue
    wronganswers = [capitals[x] for x in wrongstates]
    right = random.randint(1, 4)
    answers = []
    for i in range(1, 5):
        if i == right:
            answers.append(rightanswer)
        else:
            answers.append(wronganswers.pop())
    return [answers, right]


def gen_stateslist(numq=NUMQUESTIONS):
    """Generate a list of states for one exam."""
    stateslist = []
    for i in range(0, numq):
        while True:
            new = random.choice(list(capitals.keys()))
            if new not in stateslist:
                stateslist.append(new)
                break
            else:
                continue
    return stateslist

for i in range(NUMSTUDENTS):
    # Generate a list of states
    stateslist = gen_stateslist(NUMQUESTIONS)

    # Create a new quiz and answerkey
    quiz = ["Welcome to the quiz!"]
    answerkey = []

    # Create a list of lines for the quiz and answerkey
    for j in range(NUMQUESTIONS):
        # Ask the question
        quiz.append("\n\n")
        quiz.append(str(j+1) + ". ")
        quiz.append("What is the capital of {}?".format(stateslist[j]))
        quiz.append("\n")
        # Print the answers
        (answers, numright) = newquestion(stateslist[j])
        for k in range(len(answers)):
            quiz.append("\t" + 'ABCD'[k] + ". " + answers[k])
            quiz.append("\n")
        # Print the answerkey
        answerkey.append(str(j+1).zfill(2) + ". " + 'ABCD'[numright-1])
        answerkey.append("\n")

    # Create the directories if they don't exist
    if not os.path.isdir('quizes'):
        os.makedirs('quizes')
    if not os.path.isdir('answerkeys'):
        os.makedirs('answerkeys')

    # Write the quiz to a file
    filename = 'quizes/quiz {}.txt'.format(str(i+1).zfill(2))
    with open(filename, 'w') as f:
        for line in quiz:
            f.write(line)

    # Write the answerkey to a file
    filename = 'answerkeys/key {}.txt'.format(str(i+1).zfill(2))
    with open(filename, 'w') as f:
        for line in answerkey:
            f.write(line)
