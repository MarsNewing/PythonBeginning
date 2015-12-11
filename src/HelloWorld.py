movies=["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print("--- well I will show the first element in the array ---")
print(movies[0])
print("\n")

print("--- the array is ---")
print(movies)
print("\n")

print("--- append a element 'dream of queen' ---")
movies.append("dream of queen")
print(movies)
print("\n")

print("--- remove the last elementn ---")
movies.remove("dream of queen")
print(movies)
print("\n")

print("--- insert year for each movie ---")
year = [1989, 1995, 1999]
i = 0
for item in year:
    movies.insert(i*2+1,item)
    i=i+1

print(movies)
print("\n")


actor = ["lonado", "ming", "man"]
movies.append(actor)
print(movies)

def print_lol(array):
    for item in array:
        if isinstance(item,list):
            print_lol(item)
        else:
            print(item)

print_lol(movies)
