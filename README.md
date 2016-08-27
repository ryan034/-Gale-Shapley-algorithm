Implementation of the Gale Shapley algorithm with O(n^2) complexity. <https://en.wikipedia.org/wiki/Stable_marriage_problem>

Input is two dictionaries of the proposers and proposees respectively. Each key correspond to a list of preferred partners in descending order. The routine prints a line when a proposal is accepted or rejected and whenever a less preferred marriage is broken in place of a more preferred one. The final output is a dictionary of a stable matching between the key, value pairs. Note the algorithm is proposer optimal and may be proposee pessimal.   

eg.
```
men = {'abe': ['abi', 'bea', 'cath', 'dee'],
'bob': ['cath', 'abi', 'dee', 'bea'],
'col': ['abi', 'dee', 'bea', 'cath'],
'dan': ['abi', 'bea', 'cath', 'dee']}

women = {'abi': ['col', 'abe', 'dan', 'bob'],
'bea': ['bob', 'col', 'abe', 'dan'],
'cath': ['bob', 'abe', 'col', 'dan'],
'dee': ['dan', 'bob', 'col', 'abe']}

stable_marriage(men, women)    
```
Output:
``` 
dan proposes and marries abi
bob proposes and marries cath
abe intercepts dan and marries abi
col intercepts abe and marries abi
dan proposes and marries bea
abe intercepts dan and marries bea
dan proposes and is rejected by cath
dan proposes and marries dee
{'cath': 'bob', 'dee': 'dan', 'abi': 'col', 'bea': 'abe'}
```

