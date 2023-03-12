class Order:

    Date = ''
    Status = ''
    ShoppingCart = ''
    DeliveryAddress = ''
    PaymentMethod = ''

    def validatePayment(self):
        print("Validating Payment...")
        self.Status = "Payment Validated"

    def cancel(self):
        print("Cancelling Order...")
        self.Status = "Cancelled"

    def dispatch(self):
        print("Dispatching Order...")
        self.Status = "Dispatched"

    def confirmDelivery(self):
        print("Confirming Delivery...")
        self.Status = "Delivered"

    def refund(self):
        print("Refunding Order...")
        self.Status = "Refunded"

    def archive(self):
        print("Archiving Order...")
        self.Status = "Archived"