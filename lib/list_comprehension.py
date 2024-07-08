#!/usr/bin/env python3

def return_evens(num_list):
    even = []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
    return even

print(return_evens([2,5,7,8,10]))

def make_exclamation(sentence_list):
    new = []
    for i in sentence_list:
        i =  i +"!"
        new.append(i)
    return new

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))