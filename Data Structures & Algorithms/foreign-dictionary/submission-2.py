class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #Lol enigma machine
        #Order of the letters unknown, uses english alphabet
        #Words is sorted lexographically?
        #Return empty string if it isn't
        #Return string of unique letters sorted lexographically
        #Return any solution if multiple
        #Well I'd like to have a graph?

        graph = defaultdict(list)
        all_chars = set()
        for c in words[0]:
            all_chars.add(c)
        for i in range(1, len(words)):
            first = words[i-1]
            second = words[i]
            for c in first:
                all_chars.add(c)
            for c in second:
                all_chars.add(c)
            
            diff_char = 0
            if first == second:
                continue
            while diff_char < len(first)-1 and first[diff_char] == second[diff_char]:
                diff_char += 1
                if diff_char == len(second) and diff_char < len(first):
                    #Deal with that prefix test case
                    return ""
                #Get us to where we actually get info about the language
            #At this point we know first and second are pointing at dif characters
            if first[diff_char] == second[diff_char]:
                continue
            graph[first[diff_char]].append(second[diff_char])
        
        #At this point graph has all the extracted info about letters that
        #The dictionary gives us
        print(graph)
        #Ok now in theory i can do a a dfs or bfs to figure out letters who's order i know
        #If i hit a cycle Return nothing
        #otherwise give an order?
        visited = dict()
        all_chars = list(all_chars)
        #The dfs will in theory give me the furthest along
        to_ret = []
        def dfs(to_visit):
            if to_visit in visited:
                return visited[to_visit]
            visited[to_visit] = True

            for child in graph[to_visit]:
                if dfs(child):
                    return True

            visited[to_visit] = False
            to_ret.append(to_visit)

        for c in all_chars:
            if dfs(c):
                return ""


            
        return "".join(reversed(to_ret))
            

        #And then i
