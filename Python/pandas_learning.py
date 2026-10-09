import pandas as pd

# What is Pandas?
# Sort of like MS Excel for python programming built on top of NumPy
# Used for storing, accessing and manipulating data
# Has mainly two data storers: Series (Labelled Column), and DataFrame(labelled Rows and Columns)

series = pd.Series([1, 2, 3, 4])
print(series)

# This ^ will index them like 0, 1, 2, 3
# Custom indices can be added using second parameter in pd.Series(, index = )

l = ["Darshan", "Rahul", "Rohan", "Mohan"]
series = pd.Series(l, index = ["A", "B", "C", "D"])
print(series)

# Accessing by Label
print(series.loc["A"])

# Accessing by index
print(series.iloc[0])

# DataFrame

# Converting from Dictionary to DataFrame

dict1 = {
    "Name" : ["Walter White", "Saul Goodman", "Hank Schrader", "Mike Ehrmantraut", "Jesse Pinkman", "Tuco Salamanca", "Gus Fring"],
    "Job" : ["Teacher", "Lawyer", "Policeman", "Secret Agent", "Unemployed", "Mafia", "Businessman"],
    "Age" : [52, 45, 47, 72, 22, 56, 60]
}

df = pd.DataFrame(dict1)
print(df)

print(df.loc[2])        # Returns Hank

# Adding new rows to a DataFrame
# Best way is to create a new DataFrame and concatenate them

df_new = pd.DataFrame([{
    "Name" : "Hector Salamanca",
    "Job" : "Cartel",
    "Age" : 80}])
df = pd.concat([df, df_new])
print(df)

# Reading a CSV and converting it to a DataFrame

df = pd.read_csv("data.csv", index_col = "Name")        # Change the index, here instead of 1 2 3, its the name of that Pokemon
print(df)

# Accessing by label

print(df.loc["Pikachu"])

# Making a retrieval system:

pokemon = input("Enter a pokemon name to get its stats: ")
print(df.loc[pokemon])

# Filtering Data: Only keeping those rows that pass a certain condition

df_new = df[df["Height"] >= 1.5]
print(df_new)

psychic_pokemon = df[(df["Type1"] == "Psychic") | (df["Type2"] == "Psychic")]
print(psychic_pokemon)              # Used a C-Style 'or' operator: not or, similar to NumPy

# Aggregate Functions!

print(df.sum(numeric_only = True))
# For the entire table

# Prints      No            11325.0
#             Height          180.0
#             Weight         6934.7
#             Legendary         4.0
#             dtype:        float64

print(df["Height"].mean())
# 1.2: The average height

# Grouping Data Together: Group By

group = df.groupby("Type1")

print(group["Height"].mean())

"""
Type1
Bug         0.900000
Dragon      2.666667
Electric    0.855556
Fairy       0.950000
Fighting    1.185714
Fire        1.216667
Ghost       1.466667
Grass       1.083333
Ground      0.850000
Ice         1.550000
Normal      0.986364
Poison      1.221429
Psychic     1.371429
Rock        1.844444
Water       1.300000
Name: Height, dtype: float64

"""

# Data Cleaning
# 80% of work involving Pandas is actually data cleaning!

# 1. Drop irrelevant columns

df = df.drop(columns=["Legendary", "Type2"])
print(df)

# 2. Handling Missing Values

# 2(a): Dropping them completely
df = df.dropna(subset=["Type2"])        # Removes any row which has NaN for Type2
print(df)

#2(b): Replacing them with something meaningful / appropriate for analysis / computation

df = pd.read_csv("data.csv")

df = df.fillna({"Type2": "None"})
print(df)

#3: Fix inconsistent values

df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})
print(df)

#4. Fix Data Type: Here, Legendary Pokemons are marked as 1
#   We want them to be True, and False conversely, thus we change the 
#   data type from int to bool

df["Legendary"] = df["Legendary"].astype(bool)
print(df)

#5. Remove Duplicates: If the data contains multiple rows, we can use this function

df = df.drop_duplicates()

# The end
