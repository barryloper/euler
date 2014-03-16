#sum of even fib. nums under 4000000

f1 = 1
f2 = 2
fsum = 2
evens = ("0", "2", "4", "6", "8") # I think i%2 could get expensive for large nums. -Not that this will get that large, now that I think about it...
while f2 < 4000000:
    if str(f2)[-1:] in evens:
        fsum += f2
        #print "%d, " % f2,
    ft = f1 + f2 # a temp. to store next f
    f1 = f2 # shift the computed numbers down
    f2 = ft

print "Largest f2: {!s}. Total sum: {!s}".format(f1, fsum) 
# the largest f2 used was pushed into f1
