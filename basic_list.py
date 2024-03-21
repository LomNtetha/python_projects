movies = ["Avatar", "Titanic", "Avengers","John", "Lumkile"]
# print (movies[:2])
# for movie in movies:
#     print(movie)

# for i in range(2):  # Looping through the first two elements
#     print(movies[i])

# for movie in movies[-2:]:  # Iterate over the last two elements
#     print(movie)

# Slice the list to exclude the first and last elements
# for i in movies[1:-1]:
#     print(i)

# index = 0
# while index < len(movies):
#     print(movies[index])
#     index += 1

n = [2, 4, 6, 8]
res = 2
for x in n[1:3]:
  res *= x
print(res)