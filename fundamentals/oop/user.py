class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points, sep='\n')
        return self

    def enroll(self):
        if self.is_rewards_member !=True:
            self.is_rewards_member=True
            self.gold_card_points=200
        else:
            print("Already a rewards member!")
        print(self.is_rewards_member, self.gold_card_points)
        return self

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points=self.gold_card_points-amount
        else:
            print("Not enough points")
        print(self.gold_card_points)
        return self

user_1= User("John", "Smith", "email@noemail.com", 32)
user_1.display_info().enroll().spend_points(50).display_info()



user_2 =User("James", "Madison", "email@noemail.com", 54)
user_3 =User("Cheeseburger", "Jones", "email@noemail.com", 65)



user_2.enroll().spend_points(80).display_info()





user_3.spend_points(50)




