#Hello, World!
print("Hello, World!")

#Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 == 0):
        if (2 <= n <= 5 or n > 20):
            print("Not Weird")
        elif (6 <= n <= 20):
            print("Weird")
    else:
         print("Weird")

#Arithmetic operators
import math

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    if (1 < a < pow(10, 10) and 1 < b < pow(10, 10)):
        print(a + b)
        print(a - b)
        print(a * b)
    else:
        print("Input error")

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if (b != 0):
        print(a//b)
        print(a/b)
    else:
        print("Error: cannot divide by 0.")

#Loops
if __name__ == '__main__':
    n = int(input())
    if (1 <= n <= 20):
        for i in range(n):
            print(i*i)
    else:    
        print("Error: input constraints violated.")

#Write a function
def is_leap(year):
    leap = False
    if (1900 <= year <= pow(10, 5)):
        if (year % 4 == 0):
            leap = True
            if (year % 100 == 0):
                leap = False
                if (year % 400 == 0):
                    leap = True
    else:
        print("Error: input constraints violated.")
    return leap

#Print function
if __name__ == '__main__':
    n = int(input())
    if (1 <= n <= 150):
        for i in range(1, n + 1):
            print(i, end='')
    else:
        print("Error: input constraints violated.")

#Lists
if __name__ == '__main__':
    N = int(input())
    ris = []
    #Prendo in input i comandi
    for n in range(N):
        cmd = input()
        cmd_list = cmd.split()
        word = cmd_list[0]
        #/Implement commands
        if word == 'insert':
            ris.insert(int(cmd_list[1]), int(cmd_list[2]))
        elif word == 'print':
            print(ris)
        elif word == 'remove':
            if int(cmd_list[1]) in ris:
                ris.remove(int(cmd_list[1]))
        elif word == 'append':
            ris.append(int(cmd_list[1]))
        elif word == 'sort':
            ris.sort()
        elif word == 'pop':
            if ris != []:
                ris.pop()
        elif word=='reverse':
            ris.reverse()
        else:
            print("Error: unknown command.")

#Tuples
n = int(input())
elements = input()
t = tuple(map(int, elements.split()))
print(hash(t))

#List Comprehension
#if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(dict.fromkeys(arr))
    arr.sort()
    arr.reverse()
    print(arr[1])

#Nested Lists
if __name__ == '__main__':
    big_list = []
    list_scores = []
    list_names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        big_list.append([name, score])
        list_scores.append(score)
   
    m = min(list_scores)
    list_scores = list(dict.fromkeys(list_scores))
    list_scores.sort()
    sm = list_scores[1]
    for i in range(len(big_list)):
        if big_list[i][1] == sm:
            list_names.append(big_list[i][0])
    list_names.sort()
    for i in range(len(list_names)):
        print(list_names[i])

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = student_marks.get(query_name)
    ris = 0
    for i in l:
        ris += i
    ris = '{0:.2f}'.format(ris / len(l))
    print(ris)

#sWAP cASE
def swap_case(s):
    ris = ''
    for c in s:
        if c.isupper():
            ris += c.lower()
        else:
            ris += c.upper()
    return ris

#String Split and Join
def split_and_join(line):
    # write your code here
    ris = line.split()
    ris = '-'.join(ris)
    return ris

#What's Your Name?
def print_full_name(first, last):
    print('Hello ' + first + ' ' + last + '! You just delved into python.')

#Mutations
def mutate_string(string, position, character):
    ris = string[:position] + character + string[position + 1:]
    return ris

#Alternative solution
#def mutate_string(string, position, character):
#    ris = list(string)
#    ris[position] = character
#    ris = ''.join(ris)
#    return ris

#Birthday Cake Candles
def birthdayCakeCandles(candles):
    return candles.count(max(candles))

#def kangaroo(x1, v1, x2, v2):
    ris = ''
    if (x2 > x1 and v2 > v1):
        ris = 'NO'
    elif (v1 - v2 == 0):
        ris = 'NO'
    else:
        jumps_number = (x2 - x1) / (v1 - v2)
        if( jumps_number % 1 == 0 and jumps_number > 0):
            ris = 'YES'
        else:
            ris = 'NO'
    return ris

#Viral Advertising
def viralAdvertising(n):
    tot = 0
    p = 5
    for i in range(1, n + 1):
        likes = math.floor(p / 2)
        tot += likes
        p = likes * 3
    return tot