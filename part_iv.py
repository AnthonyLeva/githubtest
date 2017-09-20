# pylint: disable=w,c
# Problem Set 1, Part IV
# Name: Leva, Anthony
# Collaborators: Office hours - Caroline

import math


def quadratic_solver(a, b, c):
    discriminant = b**2 - 4 * a * c
    square_root = math.sqrt(discriminant)
    denominator = 2 * a
    numerator1 = -b + square_root
    numerator2 = -b - square_root
    x1 = numerator1 / denominator
    x2 = numerator2 / denominator
    return x1, x2


a = float(raw_input('Please enter the value for a:'))
b = float(raw_input('Please enter the value for b:'))
c = float(raw_input('Please enter the value for c:'))
quadratic_solver(a, b, c)

answer1, answer2 = quadratic_solver(a, b, c)
print "The first solution is", answer1
print "The second solution is", answer2
