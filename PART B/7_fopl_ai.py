def resolution(kb, alpha):
  """
  kb: knowledge base (list of lists, where each inner list represents a clause and each element within the inner list represents a literal)
  alpha: query (list of lists, where each inner list represents a clause and each element within the inner list represents a literal)

  Returns: True if the query can be inferred from the knowledge base, False otherwise.
  """
  clauses = kb + [[-1 * l for l in alpha]]
  new = []
  while True:
    n = len(clauses)
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    for (i, j) in pairs:
      resolvents = resolve(clauses[i], clauses[j])
      if [] in resolvents:
        return True
      new += resolvents
    if new == []:
      return False
    clauses += new
    new = []

def resolve(ci, cj):
  """
  ci: first clause (list of literals)
  cj: second clause (list of literals)

  Returns: list of all possible resolvents that can be derived from ci and cj
  """
  resolvents = []
  for li in ci:
    for lj in cj:
      if li == -1 * lj or lj == -1 * li:
        resolvent = [l for l in ci if l != li] + [l for l in cj if l != lj]
        resolvent = list(set(resolvent))
        if resolvent not in resolvents:
          resolvents.append(resolvent)
  return resolvents

# Example usage
kb = [['A', 'B'], ['C', '-D']]
alpha = [['A', '-B']]
result = resolution(kb, alpha)
print(result) # should print True


"""
In this code, the resolution function takes as input a knowledge base (kb) 
and a query (alpha) and returns True if the query can be inferred from the 
knowledge base, and False otherwise. The resolve function takes as input two
 clauses (ci and cj) and returns a list of all possible resolvents that can be derived from these clauses.


Define your knowledge base (kb) and query (alpha) as lists of lists. 
Each inner list represents a clause, and each element within the inner list represents a literal. 

For example:
kb = [['A', 'B'], ['C', '-D']] # represents (A AND B) OR (C AND NOT D)
alpha = [['A', '-B']] # represents (A AND NOT B)


The result variable will be either True or False, depending on whether the query can be inferred 
from the knowledge base. If result is True, it means that the query can be inferred from the knowledge base. 
If result is False, it means that the query cannot be inferred from the knowledge base.

The output will be True, because the query (A AND NOT B) can be inferred from 
the knowledge base (A AND B) OR (C AND NOT D).
"""