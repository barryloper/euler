from math import floor

def euler1(top=1000, facts=(3, 5)):

    list_of_multiples = []
    for f in facts:
        g = [f*i for i in range(1,int(top/f)+1)]
        if g[len(g)-1] == top: g.pop() #To make this return < top instead of <= top
        list_of_multiples += [x for x in g if x not in list_of_multiples]

    tot = 0
    for m in list_of_multiples:
        tot = tot + m

    return tot

if __name__ == '__main__':
    top = 1000
    facts = (3, 5)
    print "The sum of multiples of {2!r} less than {1!s} is {0!s}".format(euler1(top, facts), top, facts)
