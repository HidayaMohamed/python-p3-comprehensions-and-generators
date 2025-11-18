#!/usr/bin/env python3

def return_evens(num_list):
    even_nums= [n for n in num_list if n% 2 ==0]
    return even_nums

def make_exclamation(sentence_list):
    for i in range(len(sentence_list)):
        sentence_list[i] = sentence_list[i] + "!"
    return sentence_list