suspects = ['A', 'B', 'C', 'D']
criminal_dict = {0: 'innocent', 1: 'guilty'}
n = 1

for a in range(0, 2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                  if (a + b >= 1) and (a + e + f >= 2) and (a * d == 0) and (b == c) and (c + d == 1) and (d >= e): 
                            result = zip(suspects, [criminal_dict[a], criminal_dict[b], criminal_dict[c], criminal_dict[d])
                            print "第%d种作案方案:" %(n)
                            print result
                            n = n + 1
print "\n总共有%d种作案方案" % (n-1)
