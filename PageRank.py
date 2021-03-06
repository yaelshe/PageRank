import pandas as pd

# data structures
name_id_Dict = dict()
id_name_Dict = dict()
id_rank_Dict = dict()
id_neighbors_Dict = dict()
id_degree_Dict = dict()


# the function recieves as input the path for the input file as String
# The functin loads the graph from  a given file
def load_graph(path):
    df = pd.read_csv(path,header=None)
    id = 0
    # go through all edges in csv
    for index, row in df.iterrows():
        source = str(row[0])
        destination = str(row[1])
        # insert to name_id_dictionary with <name,id>
        if (not source in name_id_Dict):
            name_id_Dict[source] = id
            id_name_Dict[id] = source
            id += 1
        if not destination in name_id_Dict:
            name_id_Dict[destination] = id
            id_name_Dict[id] = destination
            id = id + 1
        sourceId = name_id_Dict[source]
        desId = name_id_Dict[destination]
        # insert to id_neighbors dictionary with <id,list>
        if (not desId in id_neighbors_Dict):
            id_neighbors_Dict[desId] = list()
        id_neighbors_Dict[desId].append(sourceId)
        # update degree of sourse
        if (not sourceId in id_degree_Dict):
            id_degree_Dict[sourceId] = 1
        else:
            id_degree_Dict[sourceId] += 1

    # initiate rank
    num_nodes = len(name_id_Dict)
    for name in name_id_Dict:
        id_rank_Dict[name_id_Dict[name]] = 1 / num_nodes
        if not name_id_Dict[name] in id_degree_Dict:
            id_degree_Dict[name_id_Dict[name]] = 0
        if not name_id_Dict[name] in id_neighbors_Dict:
            id_neighbors_Dict[name_id_Dict[name]] = list()
    print(id)


# The functin calcualates the page rank for each node in the graph
def calculate_page_rank(beta=0.85, delta=0.001):
    global id_rank_Dict
    i = 1
    difference = calculate_PR_iteration(beta)
    while (i <= 20 and difference > delta):
        difference = calculate_PR_iteration(beta)
        i += 1


# calculates one iteration of page rank, and return sum of difference between iteration
def calculate_PR_iteration(beta):
    global id_rank_Dict
    tempRanks = dict()
    difference = 0
    S = 0
    # for each node calc rank by its neighbors
    for nodeId in id_neighbors_Dict:
        currRank = 0
        # go through each neighbor
        for neighborId in id_neighbors_Dict[nodeId]:
            neighborRank = id_rank_Dict.get(neighborId)
            neighborDegree = id_degree_Dict[neighborId]
            rank = beta * (neighborRank / neighborDegree)
            currRank += rank
        S += currRank
        # save curr rank calculated
        tempRanks[nodeId] = currRank
        # add difference
        difference += abs(currRank - id_rank_Dict[nodeId])
    # update ranks according to current iteration
    # id_rank_Dict=dict.copy(tempRanks)
    for nodeId in id_rank_Dict:
        id_rank_Dict[nodeId] = tempRanks[nodeId] + ((1 - S) / len(id_rank_Dict))

    return difference


# The function gets the node name as String
# The function Returns the PageRank of a specific node
def get_PageRank(node_name):
    global name_id_Dict
    if (not node_name in name_id_Dict):
        return -1
    else:
        nodeId = name_id_Dict[node_name]
        return id_rank_Dict[nodeId]


# The function gets the amount of nodes to return as Integer - n
# The function Returns a list of n nodes with the highest PageRank.
# return result <node name, PageRank value >
def Get_top_nodes(n):
    result = list()
    # sort by rank and get top n
    sortedByRank = dict(sorted(id_rank_Dict.items(), key=lambda t: t[1], reverse=True)[:n])
    # convert id to name
    for oldKey, value in sortedByRank.items():
        name = id_name_Dict[oldKey]
        result.append(tuple((name, value)))
    return result


# The function returns a list of the PageRank for all the nodes in the graph
# result <node name, PageRank value >
def get_all_PageRank():
    # for number of nodes
    global name_id_Dict
    return Get_top_nodes(len(name_id_Dict))


# # MAIN
load_graph('d:\\documents\\users\\nogahm\\Downloads\\soc-sign-bitcoinalpha.csv')
calculate_page_rank()
print(Get_top_nodes(10))
