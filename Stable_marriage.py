def stable_marriage(blue_dict, red_dict):
    
    pairing_list = {}
    free_blue_list = []
    
    for key, value in red_dict.items():
        pairing_list[key] = None
    
    for key, value in blue_dict.items():
        free_blue_list.append(key)
    
    while free_blue_list != []: 

        proposer = free_blue_list[0]
        proposee = blue_dict[proposer][0] 
        proposee_pref = red_dict[proposee].index
        current_suitor = pairing_list[proposee]
            
        if current_suitor == None:
        
            free_blue_list.remove(proposer)
            pairing_list[proposee] = proposer
            
            print(proposer +' proposes and marries '+ proposee)
        
        elif proposee_pref(current_suitor) > proposee_pref(proposer):
        
            free_blue_list.append(current_suitor)
            free_blue_list.remove(proposer)
            blue_dict[current_suitor].remove(proposee)
            pairing_list[proposee] = proposer
            
            print(proposer + ' intercepts ' + current_suitor + ' and marries ' + proposee)
        
        else:
            
            blue_dict[proposer].remove(proposee)
            print(proposer + ' proposes and is rejected by ' + proposee)
       
    print(pairing_list)
    return pairing_list
