from sys import exit
i = 0
A = []
print "Can you enter the names of the girls in this class?"
print "List those who need to sit near the front first."
print "Press ENTER when done."
while True:
    x = raw_input("Girl: ")
    
    if x == "":
        s = A
        l = len(s)
        
        for girl in s:
            print """
Is there anyone %s can't sit beside?
If not type 'no'.""" % girl
            girl2 = raw_input("> ")
            i += 1
            
            if i<l and s[i] == girl2:           # checks to the right
                del s[i]
                s.append(girl2)
            elif i+7 < l and s[i+6] == girl2:   # checks behind right
                del s[i+6]
                s.append(girl2)
            elif i+6 < l and s[i+5] == girl2:   # checks behind
                del s[i+5]
                s.append(girl2)
            elif i+5 < l and (i-1)%6 > 0 and s[i+4] == girl2:
                del s[i+4]                      # checks behind left
                s.append(girl2)
            else:
                pass
            
        print "Here is your seating plan:"
        for i in range(0,l,6):
            print ", ".join(s[i:i+2]) + "\t"*2 + ", ".join(s[i+2:i+4]) + "\t"*2 + ", ".join(s[i+4:i+6]) + "\n"
        exit(0)

    else:
            A.append(x)
    
