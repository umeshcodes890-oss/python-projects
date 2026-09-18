class HashTable:
    def __init__(self):
        # Initialize the collection attribute to an empty dictionary
        self.collection = {}

    def hash(self, key: str) -> int:
        # Sum the Unicode values of each character in the string key
        return sum(ord(char) for char in key)

    def add(self, key: str, value):
        # Compute the hash of the key
        hash_value = self.hash(key)
        
        # If the hash value doesn't exist yet, initialize a nested dictionary
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
            
        # Store the key-value pair inside the nested dictionary
        self.collection[hash_value][key] = value

    def remove(self, key: str):
        # Compute the hash of the key
        hash_value = self.hash(key)
        
        # Confirm if the hash value and the specific key exist in the collection
        if hash_value in self.collection and key in self.collection[hash_value]:
            # Delete only the specific key-value pair from the nested dictionary
            del self.collection[hash_value][key]
            
            # Optional cleanup: if the nested dictionary is now empty, remove the hash key
            if not self.collection[hash_value]:
                del self.collection[hash_value]

    def lookup(self, key: str):
        # Compute the hash of the key
        hash_value = self.hash(key)
        
        # Safely retrieve the nested dictionary and look up the key
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
            
        # Return None if the key does not exist
        return None
