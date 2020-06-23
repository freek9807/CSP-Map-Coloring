class CSP():

    failed = 0
    failed_paths = 0

    def __init__(self,colour):
        self.colour = colour
        pass

    def csp_solution(self,region,adj,actual = dict()):
        if len(region) == 0:
            return actual
        fst = max(region.items(), key=lambda x: len(x[1]))
        ls = region.copy()
        ls.pop(fst[0])
        curr = adj[fst[0]]
        for col in self.colour:
            isOkay = True
            for neir in curr:
                try:
                    if actual[neir] == col:
                        isOkay = False
                except:
                    pass

            if not isOkay:
                self.failed += 1
                continue
            curr_state = actual.copy()
            curr_state[fst[0]] = col
            call = self.csp_solution(ls,adj,curr_state)
            if call is not None:
                return call
            self.failed_paths += 1
            del curr_state
        return None