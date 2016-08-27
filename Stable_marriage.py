def stable_marriage(blue_dict, red_dict):
    """
    Takes both dictionaries of preferred partners on each side.
    Converts dictionary of proposers into list.
    Initialises dictionary of final matching.
    """
    pairing_list = {}
    free_blue_list = []
    
    for key, value in red_dict.items():
        pairing_list[key] = None
    
    for key, value in blue_dict.items():
        free_blue_list.append(key)
    """
    Iterates through list of proposers. 
    Each proposer proposes to their preferred proposee. 
    If proposee is unmatched or is in a less stable matching, the proposer is matched with the proposee and is removed from the list.
    In the case that a less stable matching is broken, the original proposer appended to the list.
    Halts when every proposer is in a marriage.
    """
    while free_blue_list != []: 

        proposer = free_blue_list[0]
        proposee = blue_dict[proposer][0] 
        proposee_pref = red_dict[proposee].index
        current_suitor = pairing_list[proposee]
            
        if current_suitor == None:
        
            free_blue_list.remove(proposer)
            pairing_list[proposee] = proposer
            
            print(proposer +' proposes and marries '+ proposee + '.')
        
        elif proposee_pref(current_suitor) > proposee_pref(proposer):
        
            free_blue_list.append(current_suitor)
            free_blue_list.remove(proposer)
            blue_dict[current_suitor].remove(proposee)
            pairing_list[proposee] = proposer
            
            print(proposer + ' intercepts ' + current_suitor + ' and marries ' + proposee + '.')
        
        else:
            
            blue_dict[proposer].remove(proposee)
            print(proposer + ' proposes and is rejected by ' + proposee + '.')
       
    print(pairing_list)
    return pairing_list
