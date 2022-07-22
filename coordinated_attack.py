import random

class Node():
    def __init__(self, id, n, r):
        self.id = id
        self.round = 0
        self.decision = "unknown"
        self.key = "undefined"
        self.n = n
        self.values = ["undefined" for i in range(n)] 
        self.values[self.id] = random.randint(0, 1) # ???aya hamin
        self.levels = [-1 for i in range(n)] 
        self.levels[self.id] = 0
        self.maxiteration = r

    def rand(self): 
        if self.round == 0 and self.id == 1 :
            self.key = random.randint(0, self.maxiteration)
            print("key")
            print(self.key)
  
    def msgs(self):
        mssg = {"levels":self.levels, "values":self.values, "key": self.key}
        return mssg  
    
    def trans(self, msg_list):      # mssg: values, levels , key
        
        self.round = self.round + 1
        


        for mssg in msg_list:    
            if mssg["key"] != "undefined":
                self.key = mssg["key"]

            p_val = mssg["values"]
            p_level = mssg["levels"]

            for j in range(self.n): 
                if j != self.id:
                    if p_val[j] != "undefined":
                        self.values[j] = p_val[j]         
                
                    self.levels[j]= max(p_level[j], self.levels[j])

            self.levels[self.id] = 1 + min([x for i,x in enumerate(self.levels) if i!=self.id] ) # valy khode i nabayad bashe
        if self.round == 1:
            if self.key != "undefined" and self.levels[self.id] >= self.key and all(element == 1 for element in self.values) :
                self.decision = 1
            else:
                self.decision = 0        

def msg_lost():
    pass


if __name__ == "__main__":
    nodes = int(input("Enter number of nodes "))
    rounds = int(input("Enter number of rounds "))
    node_list = []

    for n in range(nodes):
        node_list.append(Node(n, nodes, rounds))  #id, n, r        

    for r in range(rounds):
        msg_list = []
        for n in node_list:
            n.rand()
            msg_list.append(n.msgs())
        
        for n in node_list:

            
            # vase jhodesho be khodesh nafreste
            #  eenja random yeserio nafreste 
            n.trans(msg_list)
            
    for n in node_list:
        print(n.levels)
        print(n.values)
        print(n.decision)




