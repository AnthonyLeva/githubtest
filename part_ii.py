# pylint: disable=w,c
# Problem Set 1, Part II
# Name: Leva, Anthony
# Collaborators: N/a

from mystery import gen_adjective

name = raw_input('What is your name?')
print 'Hi,', name + '!', 'You look', gen_adjective(), 'today!'
