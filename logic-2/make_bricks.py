## https://codingbat.com/prob/p118406 ##
# make_bricks #

'''We want to make a row of bricks that is goal inches long. We have a number of
small bricks (1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops.
See also: Introduction to MakeBricks
(https://codingbat.com/doc/practice/makebricks-introduction.html)'''

def make_bricks(small, big, goal):
    if 1*small + 5*big < goal:
        return False
    else:
        if goal % 5 <= small:
            return True

    return False
