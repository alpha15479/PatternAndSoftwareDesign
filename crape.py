class Crape:
    def __init__(self, crape, crape_p, format_):
        self.crape = crape
        self.crape_p = crape_p
        self.title = 'Monthly report'
        self.text = ['Things are going', 'really, really well.']
        self.format_ = format_
        
    def price_crape(self):
        price = self.crape_p(self)
        return price
        
    def __repr__(self):
        statement = "Order : {}"
        return statement.format(self.price_crape())

class Handler(Crape):
    
    def __init__(self, crape, crape_p):
        self.crape = crape
        self.crape_p = crape_p
        
    def Charcoal(self, request):
        self.nextHandler.handle(request)
        
    def Normal(self, request):
        self.nextHandler.handle(request)

class Charcoal(Handler):
    
    def Charcoal(order):
        crape = order.crape
        price = 0
        result = ""
        if crape["batter"] == "charcoal":
            if crape["salty"] == "egg":
                price += 10
                result += ("egg + ")
            if  crape["salty"] == "chili":
                price += 10
                result+=("chili + ")
            if  crape["salty"] == "flossyPork":
                price += 10
                result+=("flossyPork + ")
            if  crape["salty"] == "ham":
                price += 20
                result+=("ham + ")

            if crape["sweet"] == "foiThong":
                price += 15
                result+=("foiThong + ")
            if crape["sweet"] == "custard":
                price += 10
                result+=("custard + ")
            if crape["sweet"] == "choco":
                price += 10
                result+=("choco + ")
            if crape["sweet"] == "jelly":
                price += 10
                result+=("jelly + ")
            if crape["sweet"] == "nutella":
                price += 15
                result+=("nutella + ")
                
            if crape["topping"] == "banana":
                price += 10
                result+=("banana + ")
            if crape["topping"] == "cheese":
                price += 10
                result+=("cheese + ")
            if crape["topping"] == "tuna":
                price += 25
                result+=("tuna + ")
            if crape["topping"] == "crabStick":
                price += 20 
                result+=("crabStick + ")
            
            if crape["sauce"] == "chocolate":
                price += 10
                result+=("chocolate")
            if crape["sauce"] == "strawberry":
                price += 10
                result+=("strawberry")
            if crape["sauce"] == "caramel":
                price += 15
                result+=("caramel")
            return "แป้งชาร์โคล " + str(price) +" บาท", result
        
    def Normal(self, request):
        self.nextHandler.handle(request)

class Normal(Handler):
    
    def Charcoal(self, request):
        self.nextHandler.handle(request)
         
    def Normal(order):
        crape = order.crape
        price = 0
        result = ""
        if crape["batter"] == "normal":
            if crape["salty"] == "egg":
                price += 5
                result += ("egg + ")
            if  crape["salty"] == "chili":
                price += 5
                result+=("chili + ")
            if  crape["salty"] == "flossyPork":
                price += 5
                result+=("flossyPork + ")
            if  crape["salty"] == "ham":
                price += 15
                result+=("ham + ")

            if crape["sweet"] == "foiThong":
                price += 10
                result+=("foiThong + ")
            if crape["sweet"] == "custard":
                price += 10
                result+=("custard + ")
            if crape["sweet"] == "choco":
                price += 10
                result+=("choco + ")
            if crape["sweet"] == "jelly":
                price += 10
                result+=("jelly + ")
            if crape["sweet"] == "nutella":
                price += 10
                result+=("nutella + ")
                
            if crape["topping"] == "banana":
                price += 10
                result+=("banana + ")
            if crape["topping"] == "cheese":
                price += 10
                result+=("cheese + ")
            if crape["topping"] == "tuna":
                price += 25
                result+=("tuna + ")
            if crape["topping"] == "crabStick":
                price += 20 
                result+=("crabStick + ")
            
            if crape["sauce"] == "chocolate":
                price += 5
                result+=("chocolate")
            if crape["sauce"] == "strawberry":
                price += 5
                result+=("strawberry")
            if crape["sauce"] == "caramel":
                price += 10
                result+=("caramel")
            return "แป้งธรรมดา " + str(price)+" บาท", result