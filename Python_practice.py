print("Hello World!")
print(type(3))
print(type(34.12))
print(type('True'))
print(type(True))
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16- 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)

counties = ["Arapahoe","Denver","Jefferson"]
my_list = []

# slicing
# list[start : end]
print(counties[1:])
print(counties[1:3])
print(counties[1:2])
counties.append("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties.append("El Paso")
print(counties)
counties.pop(-1)
print(counties)

print('----------------------------')

# Add El Paso to the second position in the list.
counties[1] = "El Paso"
print(counties)
# Remove Arapahoe from the list.
counties.remove("Arapahoe")
print(counties)

# Make Denver the third item in the list, but keep Jefferson the second item in the list
counties.append("Denver")
print(counties)

# Add Arapahoe to the list.
counties.append("Arapahoe")
print(counties)

print('-------------------------------')
# tuple
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(counties_tuple[:-2])
print(counties_tuple[:2])
print(counties_tuple[:-1])
print(counties_tuple[1:2])

# Dictionaries
print('------------------------')
# create dictionary
my_dictionary = {}
my_dictionary = dict()
counties_dict = dict()
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
# get all keys
print(counties_dict.keys())
# get values
print(counties_dict.values())
# get specific value
print(counties_dict.get("Denver"))
print(counties_dict['Arapahoe'])
print(counties_dict[('Arapahoe')])
print(counties_dict.get('Arapahoe'))

# List of dict
print('-----------------------')
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
# Get the length of the voting_data list of dictionaries.
print("len of list :{}".format(len(voting_data)))
# Use indexing and slicing to get one or more dictionaries.
print("[:2] : {}".format(voting_data[:2]))
print("[1:2] : {}".format(voting_data[1:2]))
print("[:-1] : {}".format(voting_data[:-1]))
print("[1:] : {}".format(voting_data[1:]))
# Use the append(), insert(), and remove() methods to add and remove one or more dictionaries.
# Add the new county “El Paso” and its registered voters, 461149, to the second position in voting_data.
voting_data[1] = ({"county":"El Paso", "registered_voters": 461149})
print("dict:{}".format(voting_data))
# Remove “Arapahoe” and its registered voters from voting_data.
voting_data.pop(0)
print("dict:{}".format(voting_data))
# Make “Denver” and its registered voters the third item in voting_data,
voting_data.append({"county":"Denver", "registered_voters": 463353})
# but keep “Jefferson” and its registered voters as the second item.
print("dict:{}".format(voting_data))
# Add “Arapahoe” and its registered voters to voting_data.
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print("dict:{}".format(voting_data))


# CONDITIONS
print('------------------------------------')
# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# AND
x = 5
y = 5
if x == 5 and y == 5:
    print("True")
else:
    print("False")

# OR
if x == 3 or y == 5:
    print("True")
else:
    print("False")

# NOT
if not(x > y):
    print("True")
else:
    print("False")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# Loops
print('------------------ LOOP ----------------------')
x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])
print(" ")

print('-------- touple -----------')
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
for i in range(len(counties_tuple)):
      print(counties_tuple[i])

# print(" ")
# for i in len(counties_tuple):
#       print(counties_tuple[i])

print(" \nin ")
for county in counties_tuple:
      print(county)

print('\n ------------- DICT ----------------')
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

print(" ")
for county in counties_dict.keys():
    print(county)
print(" ")

for voters in counties_dict.values():
    print(voters)

print(" ")
for county in counties_dict:
    print(counties_dict[county])

print(" ")
for county in counties_dict:
    print(counties_dict.get(county))

print(" ")
for county, voters in counties_dict.items():
    print("{} county has {} registered voters".format(county, voters))

print(" ")
for i in range(len(voting_data)):
      print(voting_data[i])

print(' ------------------ ')
print(" \nrange ")
for county in range(len(voting_data)):
     print(county)

print("\n kay val")
for county_dict in voting_data:
     for key, value in county_dict.items():
         print(value)

print(" \nvalue ")
for county_dict in voting_data:
    print(county_dict)
    print(county_dict['registered_voters'])

print(" \n val 1")
for county_dict in voting_data:
   for value in county_dict:
       print(value)

print("\n final val")
for county_dict in voting_data:
     print(county_dict.values())

# --------------------------------------------------
# FSTRING
print("\n------------------- FSTRING--------------------")
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

print("\n")
for county_dict in voting_data:
    # print(counties_dict)
    # print(county_dict["county"])
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")

