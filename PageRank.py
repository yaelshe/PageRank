import pandas as pd

#data structures
name_id_Dict= dict()
id_rank_Dict= dict()
id_neighbors= dict()

# default values
beta=0.85
lamda=0.001

# the function recieves as input the path for the input file as String
# The functin loads the graph from  a given file
def load_graph(path):
    df = pd.read_csv(path)
    id=0
    # go throw all edges in csv
    for index, row in df.iterrows():
        source = row[0]
        destination = row[1]
        # insert to name_id_dictionary with <name,id>
        if(not source in name_id_Dict):
            name_id_Dict[source]= id
            id=id+1
        if (not destination in name_id_Dict):
            name_id_Dict[destination] = id
            id = id + 1
        sourceId=name_id_Dict[source]
        desId = name_id_Dict[destination]
        # insert to id_neighbors dictionary with <id,list>
        if(not desId in id_neighbors):
            id_neighbors[desId]= list()
        id_neighbors[desId].append(sourceId)
    #initiate rank
    num_nodes=len(name_id_Dict)
    for nodeId in name_id_Dict:
        id_rank_Dict[nodeId]=1/num_nodes
    print(id)
load_graph('d:\\documents\\users\\sheinbey\\Downloads\\Wikipedia_votes.csv')
print ('nogah is the queen')



#
# # The functin calcualates the page rank for each node in the graph
# def calculate_page_rank():
#
# # The function gets the node name as String
# # The function Returns the PageRank of a specific node
# def get_PageRank(node_name):
#
# # The function gets the amount of nodes to return as Integer - n
# # The function Returns a list of n nodes with the highest PageRank.
# def Get_top_nodes(n):
# # result <node name, PageRank value >
#
# # The function returns a list of the PageRank for all the nodes in the graph
# def get_all_PageRank():
# # result <node name, PageRank value >



# id, name - dic
# 1
# id, list
# of
# neighbors - dic2
# id, currentRank - dic3
