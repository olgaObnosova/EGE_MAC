graph=((1,2,3),(0,4,5),(0,5,6),(0,6,7),(1,5),(1,2,4,8),(2,3,7,8,9),(3,6),(5,6,9),(6,8))
 
def get_vertex(gr,v,chk):
    res=[]
    for a in gr[v]:
        if a not in chk:
            res.append(a)
    return res        
 
def bfs(gr,start):
    que=[start]
    chk=[start]
    tree=[]
    while (len(que)>0):
        v=que.pop()
        z=get_vertex(gr,v,chk)
        for w in z:
            que=[w]+que
            chk.append(w)
            tree.append((v,w))
    return tree
    
def get_path(tree,start,finish):
    curr=finish
    length=0
    path=[]
    while curr != start:
        for pair in tree:
            if pair[1]==curr:
                path.append(pair)
                length+=1
                curr=pair[0]
                break
    return (path[::-1],length)        
 
def task(graph,start,finish):
    tr=bfs(graph,start)
    return get_path(tr,start,finish)
    
print(task(graph,0,9))
