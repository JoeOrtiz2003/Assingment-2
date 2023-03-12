class Shop:

    Name = ''
    Description = ''
    ListOfCategories = ''
    ListOfItems = ''
    URL = ''

    def viewCategory(self, Category):
        print(f"Showing items in the {Category} category:")
        for item in self.ListOfItems:
            if item.Category == Category:
                print(f"{item.Title} ({item.Price})")

    def searchItems(self, Keyword):
        print(f"Searching for items with keyword '{Keyword}':")
        for item in self.ListOfItems:
            if Keyword in item.Title or Keyword in item.Description:
                print(f"{item.Title} ({item.Price})")

    def viewItems(self):
        print("Showing all items:")
        for item in self.ListOfItems:
            print(f"{item.Title} ({item.Price})")

    def viewShoppingCart(self, Cart):
        Total = 0
        print("Shopping Cart Contents:")
        for item in Cart:
            print(f"{item.Title} ({item.Price})")
            Total += item.Price
        print(f"Total cost: {Total}")