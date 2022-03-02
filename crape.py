class Crape:
    def __init__(self, crape, crape_p):
        self.crape = crape
        self.crape_p = crape_p
        
    def price_crape(self):
        price = self.crape_p(self)
        return price
        
    def __repr__(self):
        statement = "ราคาเครป : {}"
        return statement.format(self.price_crape())

    
def Charcoal(order):
    crape = order.crape
    price = 0
    if crape["batter"] == "charcoal":
        if crape["salty"] == "egg":
            price += 10
        if  crape["salty"] == "chili":
            price += 10
        if  crape["salty"] == "flossyPork":
            price += 10
        if  crape["salty"] == "ham":
            price += 15

        if crape["sweet"] == "foiThong":
            price += 10
        if crape["sweet"] == "custard":
            price += 10
        if crape["sweet"] == "choco":
            price += 10
        if crape["sweet"] == "jelly":
            price += 10
        if crape["sweet"] == "nutella":
            price += 10
            
        if crape["topping"] == "banana":
            price += 10
        if crape["topping"] == "cheese":
            price += 10
        if crape["topping"] == "tuna":
            price += 25
        if crape["topping"] == "crabStick":
            price += 20 
        
        if crape["sauce"] == "chocolate":
            price += 10
        if crape["sauce"] == "strawberry":
            price += 10
        if crape["sauce"] == "caramel":
            price += 10
        return price

def Normal(order):
    crape = order.crape
    price = 0
    if crape["batter"] == "normal":
        if crape["salty"] == "egg":
            price += 5
        if  crape["salty"] == "chili":
            price += 5
        if  crape["salty"] == "flossyPork":
            price += 5
        if  crape["salty"] == "ham":
            price += 10

        if crape["sweet"] == "foiThong":
            price += 10
        if crape["sweet"] == "custard":
            price += 10
        if crape["sweet"] == "choco":
            price += 10
        if crape["sweet"] == "jelly":
            price += 10
        if crape["sweet"] == "nutella":
            price += 10
            
        if crape["topping"] == "banana":
            price += 10
        if crape["topping"] == "cheese":
            price += 10
        if crape["topping"] == "tuna":
            price += 25
        if crape["topping"] == "crabStick":
            price += 20 
        
        if crape["sauce"] == "chocolate":
            price += 5
        if crape["sauce"] == "strawberry":
            price += 5
        if crape["sauce"] == "caramel":
            price += 10
        return price
