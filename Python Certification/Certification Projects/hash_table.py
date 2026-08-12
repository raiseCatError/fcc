class HashTable:


    def __init__(self):

        self.collection = {}


    def hash(self, unhashed_input: str) -> int:

        unicode_hash = 0

        for each_char in unhashed_input:
            unicode_hash += ord(each_char)

        return unicode_hash


    def add(self, key: str, value: str):

        hashed_key = self.hash(key)

        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        self.collection[hashed_key][key] = value

        return


    def remove(self, key: str):
        
        hashed_key = self.hash(key)

        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
            
        return

    def lookup(self, key: str):
        
        hashed_key = self.hash(key)

        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        
        return


    def __str__(self):
        return self.name

cat = HashTable()

fcc = HashTable()

print(fcc.hash('fcc'))
print(fcc.hash('cfc'))

print(cat.hash('meow'))
cat.add('meow', 'purr')
cat.add('meowa', 'peurr')
cat.add('meoww', 'peurr')
print(cat.collection)
cat.remove('meow')
print(cat.collection)
cat.lookup('meowa')