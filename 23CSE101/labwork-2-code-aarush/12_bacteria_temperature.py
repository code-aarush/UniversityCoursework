# ================================================================
#  SCENARIO
#  A biology lab tracks bacterial growth at different temperatures.
#  Each class of bacteria thrives in specific ranges.
#
#  LEARNING GOALS
#  • Nested conditions and comparisons
#  • Dictionaries and lambda expressions
#
#  PROBLEM DESCRIPTION
#  Classes and Ranges:
#     Hyperthermophile (t ≥ 60)
#     Thermophile (45 ≤ t ≤ 122)
#     Mesophile (20 ≤ t ≤ 45)
#     Psychrotrophs (t ≥ 0)
#     Psychrophiles (-15 ≤ t ≤ 10)
#
#  Input: n then n temperatures.
#  Output:y
#     For each temp → matching classes (| separated).
#     Then totals for each class (Name: count).
#  Print twice (manual and lambda list).
#
#  EXAMPLE
#     Input:
#       6
#       75 30 -10 25 0 50
#     Output (per temp + totals for both methods)
# ================================================================

n = int(input("Number of readings: "))
temps = list(map(int, input().split()))

# TODO 1 – Manual classification with if chains. Produce per-temp labels and totals.
per_manual = []   # list of strings like "Thermophile|Psychrotrophs"
totals_manual = {}  # dict of class -> count

for t in temps:
    labels = []

    if t >= 60:
        labels.append("Hyperthermophile")
    if 45 <= t <= 122:
        labels.append("Thermophile")
    if 20 <= t <= 45:
        labels.append("Mesophile")
    if t >= 0:
        labels.append("Psychrotrophs")
    if -15 <= t <= 10:
        labels.append("Psychrophiles")

    per_manual.append("|".join(labels))

    for label in labels:
        totals_manual[label] = totals_manual.get(label, 0) + 1

# TODO 2 – Use list of (name, lambda) and dict.get() to replicate the same.
CLASSES = [
    ("Hyperthermophile", lambda t: t >= 60),
    ("Thermophile",      lambda t: 45 <= t <= 122),
    ("Mesophile",        lambda t: 20 <= t <= 45),
    ("Psychrotrophs",    lambda t: t >= 0),
    ("Psychrophiles",    lambda t: -15 <= t <= 10),
]
per_builtin = []
totals_builtin = {}

for t in temps:
    labels = [name for name, cond in CLASSES if cond(t)]
    per_builtin.append("|".join(labels))
    for label in labels:
        totals_builtin[label] = totals_builtin.get(label, 0) + 1

# TODO 3 – Print per-temp lines (manual), then totals (manual).
# Then print per-temp lines (built-in), then totals (built-in).

for line in per_manual:
    print(line)

for name, count in totals_manual.items():
    print(f"{name}: {count}")


for line in per_builtin:
    print(line)

for name, count in totals_builtin.items():
    print(f"{name}: {count}")