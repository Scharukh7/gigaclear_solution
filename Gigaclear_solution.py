#%%
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
#import load_graph as file


class load_graph:
    """"
    this class loads the graphml file provided and goes through nodes and edges, as well as adding to the attributes
    
    attributes:
    ------------
    path: directory where the graphml file is located
    cabinets_rate: setting the cabinet price to 0 and then increment by 1 everytime a node is found
    pot_rate: setting the pot price to 0 and then increment by 1 every time a node is found
    verge_length: setting the verge length to 0 and then incremented every time an edge is found
    road_length: setting the road length to 0 and then incremented everytime an edge is found
    """""
    path = '/home/shah/Desktop/gigaclear-code-challenge-python/problem.graphml'
    G = nx.read_graphml(path)

    #nodes
    cabinets_rate = 0
    pot_rate = 0
    chamber_rate = 0
    #edges
    verge_length = 0
    road_length = 0


    for node in G.nodes(data=True):
        
        #accessing second element of the tuple and 
        #converting it into a dict
        network_nodes=dict(node[1])


        #looping thru the network and taking count of the nodes    
        for x,y in network_nodes.items():
            if network_nodes[x]=='Cabinet':
                cabinets_rate+=1
                print(f"cabinet count: ",cabinets_rate)
            if network_nodes[x]=="Pot":
                pot_rate+=1
                print(f"pot count: ",pot_rate)
            if network_nodes[x]=='Chamber':
                chamber_rate+=1
                print(f"chamber count: ",chamber_rate)
    print(f"\n")

    for edge in G.edges(data=True):
        
        network_edges=dict(edge[2])#accessing the third elelment of the tuple
        
        if network_edges['material']=='verge':
            verge_length+=network_edges['length']
        else:
            road_length+=network_edges['length']

    #visualization
    pos_nodes = nx.spring_layout(G)
    nx.draw(G, pos_nodes, with_labels=True)
    #adding labels to each node with their key type
    pos_attrs = {}
    for node, coords in pos_nodes.items():
        pos_attrs[node] = (coords[0], coords[1] + 0.08)
            
    node_attrs = nx.get_node_attributes(G, 'type')
    custom_node_attrs = {}
    for node, attr in node_attrs.items():
        custom_node_attrs[node] = "'" + attr + "'"
    #adding labels to the edges
    nx.draw_networkx_labels(G, pos_attrs, labels=custom_node_attrs)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos_nodes, {('A','F'):"50m",('F','B'):"20m",('F','G'):"100m",('G','I'):"40m",('C','G'):"50m",('G','H'):"100m",('D','H'):"100m",('E','H'):"50m"})

    plt.show()

class Card_A:
    """"
    this class calculates the total rate of card A with the function card_A_rate_calculator with the given cost value for each attribute

    attributes:
    ------------

    cabinets_a: variable
    verge_length_a: variable 
    road_length_a: variable
    chambers_a: variable
    pots_a: variable
    """""
    def __init__(self,cabinets_a,verge_length_a,road_length_a,chambers_a,pots_a):
        self.cabinets_a = cabinets_a
        self.verge_length_a = verge_length_a
        self.road_length_a = road_length_a
        self.chambers_a = chambers_a
        self.pots_a = pots_a

    def card_A_rate_calculator(self):
        return (self.cabinets_a * 1000) + (self.verge_length_a * 50) + (self.road_length_a * 100) + (self.chambers_a * 200) + (self.pots_a * 100)
    
    

class Card_B:
    """"
    this class calculates the total rate of card B with the function card_B_rate_calculator with the given cost value for each attribute

    attributes:
    ------------

    cabinets_b: variable
    verge_length_b: variable 
    road_length_b: variable
    chambers_b: variable
    pots_b: variable
    """""
    def __init__(self, cabinets_b, verge_length_b, road_length_b, chambers_b, pots_b):
        self.cabinets_b =cabinets_b
        self.verge_length_b =verge_length_b
        self.road_length_b =road_length_b
        self.chambers_b =chambers_b
        self.pots_b = pots_b

    def card_B_rate_calculator(self):
        return (self.cabinets_b * 1200) + (self.verge_length_b *40) + (self.road_length_b *  80) + (self.chambers_b * 200) + ((self.verge_length_b + self.road_length_b) * 20)

if __name__=="__main__":
    
    print(f"\n")
    calculatorA=Card_A(load_graph.cabinets_rate,load_graph.verge_length,load_graph.road_length,load_graph.chamber_rate,load_graph.pot_rate)
    print(f"card A cost is £ {calculatorA.card_A_rate_calculator()}, \n")

    calculatorB=Card_B(load_graph.cabinets_rate,load_graph.verge_length,load_graph.road_length,load_graph.chamber_rate,load_graph.pot_rate)
    print(f"card B cost is £ {calculatorB.card_B_rate_calculator()}, \n")

    print(f"Total difference between Card A cost and Card B cost is £ {calculatorB.card_B_rate_calculator() - calculatorA.card_A_rate_calculator()}")

# %%
