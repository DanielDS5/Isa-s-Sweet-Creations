class Cart:
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"]={}
        self.cart = cart
            
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
            
    def add(self, product):
        if(str(product.id) not in self.cart.keys()):
            self.cart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "price": product.price,
                "amount": 1,
                "img": product.image.url
            }
            
        else:
            self.cart[str(product.id)]["amount"] = self.cart[str(product.id)]["amount"] + 1
            self.cart[str(product.id)]["price"] += product.price
            
            
        self.save()
        
    def delete(self, product):
        product.id = str(product.id)
        
        if product.id in self.cart:
            del self.cart[product.id]
        
        self.save()
        
    def substract(self, product):
        if self.cart[str(product.id)]["amount"] == 1:
            self.delete(product)
        else:
            self.cart[str(product.id)]["amount"] = self.cart[str(product.id)]["amount"] - 1
            self.cart[str(product.id)]["price"] -= product.price
            
        self.save()
        
    def clean(self):
        self.session["cart"]={}
        self.save()