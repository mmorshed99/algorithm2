# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    coordinate = 0
    count = 0
    save_count = 0
    failure = False
    opening_brackets_stack = []
    for i, next in enumerate(text): ##enumerate(thing), where thing is either an iterator or a sequence, returns a iterator that will return (0, thing[0]), (1, thing[1]), (2, thing[2]), and so forth.
        if len(opening_brackets_stack) == 0:
           save_count = save_count + count
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            pass
        count +=1
        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            

            if len(opening_brackets_stack) == 0:
              failure = True
              coordinate = count
              break
            if (next == ')'):
              if opening_brackets_stack.pop() != '(' :
                failure = True
                coordinate = count
                break 
            if (next ==']'):
              if opening_brackets_stack.pop() != '[' :
                            failure= True
                            coordinate = count
                            break
            if (next =='}'):
              if opening_brackets_stack.pop() != '{' :
                            failure= True
                            coordinate = count
                            break


            

    if failure == True:
      print (count)
    elif len(opening_brackets_stack) != 0:
      count = save_count + len(opening_brackets_stack)
      print (count)     
    else:
      print ("Success")  
