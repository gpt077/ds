hash_table=[[] for _  in range(10)]
print(hash_table)

def insert(hash_table,key, value):
    hash_key=hash(key) % len(hash_table)
    key_exists=False
    bucket=hash_table[hash_key]
    for i ,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            key_exists=True
            break
    if key_exists:
        bucket[i]=((key,value))
    else:
        bucket.append((key,value))


def search(hash_table,key):
    hash_key=hash(key)% len(hash_table)
    bucket=hash_table[hash_key]
    for i , kv  in enumerate(bucket):
        k,v=kv
        if key == k:
            return v


def delete(hash_table,key):
    hash_key=hash(key) % len(hash_table)
    key_exists=False
    bucket=hash_table[hash_key]
    for i ,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            key_exists=True
            break

    if key_exists:
        del bucket[i]
        print("key {} deleted".format(key))
    else:
        print("key {} not found".format(key))


insert(hash_table,10, 'Nepal')
insert(hash_table,25, 'USA')
insert(hash_table,20, 'India')
print(hash_table)

print(search(hash_table,10))
print(search(hash_table,20))
print(search(hash_table,30))

delete(hash_table,100)
print(hash_table)
delete(hash_table,20)
print(hash_table)
