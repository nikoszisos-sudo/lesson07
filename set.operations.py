A = {1,2,3,4}
B = {4,5}
print("union: " + str(A | B))
print("intersection: " + str(A & B))
print("difference A-B: " + str(A - B))
print("difference B-A: " + str(B - A))
print("symmetric_difference: " + str(A ^ B))
print("A subset B: " + str(A.issubset(B)))
print("A, B disjoint: " + str(A.isdisjoint(B)))

A.update(B)
print("A= A | B: " + str(A))
A.intersection_update(B)
print("A= A & B: " + str(A))
