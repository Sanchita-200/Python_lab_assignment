
fruits = {
    "apple",
    "banana",
    "orange",
    "mango",
    "grapes",
    "pineapple",
    "watermelon",
    "guava",
    "papaya",
    "strawberry"
}


summer_fruits = {
    "mango",
    "watermelon",
    "pineapple",
    "lychee",
    "muskmelon"
}


winter_fruits = {
    "apple",
    "orange",
    "guava",
    "strawberry",
    "kiwi"
}


result1 = summer_fruits - fruits

print("Summer fruits but not in fruits:")
print(result1)


result2 = (summer_fruits & winter_fruits) - fruits

print("\nSummer and winter fruits but not in fruits:")
print(result2)


if "orange" in fruits:
    print("\nOrange is present in fruits.")
else:
    print("\nOrange is not present in fruits.")


print("\nPineapple is present in:")

if "pineapple" in fruits:
    print("Fruits set")

if "pineapple" in summer_fruits:
    print("Summer fruits set")

if "pineapple" in winter_fruits:
    print("Winter fruits set")