# python3
import sys

class JobQueue:
    def read_data(self):
        #self.num_workers, m = map(int, input().split())
        #self.jobs = list(map(int, input().split()))
        #assert m == len(self.jobs)
        input = sys.stdin.read()
        self.data = list(map(int, input.split()))
        self.num_workers = self.data[0]
        m= self.data[1]
        self.jobs = self.data[2:]
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        #### This function will return the next node who will be assigned the task based on priority ####
        def find_smaller(left, right,tree_left, tree_right, prio_tree_left, prio_tree_right):
            
            if prio_tree_left < prio_tree_right:
              return left
            if prio_tree_right < prio_tree_left:
              return right
            if prio_tree_left == prio_tree_right:
              if tree_left < tree_right:
                return left
              elif tree_right < tree_left:
                return right
            return -1 
        prio = []
        index = []
        tree = []
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        for i in range(0,self.num_workers):
           prio.append(0)
           index.append(i)
           tree.append(i)
        

        for i in range(len(self.jobs)):
           ### This loop is running for each task to be assigned ###
           ### The task will be assigned to the root node always and tree will be adjusted after the task is assigend to the root ###
           self.assigned_workers[i] = tree[0]
           self.start_times[i] = prio[tree[0]]
           prio[tree[0]] += self.jobs[i]
           current = 0
           left = 0
           right = 0
           if 2*current + 1 < self.num_workers:
             left = 2*current +1
           if 2*current + 2 < self.num_workers:
             right = 2*current + 2
           ### Trying to find the next one based on priority ###
           next = find_smaller(left, right, tree[left], tree[right], prio[tree[left]], prio[tree[right]])
           while (current != next and next != -1):
                ### if priority of next is better than current, next will move upwards in the tree ###
                while ((prio[tree[current]] > prio[tree[next]]) or ((prio[tree[current]] == prio[tree[next]]) and (tree[current] > tree[next]))):
                      tree[current], tree[next] = tree[next], tree[current]
                      current = next
                      left = current
                      right = current
                      if  2*current + 1 < self.num_workers:
                         left = 2*current +1
                      if 2*current + 2 < self.num_workers:
                         right = 2*current + 2
                      next = find_smaller(left, right, tree[left], tree[right], prio[tree[left]], prio[tree[right]])
                      if current == next or next == -1:
                        break

                break



                    
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

