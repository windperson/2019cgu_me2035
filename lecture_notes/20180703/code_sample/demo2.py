#%%
def splitId(input):
    data = input.split(',')
    return (data[0], data[1], data[2])
#%%

( _ , y, z) = splitId("10,11,12")
#print("x= "+x)
print("y= "+y)
print("z= "+z)

#%%
set1 = {"1", "2", "3"}
set2 = {"3", "4", "5"}
print("union= ")
print(set1.union(set2))
print("intersect= ")
print(set1.intersection(set2))

#%%
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "other" : ['tool1', 'tool2']
}
dict["year"] = 2019
print(dict["year"])
print(dict["other"])
dict["seats"] = 4
if "seats" in dict:
    print("total seats: " + str(dict["seats"]))