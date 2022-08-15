
# **************************************************
#                   A Star
# **************************************************


# This is A_Star node class 
# It makes new node and print soltions
class Node_A_Star:
    # class init
    def __init__(self, costSol, heuristic, state, sols):
        self.costSol = costSol
        self.evaluation_function = costSol + heuristic
        self.state = state
        self.sols = sols
    # compare evalution with other
    def __lt__(self, other):
        return self.evaluation_function < other.evaluation_function
    # print solutions
    def print_sols(self):
        i = 0
        while i < len(self.sols):
            if (i+1) % 3 == 0:
                print('| Solution\t    | (', self.sols[i], ')     returns with the west flashlight  |')
                i += 1
            else:
                print('| Solution\t    | (', self.sols[i], ',', self.sols[i+1], ') move to the west side\t\t  |')
                i += 2

import bisect, itertools, datetime            
Search_Cost_A_Star = 0                                      # Total number of generated nodes

# This is A Star Algorithm class 
# It makes new Tree-graph and saves each node
class Tree_A_Star:
    def __init__(self, listTimeUnits, num_people):
        state = [0] * num_people
        sols = []
        costSol = 0
        root = Node_A_Star(costSol, 0, state, sols)         # root node

        self.orig = listTimeUnits                           # time units list
        self.fringe = [root]                                # It saves each stage nodes
        self.listTimeUnits = sorted(listTimeUnits)          # sort time units list values
        self.number = num_people                            # save length
    # It checks if there is no repeated nodes
    def is_repeated_states(self, node):
        for i in self.fringe:
            if node.state == i.state and node.evaluation_function < i.evaluation_function:
                self.fringe.remove(i)
                bisect.insort(self.fringe, node)
                return True
            if node.state == i.state:
                return True
        return False
    # Find heuristic value
    def find_heuristic(self,node,place):
        left_time = []
        time_sum = 0
        for index in list(range(len(self.listTimeUnits))):
                if node.state[index] == place:
                        left_time.append(self.listTimeUnits[index])
        left_time = left_time[::-1]
        for index in range(len(left_time),2):
                time_sum += left_time[index]
        return time_sum
    # It makes nodes according to A Star algorithms
    def make_nodes(self,node):
        global Search_Cost_A_Star
        length = self.number
        # If the flashlight is on the East side         
        if len(node.sols) % 3 == 0:
            h = self.find_heuristic(node,0)
            fin = []
            left = []
            c = 0
            for index in range(length):
                    if node.state[index] == 0:
                            left.append(index)
                            c += 1
            a = left[0]
            b = left[1]           
            if c == 2:
                fin = [[a,b]]                
            else:
                c = left[-1]
                d = left[-2]
                fin = [[a,b],[a,c],[d,c]]
            c = 0
            for index in fin:
                    new_state = list(node.state)
                    new_state[index[0]] = 1
                    new_state[index[1]] = 1
                    new_steps = list(node.sols)
                    if(self.listTimeUnits[index[0]]==self.listTimeUnits[index[1]]):
                        for f in range(self.orig.index(self.listTimeUnits[index[0]])+1,length):
                            if(self.listTimeUnits[index[1]]==self.listTimeUnits[f]):
                                new_steps.extend([self.orig.index(self.listTimeUnits[index[0]])+1, f+1])
                                break
                    else:
                        new_steps.extend([self.orig.index(self.listTimeUnits[index[0]])+1, self.orig.index(self.listTimeUnits[index[1]])+1])

                    Search_Cost_A_Star += 1
                    new_cost = node.costSol + max(self.listTimeUnits[index[0]], self.listTimeUnits[index[1]])
                    # If it's a new state, make new node                    
                    new_node = Node_A_Star(new_cost, h , new_state, new_steps)
                    # Check for Repeated States
                    if not self.is_repeated_states(new_node):
                        # Insert new node at the end of the fringe
                        bisect.insort(self.fringe, new_node)
        # If the flashlight is on the West side
        else:
            h = self.find_heuristic(node,1)
            for index in list(range(length)):
                if (node.state[index] == 1):
                    new_state = list(node.state)
                    new_state[index] = 0
                    new_steps = list(node.sols)
                    new_steps.append(self.orig.index(self.listTimeUnits[index])+1)
                    new_cost = node.costSol + self.listTimeUnits[index]
                    new_node = Node_A_Star(new_cost, h, new_state, new_steps)
                    Search_Cost_A_Star += 1
                    # Check for Repeated States
                    if not self.is_repeated_states(new_node):
                        # Insert new node at the end of the fringe
                        bisect.insort(self.fringe, new_node)

    def a_star(self):
        Space_Req = 0
        length = self.number
        while 1:
            # Look for fringe and increase the Space_Req variable
            node = self.fringe.pop(0)
            Space_Req += 1
            # make nodes
            self.make_nodes(node)
            # Check for End state
            if node.state == [1] * length:
                print("\t\tResult using A star algorithm")
                print('|'+'-'*65 + '|')
                # Print Solution results
                node.print_sols()
                # print Solution-Cost and Space-Requirement
                print('|-------------------|'+'-'*45 + '|')
                print('| Solution Cost     |', node.costSol, '\t'*5 +'  |')
                print('|-------------------|'+'-'*45 + '|')
                print('| Search Cost       |', Search_Cost_A_Star -1, '\t'*5 +'  |')
                print('|-------------------|'+'-'*45 + '|')
                print('| Space Requirement |', Space_Req, '\t'*5 +'  |')
                print('|'+'-'*65 + '|')
                break


# C = 1                                                 # test case : There is one test case
# K = 3                                                 # number of people : Three people
# time_unit = [3, 2, 5]                                 # time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 7                                                 # number of people : Three people
# time_unit = [9,9,9,9,9,9,30]                          # time units list for each people

C = 1                                                   # test case : There is one test case
K = 6                                                   # number of people : Four people
time_unit = [44, 55, 66, 33, 8, 1]                      # time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 8                                                 # number of people : Ten people
# time_unit = [5, 6, 4, 3, 3, 4, 5, 6000]               # time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 8                                                 # number of people : Ten people
# time_unit = [50, 60, 40, 30, 30, 40, 50, 6]           # time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 8                                                 # number of people : Ten people
# time_unit = [10, 100, 1000, 10000, 1000, 100, 10, 1]  # time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 9                                                 # number of people : Ten people
# time_unit = [100, 2, 3, 4, 5, 60, 7, 8, 9]            # time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 9                                                 # number of people : Ten people
# time_unit = [3,3,3,4,4,4,4,8,8]                       # time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 10                                                # number of people : Ten people
# time_unit = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 10                                                # number of people : Ten people
# time_unit = [100, 90, 80, 70, 60, 60, 70, 80, 90, 100]# time units list for each people

# C = 1                                                 # test case : There is one test case
# K = 10                                                # number of people : Ten people
# time_unit = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]            # time units list for each people

# Get the current time for measuring
start_time = datetime.datetime.now()  

while C:
    if len(time_unit) != K:
        print('Error!, Please re-input \'K\' and \'time_unit\' values.')
        break

    # Test A Star algorithm
    East_West_UCS = Tree_A_Star(time_unit, K)       # make tree-graph with input values
    East_West_UCS.a_star()                          # Test A Star algorithms
    C -= 1

end_time = datetime.datetime.now()
delta_time = end_time - start_time
elapsed_time = delta_time.seconds + delta_time.microseconds / 1e+6

print('|\tTime (1000 calls, in secs) : {}s\t\t\t  |'.format(elapsed_time))

