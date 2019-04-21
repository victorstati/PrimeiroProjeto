# Tuplas NAO podem ser alteradas

dimens = (200, 5)
print(dimens[0])
print(dimens[1])

for dimen in dimens:
    print(dimen)

print()
print()

dimens = (200, 5)
print("Original dimensions:")
for dimen in dimens:
    print(dimen)

dimens = (400, 100)
print("\nModified dimensions")
for dimen in dimens:
    print(dimen)