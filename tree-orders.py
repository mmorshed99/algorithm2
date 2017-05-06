# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    printed = []
    for i in range(0,(self.n)):
        printed.append(1)  ##1 while not visited yet
    #print(len(printed))
    current_index = 0
    stack = []
    while (True):
         #stack = []
         if current_index == 0:
           #if printed[current_index] == 0:
           temp = 0
           for j in range(1,self.n):
              if printed[j] == 1:
                temp = 1
                break
           if temp == 0:
             if  printed[current_index] == 1:
               self.result.append(self.key[current_index])
             break
         #print(current_index)
         #print(stack)
         #print(self.key[self.right[current_index]])   
         if self.left[current_index] != -1 and printed[self.left[current_index]] == 1:
            stack.append(current_index)
            current_index = self.left[current_index] 
            continue 
         #print(self.key[self.right[current_index]])   
         elif self.right[current_index] != -1 and printed[self.right[current_index]] == 1:
            if printed[current_index] == 1:
              self.result.append(self.key[current_index])
              printed[current_index] = 0 
            stack.append(current_index)
            current_index = self.right[current_index]
         else: 
            if printed[current_index] == 1:
              self.result.append(self.key[current_index])
              printed[current_index] = 0 
            current_index = stack.pop()
                
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    printed = []
    for i in range(0,(self.n)):
        printed.append(1)  ##1 while not visited yet
    #print(len(printed))
    current_index = 0
    stack = []
    while (True):
         if current_index == 0:
           if printed[current_index] == 0:
              temp = 0
           for j in range(0,self.n):
              if printed[j] == 1:
                temp = 1
                break
           if temp == 0:
             break
         if self.left[current_index] != -1 and printed[self.left[current_index]] == 1:
            if printed[current_index] == 1:
              self.result.append(self.key[current_index])
              printed[current_index] = 0 

            stack.append(current_index)
            current_index = self.left[current_index] 

         elif self.right[current_index] != -1 and printed[self.right[current_index]] == 1:
            if printed[current_index] == 1:
              self.result.append(self.key[current_index])
              printed[current_index] = 0 
            stack.append(current_index)
            current_index = self.right[current_index]
         else: 
            if printed[current_index] == 1:
              self.result.append(self.key[current_index])
              printed[current_index] = 0 
            current_index = stack.pop()
            
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    printed = []
    for i in range(0,(self.n)):
        printed.append(1)  ##1 while not visited yet
    #print(len(printed))
    current_index = 0
    stack = []
    while (True):
         if current_index == 0:
           #if printed[current_index] == 0:
           temp = 0
           for j in range(1,self.n):
              if printed[j] == 1:
                temp = 1
                break
           if temp == 0:
             self.result.append(self.key[current_index])
             break
         #print(current_index)
         if self.left[current_index] != -1 and printed[self.left[current_index]] == 1:
            #if printed[current_index] == 1:
              #self.result.append(self.key[current_index])
              #printed[current_index] = 0 

            stack.append(current_index)
            current_index = self.left[current_index] 

         elif self.right[current_index] != -1 and printed[self.right[current_index]] == 1:
            #if printed[current_index] == 1:
              #self.result.append(self.key[current_index])
              #printed[current_index] = 0 
            stack.append(current_index)
            current_index = self.right[current_index]
         else: 
            if printed[current_index] == 1:
              self.result.append(self.key[current_index])
              printed[current_index] = 0 
            current_index = stack.pop()
                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
