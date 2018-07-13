#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

import sys
import os
from check_arg import *
from format_eq import *

""" - parse l'equation passee
    - prend en compte les equations sous forme naturelle (ex: 5 + 4 * X + X^2 = X^2) 
    - donne la forme reduite sous forme naturelle
    - affichage des etapes de resolution
    - affichage en couleurs """

class polynom:
    def __init__(self):
        self.res = [0]
        self.reduc = ""
        self.degree = -1
        self.discrim = 0
        self.result = ""
        self.result2 = ""
        self.unsolvable = False

def print_result(p):
    if p.degree < 0:
        print("No 'X' in equation.")
    else:
        print("\033[4mReduced form:\033[0m", p.reduc)
        print("\033[4mPolynomial degree:\033[0m", p.degree)
        if p.reduc == "0":
            print("\033[4mThe solutions are:\033[0m")
            print("All reals numbers.")
        elif p.unsolvable == True:
            print("\033[91mThis equation can not be solved (no solution possible).\033[0m")
        elif p.result != "" and (p.degree == 1 or p.discrim == 0):
            if p.degree == 2 and p.discrim == 0:
                print("\033[4mDiscriminant is nul.\033[0m\033[0m")
            print("\033[4mThe solution is:\033[0m\033[92m")
            print(p.result, "\033[0m")
        elif p.degree > 2:
            print("\033[91mThe polynomial degree is stricly greater than 2, I can't solve.\033[0m")
        elif p.discrim > 0:
            print("\033[4mDiscriminant is strictly positive, the two solutions are:\033[0m\033[92m")
            print(p.result)
            print(p.result2, "\033[0m")
        elif p.discrim < 0:
            print("\033[4mDiscriminant is strictly negative, the two solutions are:\033[0m\033[92m")
            print(p.result)
            print(p.result2, "\033[0m")

"""" Simplified Newton Iterative Sqrt Method """
def simple_sqrt(n):
    if n < 0:
        return 0
    val = n
    while True:
        last = val
        val = (val + n / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val

def solution_deg_two(p):
    p.discrim = p.res[1] * p.res[1] - 4 * p.res[2] * p.res[0]
    if p.discrim > 0:
        p.result = (-1 * p.res[1] - simple_sqrt(p.discrim)) / (2 * p.res[2])
        p.result2 = (-1 * p.res[1] + simple_sqrt(p.discrim)) / (2 * p.res[2])
    elif p.discrim == 0:
        p.result = (-1 * p.res[1]) / (2 * p.res[2])
    else:
        b = -1 * p.res[1]
        a = 2 * p.res[2]
        sqrt_delta = simple_sqrt(-1 * p.discrim)
        if a > 0:
            p.result += "(" + str(b) + " - " + str(sqrt_delta) + "i) / " + str(a)
            p.result2 = "(" + str(b) + " + " + str(sqrt_delta) + "i) / " + str(a)
        else:
            p.result = "(" + str(b) + " - " + str(sqrt_delta) + "i) / (" + str(a) + ")"
            p.result2 = "(" + str(b) + " + " + str(sqrt_delta) + "i) / (" + str(a) + ")"

def solution(p):
    i = 0
    tmp = 0
    if p.degree == 2:
        solution_deg_two(p)
    elif p.degree == 1:
        p.result = p.res[0] / (p.res[1] * -1)
    else:
        while i < len(p.res):
            if p.res[i] != 0:
                tmp += 1
            i += 1
        if p.res[0] != 0 and tmp == 1:
            p.unsolvable = True
    if p.result == 0:
        p.result = 0

def print_me(tab):
    my_str = ""
    tmp = 0
    for elt in tab:
        if type(elt) == str and elt[0] == '-':
            my_str += "(" + elt + ") "
        elif type(elt) == str and elt == "X^1":
            my_str += "X "
        elif type(elt) == str and elt == "-X^1":
            my_str += "(-X) "
        elif type(elt) == str:
            my_str += elt + " "
        else:
            if elt >= 0:
                my_str += str(elt) + " "
            else:
                my_str += "(" + str(elt) + ") "
        if elt == "=":
            tmp = 1
    if tmp == 0:
        my_str += "= 0"
    return my_str

def read_arg(argv):
    check_argv(argv)
    cut = argv.split(" ")
    p = polynom()
    check_format(cut, p)
    remove_stars(cut)
    remove_sign(cut)
    print("\033[94m\033[4mstep 1: Reformat the equation\033[0m\n\t", print_me(cut))
    put_to_left(cut)
    print("\033[94m\033[4mstep 2: Pass all elements to the left side\033[0m\n\t",\
     print_me(cut))
    reduce_me(cut)
    sort_me(cut, p)
    format_reduced_form(p)
    print("\033[94m\033[4mstep 3: Sort and reduce the equation\033[0m\n\t", \
        p.reduc)
    solution(p)
    if p.degree == 2:
        print("\033[94m\033[4mstep 4: Calculate discriminant\033[0m\n\tΔ =", \
        p.discrim)
    if p.result != "":
        print("\033[94m\033[4mLast step: Calculate solution(s)\033[0m\n")
    print_result(p)

try:
    arg = sys.argv[1]
    try:
        read_arg(arg)
    except:
        pass
except:
    print("\033[91mMissing Equation. computorv1 take an equation to argv.\033[0m")

