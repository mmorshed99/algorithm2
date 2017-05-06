# python3
import math
import sys
class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    input = sys.stdin.read()
    self._data = list(map(int, input.split()))
    n = self._data[0]
    self._data = self._data[1:]
    assert n == len(self._data)

  def WriteResponse(self):

    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):

     number = len(self._data)

     levels = (math.log(number)/math.log(2))
     if levels == math.ceil(levels):
       levels = int(levels)
       p =  math.pow(2,levels)
     else:
       levels = math.ceil(levels)
       levels = int(levels)
     
       p =  math.pow(2,levels)//2
     p = p-1
     p = int(p)
     
     q = number
     while (p !=q) and (p>=0) :
      for i in range(p ,q):
        if i%2 == 1 and i !=number :
         if(i+1 < number):
          if (self._data[i] < self._data[i+1]):
            if self._data[i] < self._data[(i-1)//2]:
               self._swaps.append(((i-1)//2,i))
               self._data[i], self._data[(i-1)//2] = self._data[(i-1)//2], self._data[i]
               r = 2 * i + 1
               j = i
               #t = r + 1
               while r < number:
                    if ((r+1 < number) and  (self._data[r] < self._data[r+1]) and (self._data[r] < self._data[j])) or ((r+1 >= number) and (self._data[r] < self._data[j])):  

                      self._swaps.append((j,r))
                      self._data[r], self._data[j] = self._data[j], self._data[r]
                      j = r 
                      r = 2 * r + 1
                   
                    elif (r+1 <number) and self._data[r+1] < self._data[j]: 
                      self._swaps.append((j,r+1))
                      self._data[r+1], self._data[j] = self._data[j], self._data[r+1]
                      j = r+1
                      r = 2 * j + 1
                    else:
                      break     
          else:
            if (self._data[i+1] < self._data[(i-1)//2]):
               self._swaps.append(((i-1)//2,i+1))
               self._data[i+1], self._data[(i-1)//2] = self._data[(i-1)//2], self._data[i+1]
               r = 2* (i+1) + 1
               j = i+1
               while r < number:
                    if ((r+1 < number) and  (self._data[r] < self._data[r+1]) and (self._data[r] < self._data[j])) or ((r+1 >= number) and (self._data[r] < self._data[j])):

                      self._swaps.append((j,r))
                      self._data[r], self._data[j] = self._data[j], self._data[r]
                      j = r 
                      r = 2 * r + 1
                    elif (r+1 <number) and self._data[r+1] < self._data[j]: 
                      self._swaps.append((j,r+1))
                      self._data[r+1], self._data[j] = self._data[j], self._data[r+1]
                      j = r+1
                      r = 2 * j + 1
                    else:
                      break
         else:
           if self._data[i] < self._data[(i-1)//2]:
               self._swaps.append(((i-1)//2,i))
               self._data[i], self._data[(i-1)//2] = self._data[(i-1)//2], self._data[i]
               r = 2 * i + 1
               j = i
               
               while r < number:
                    if ((r+1 < number) and  (self._data[r] < self._data[r+1]) and (self._data[r] < self._data[j])) or ((r+1 >= number) and (self._data[r] < self._data[j])): 
                    #if self._data[r] < self._data[j]:
                      self._swaps.append((j,r,))
                      self._data[r], self._data[j] = self._data[j], self._data[r]
                      j = r 
                      r = 2 * r + 1
                   
                    elif (r+1 <number) and self._data[r+1] < self._data[j]: 
                      self._swaps.append((j,r+1))
                      self._data[r+1], self._data[j] = self._data[j], self._data[r+1]
                      j = r+1
                      r = 2 * j + 1
                    else:
                     break  

      p = (p-1)//2

      q = p * 2 



  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
