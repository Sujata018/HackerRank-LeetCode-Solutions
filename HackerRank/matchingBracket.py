#!/usr/bin/env python
# coding: utf-8

# In[50]:


def isBalanced(s):
    openBrackets=[]
    for curBracket in s:
        if curBracket in '[({':
             openBrackets.append(curBracket)
        elif curBracket in ']})':
            try:
                prevBracket = openBrackets.pop()
            except:
                return 'NO'
            if (prevBracket,curBracket) not in (('(',')'), ('{','}'), ('[',']')):
                return 'NO'
        else:
            sys.exit("Invalid input")   
    if len(openBrackets) == 0:
        return 'YES'
    else:
        return 'NO'


# In[51]:


if __name__=='__main__':
    print(isBalanced('{}[](()'))

