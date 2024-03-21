# nums = {
#   1: "one",
#   2: "two",
#   3: "three",
# }

# print(nums[1])
# print(nums[2])
# print(nums[3])

# nums = {
#   1: "one",
#   2: "two",
#   3: "three",
# }

# keys_to_print = [1, 2, 3]

# for key in keys_to_print:
#     print(nums[key])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
keys_to_print = ["brand", "model", "year"]

for key in keys_to_print:
    print(thisdict[key])

for key, value in thisdict.items():
    print(key, ":", value)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)