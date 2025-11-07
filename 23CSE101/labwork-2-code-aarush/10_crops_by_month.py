# ================================================================
#  SCENARIO
#  A local farm shop wants a monthly board showing which crops
#  are currently harvested.
#
#  LEARNING GOALS
#  • Compound conditions and range checks
#  • Storing structured data in dictionaries
#
#  PROBLEM DESCRIPTION
#  Month → Crop Mapping
#     Wheat (3-4), Rice (9-10), Soybean (10-11),
#     Watermelon (5-6), Onion (2-3)
#  Input month number (1–12).
#  Output matching crops comma-separated or “No crops.”
#  Print twice (if-chain and dictionary lookup).
#
#  EXAMPLE
#     Input: 3
#     Output:
#        Wheat,Onion
#        Wheat,Onion
# ================================================================

month = int(input("Enter month (1-12): "))

# TODO 1 – Manual if statements for each crop.
crops_manual = []
if 3 <= month <= 4:
    crops_manual.append("Wheat")
if 9 <= month <= 10:
    crops_manual.append("Rice")
if 10 <= month <= 11:
    crops_manual.append("Soybean")
if 5 <= month <= 6:
    crops_manual.append("Watermelon")
if 2 <= month <= 3:
    crops_manual.append("Onion")

# HINT: append crop names when month is within range

# TODO 2 – Dictionary of (name: (start, end)) and loop through.
crops_builtin = []
ranges = {
    "Wheat": (3, 4),
    "Rice": (9, 10),
    "Soybean": (10, 11),
    "Watermelon": (5, 6),
    "Onion": (2, 3)
}

for crop, (start, end) in ranges.items():
    if start <= month <= end:
        crops_builtin.append(crop)
        
# HINT: ranges = {"Wheat": (3,4), ...}; if lo <= month <= hi: append

print(",".join(crops_manual) if crops_manual else "No crops")
print(",".join(crops_builtin) if crops_builtin else "No crops")

# REFLECTION:
# Which style is easier to maintain as the list grows?
