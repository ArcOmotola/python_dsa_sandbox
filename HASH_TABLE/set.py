class CustomSet:
    def __init__(self):
       self.elements = {}
    
    def add(self, elem):
        """Add element to the set."""
        if elem not in self.elements:
            self.elements[elem] = True
    
    def contains(self, elem):
        """Check if element is in the set."""
        return elem in self.elements
    
    
    def remove(self, elem):
        """Remove element from the set. Raises KeyError if not present."""
        if elem in self.elements:
          self.elements[elem] = False
        else:
            raise KeyError(f"Element {elem} not found in the set.")
    
    def size(self):
        """Return the number of elements in the set."""
        len(self.elements)
    
    def __iter__(self):
        """Allows iteration over the set."""
        iter(self.elements)
    
    def __str__(self):
        """String representation of the set."""
        return "{" + ", ".join(str(elem) for elem in self.elements) + "}"

# Example usage
cs = CustomSet()
cs.add(1)
cs.add(2)
cs.add(3)

print(cs)  # Output: {1, 2, 3}
print(cs.contains(2))  # Output: True
print(cs.size())  # Output: 3

cs.remove(3)
print(cs)  # Output: {1, 2}

for item in cs:
    print(item)  # Outputs: 1 2
