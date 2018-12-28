"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
fo = open('q&a.txt', 'r')
quiz_content = [line.strip() for line in fo.readlines()]
fo.close()


print(quiz_content)
correct_answers=0
for question in quiz_content:
    question_list = question.split('=')
    print(f'{question_list[0]}=')
    user_input = input()
    if user_input == question_list[1]:
        correct_answers = correct_answers + 1

print(f'{correct_answers}/{len(quiz_content)}')

fo = open('results.txt', 'w')
fo.write(f'{correct_answers}/{len(quiz_content)}')
fo.close()