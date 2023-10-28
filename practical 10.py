def display_hash(hashTable):

    for i in range (len(hashTable)):
        print (i,end="")

        for j in HashTable[i]:
            print("-->",end = "")
            print(j,end=" ")
        print()
HashTable=[[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert (HashTable,keyvalue, value):

    hash_key =Hashing(keyvalue)
    HashTable[hash_key].append(value)

insert(HashTable, 10, 'Allahabad')
insert(HashTable, 25, 'mumbai')
insert(HashTable, 20, 'dellhi')
insert(HashTable, 9, 'mathura')
insert(HashTable, 21, 'punjab')
insert(HashTable, 21, 'noida')

display_hash (HashTable)
