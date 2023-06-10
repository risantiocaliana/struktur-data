def all_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph:
            return []
        paths = []
        for node in graph[start]:
            if not node in path:
                newpaths = all_path(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
def shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        shortest = None
        
        for node in graph[start]:
            if node not in path:
                newpath = shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
    
def find_ListShortestPath(Allpaths,ShortestPath):
    ListShortest = [];
    for path in Allpaths:
        if len(path) == len(ShortPath):
            ListShortest.append(path)
    return ListShortest

def displayBlock(Paths):
    for i in range(len(Paths)):
        print('Path',i+1,'=',Paths[i])
    
def find_AllEdge(graphs):
    ListEdge = []
    for keys in graphs.keys():
        if graphs[keys] != []:
            for value in graphs[keys]:
                temp = keys+' => '+value,
                ListEdge.append(temp)
    return ListEdge


graphSembarang = {
 'A': ['C','D','G'],
 'B': ['C','E','F','G'],
 'C': ['A','B','D','E'],
 'D': ['C','E','F'],
 'E': ['C','B',],
 'F': ['E'],
 'G': ['C']
 }
#print(find_path(graph, 'E', 'C'))
ListAll_Path = all_path(graphSembarang,'A','E')
print('\nAll Path : ')
displayBlock(ListAll_Path)
ShortPath = shortest_path(graphSembarang,'A','E')
ListShortestPath = find_ListShortestPath(ListAll_Path,ShortPath)
print('\nShortest Path and Alternative : ')
displayBlock(ListShortestPath)
SemuaEdge = find_AllEdge(graphSembarang)
print('\nAll Edge : ')
displayBlock(SemuaEdge)