import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
shoplist = ['a','b','c']
# Write to the file
f = open(shoplistfile, 'wb')

# Dump the object to a file
pickle.dump(shoplist, f)# 封装(pickling)
f.close()

# Destroy the list variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)# 解封(unpickling)
print(storedlist)
