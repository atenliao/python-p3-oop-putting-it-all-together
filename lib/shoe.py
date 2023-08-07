#!/usr/bin/env python3

class Shoe:
    condition = None
    def __init__(self, brand, size) -> None:
        self.brand =brand
        self.size = size
        Shoe.condition = "New"
        pass
    

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if(type(value) != int):
            print("size must be an integer")
        self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")