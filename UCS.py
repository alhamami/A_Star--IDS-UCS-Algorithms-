
# ********************************************
#       Uniform - Cost -Search   
# ********************************************


# This is Node_UCS class 
# It makes new node and print soltions
class Node_UCS:
    # class init
    def __init__(self, costSol, state, sols):
        self.costSol = costSol
        self.state = state
        self.sols = sols
    # compare solution cost value
    def __lt__(self, other):
        return self.costSol < other.costSol
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

Search_Cost_UCS = 0                                     # Total number of generated nodes

# This is UCS Algorithm class 
# It makes new Tree-graph and saves each node
class Tree_UCS:
    def __init__(self, listTimeUnits, memberNum):
        state = [0] * memberNum
        sols = []
        costSol = 0
        root = Node_UCS(costSol, state, sols)           # root node
        self.fringe = [root]                            # It saves each stage nodes
        self.listTimeUnits = listTimeUnits              # time units list 
        self.number = memberNum                         # number of members

    # It checks if there is no repeated nodes
    def is_repeated_states(self, node):
        for i in self.fringe:
            if node.state == i.state and node.costSol < i.costSol:
                self.fringe.remove(i)
                bisect.insort(self.fringe, node)
                return True
            if node.state == i.state:
                return True
        return False
    # It makes nodes according to UCS algorithms
    def make_nodes(self, node):
        length = self.number
        global Search_Cost_UCS
        # If the flashlight is on the East side 
        if len(node.sols) % 3 == 0:
            for pair in itertools.combinations(list(range(length)), 2):
                # If it's a new state, make new node
                if (node.state[pair[0]] == 0 and node.state[pair[1]] == 0):
                    new_state = list(node.state)
                    new_state[pair[0]] = 1
                    new_state[pair[1]] = 1
                    new_sols = list(node.sols)
                    new_sols.extend([pair[0]+1, pair[1]+1])
                    new_cost = node.costSol + max(self.listTimeUnits[pair[0]], self.listTimeUnits[pair[1]])
                    new_node = Node_UCS(new_cost, new_state, new_sols)
                    Search_Cost_UCS += 1
                    # Check for Repeated States
                    if not self.is_repeated_states(new_node):
                        # Insert new node at the end of the fringe
                        bisect.insort(self.fringe, new_node)
        # If the flashlight is on the West side
        else:
            for item in list(range(length)):
                if (node.state[item] == 1):
                    new_state = list(node.state)
                    new_state[item] = 0
                    new_sols = list(node.sols)
                    new_sols.append(item+1)
                    new_cost = node.costSol + self.listTimeUnits[item]
                    Search_Cost_UCS += 1
                    new_node = Node_UCS(new_cost, new_state, new_sols)
                    # Check for Repeated States
                    if not self.is_repeated_states(new_node):
                        # Insert new node at the end of the fringe
                        bisect.insort(self.fringe, new_node)
                        

    def Uniform_Cost_Search(self):
        Space_Req = 0
        length = self.number
        while True:
            # Look for fringe and increase the Space_Req variable
            node = self.fringe.pop(0)
            Space_Req += 1
            # Make States with make_nodes() function
            self.make_nodes(node)
            # Check for End State
            if node.state == [1] * length:
                print("\t\tResult using UCS algorithm")                
                print('|'+'-'*65 + '|')
                # Print Solution results
                node.print_sols()
                # print Solution-Cost and Space-Requirement
                print('|-------------------|'+'-'*45 + '|')
                print('| Solution Cost     |', node.costSol, '\t'*5 +'  |')
                print('|-------------------|'+'-'*45 + '|')
                print('| Search Cost       |', Search_Cost_UCS - 1, '\t'*5 +'  |')
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

C = 1                                                 # test case : There is one test case
K = 6                                                 # number of people : Four people
time_unit = [44, 55, 66, 33, 8, 1]                             # time units list for each people

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

    # Test UCS algorithms
    East_West_UCS = Tree_UCS(time_unit, K)              # make tree-graph with input values
    East_West_UCS.Uniform_Cost_Search()                 # Test UCS algorithms
    C -= 1

end_time = datetime.datetime.now()
delta_time = end_time - start_time
elapsed_time = delta_time.seconds + delta_time.microseconds / 1e+6

print('|\tTime (1000 calls, in secs) : {}s\t\t\t  |'.format(elapsed_time))
