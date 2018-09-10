from sys import stdin
import random

def process_line(line):
    question = line[1]
    answers = line[2:7]
    random.shuffle(answers)

    return question, answers

def enumerate_to_letter(num):
    d = {0:'a',
         1:'b',
         2:'c',
         3:'d',
         4:'e'}

    return d[num]

def main():
    counter = 1
    for line in stdin:
        line = line.strip('\r\n').split('\t')

        #don't include the initial header or any short answer questions
        try:
            if line[1].lower().startswith('question') or not line[3]:
                continue     
        except IndexError:
            continue
 
        question, answers = process_line(line)

        print '%s. ' % counter + question + '\n'
        for i, answer in enumerate(answers):
            letter = enumerate_to_letter(i)
            print  '%s. ' % letter + answer + '\n'

        print '\n\n'

        counter += 1

if __name__=='__main__':
    main()
