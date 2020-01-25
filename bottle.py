#permutation : retourne tous les arrangements possibles de liste de longueur n.
permutation_list = []
for k in itertools.permutations("ABCD",2):
    permutation_list.append(k)
print("permutations")
print(permutation_list)