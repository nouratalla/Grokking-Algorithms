from collections import deque

def is_mango_seller(name):
     return name[-1] == 'm' # this is the condition in book
 
    
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_q = deque()
    search_q += [name]
    searched = [] # to keep track of searched people and prevent infinite loops
    
    while search_q:
        person = search_q.popleft()
        if person in searched:
            continue
        if is_mango_seller(person):
            print('Mangpo seller found and his name is ' + person)
            return True
        
        search_q += graph[person]
        searched.append(person)
    
    return False

search("you")
        
    