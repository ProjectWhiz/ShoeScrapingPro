# Make a class that will allow you to create certain inputs based on user needs

class ShoeInput:
    def __init__(self):
        self.user = None
        self.brand = None
        self.price = None
        self.size = None

    def input_type(self):
        while True:
            self.user = int(input("How do you want to query?\n1:brand\n2.price?\nAnswer: "))
            if self.user == 1:
                self.brand_check()
                break
                
            elif self.user == 2:
                print("You selected price")
                self.price_check()
                break
            else:
                print("Invalid input, please try again.\n")
                continue    
            
    def brand_check(self):
        brand_type = []
        self.brand = input("What brand do you want to search for?\nAnswer: ")
        brand_type.append(self.brand)
        print(brand_type)
        
    def price_check(self):
        price = []
        self.price = float(input("What is your current budget?\nAnswer:$ "))
        price.append(self.price)
        print(price)
        




def main():
    shoe_input = ShoeInput()
    shoe_input.input_type()




if __name__ == "__main__":
    main()
















