
class CommandParser:

    def __init__(self, keywords = {}):
        self.keywords = keywords

    """
    Returns the predicate of the action.
    """
    def getPredicate(self, action, room):
        # build a list of candidates and pick the longest one
        candidates = []
        for candidate in self.keywords:
            if(action.startswith(candidate)):
                candidates.append(candidate)

        for candidate in room.moves:
            print(candidate)
            if(action.startswith(candidate)):
                candidates.append(candidate)
        
        longestCandidate = ""
        for candidate in candidates:
            if(len(candidate) > len(longestCandidate)):
                longestCandidate = candidate
        
        return longestCandidate

    """
    Returns the keyword that the action's actual predicate was mapped to.
    """
    def getKeyword(self, predicate, room):
        if(predicate in self.keywords):
            return self.keywords[self.getPredicate(action, room)]
        elif(predicate in room.moves):
            return "move"
        else:
            return ""

    """
    Returns the action with the predicate removed.
    """
    def removePredicate(self, action, predicate):
        return action[len(predicate):].strip()