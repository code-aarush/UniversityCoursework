# ================================================================
#  SCENARIO
#  Two lab sections submit partner lists. You must merge them
#  alternately (A1, B1, A2, B2, …) and append leftovers.
#
#  LEARNING GOALS
#  • Index manipulation and while loops
#  • zip() and list concatenation
#
#  PROBLEM DESCRIPTION
#  Input: two lines of roll numbers.
#  Output: interleaved list printed twice (manual and zip()).
#
#  EXAMPLE
#     Input:
#       A1 A2 A3
#       B1 B2
#     Output:
#       A1 B1 A2 B2 A3
#       A1 B1 A2 B2 A3
# ================================================================

a = input("List A: ").split()
b = input("List B: ").split()

# TODO 1 – Manual merging with index counters.
merged_manual = []
i = 0
j = 0

while i < len(a) or j < len(b):
    if i < len(a):
        merged_manual.append(a[i])
        i += 1
    if j < len(b):
        merged_manual.append(b[j])
        j += 1

# HINT: use i, j indices and alternate appends

# TODO 2 – Use zip() then append leftover elements.
merged_builtin = []
merged_builtin = []

for x, y in zip(a, b):
    merged_builtin.append(x)
    merged_builtin.append(y)

if len(a) > len(b):
    merged_builtin.extend(a[len(b):])
else:
    merged_builtin.extend(b[len(a):])


# HINT: for x,y in zip(a,b): out += [x,y]; then extend the remainder

print(" ".join(merged_manual))
print(" ".join(merged_builtin))

# REFLECTION:
# Which version took fewer lines but remained clear?
