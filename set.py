nums=tuple(input("Sandardy jaz: ").split(","))
nums2=tuple(input("Sandardy jaz:").split(","))

total = len(set(nums).intersection(set(nums2)))
print(total)
