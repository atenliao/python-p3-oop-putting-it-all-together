#!/usr/bin/env python3

class Book:
    page_count =0
    def __init__(self,title, page_count):
        self.title=title
        self._page_count =page_count
        if(type(self.page_count) is int):
            print("it is integer")
        else:
            print("page_count must be an integer")
        
    @property
    def page_count(self):
        print("get page_count")
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if(type(value) != int):
            print("page_count must be an integer")
        else:
            print("it is integer")
        self._page_count = value
        
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    pass
    
        