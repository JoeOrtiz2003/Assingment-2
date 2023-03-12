class Item:

    Code = ''
    Title = ''
    Description = ''
    Category = ''
    Picture = ''
    QuantityInStock = 0
    Price = 0

    def viewFullDescription(self):
        print(f"Code: {self.Code}")
        print(f"Title: {self.Title}")
        print(f"Description: {self.Description}")
        print(f"Category: {self.Category}")
        print(f"Picture: {self.Picture}")
        print(f"Quantity in Stock: {self.QuantityInStock}")
        print(f"Price: {self.Price}")

    def addToCart(self, Quantity):
        if Quantity > self.QuantityInStock:
            print("Error: Not Enough stock.")
            return False
        self.QuantityInStock -= Quantity
        return True

    def updateStockLevel(self, Quantity):
        self.QuantityInStock += Quantity