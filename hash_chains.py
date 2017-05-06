# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        #hash_index = self._hash_func
        if query.type == "check":
            # use reverse order, because we append strings to the end
            #self.write_chain(cur for cur in reversed(self.elems)
                        #if self._hash_func(cur) == query.ind)
           #print (query.ind)
           #print(self.elems[query.ind])
           if query.ind in self.elems:
             #print(22)
             print(self.elems[query.ind])
           else:
             print(' ') 

        else:
            #try:
                #ind = self.elems.index(query.s)
            #except ValueError:
                #ind = -1
            if query.type == 'find':
                hash_index = self._hash_func(query.s)
                if hash_index in self.elems:
                  pieces = self.elems[hash_index].split()
                  if query.s in pieces:
                    print('yes')
                  else:
                    print('no')
                else:
                    print('no')

                #self.write_search_result(ind != -1)
            elif query.type == 'add':
                hash_index = self._hash_func(query.s)
                #print(hash_index)
                if hash_index in self.elems:
                  pieces = self.elems[hash_index].split()
                  #print(pieces)
                  #print(query.s)
                  if query.s not in pieces:
                    pieces.insert(0,query.s)
                    self.elems[hash_index] = ' '.join(pieces)
                else:
                    self.elems[hash_index]=query.s
                #if ind == -1:
                    #self.elems.append(query.s)
            else:
                #if ind != -1:
                    #self.elems.pop(ind)
                hash_index = self._hash_func(query.s)
                if hash_index in self.elems:
                  pieces = self.elems[hash_index].split()
                  if query.s in pieces:
                    pieces.remove(query.s)
                  self.elems[hash_index] = ' '.join(pieces)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
