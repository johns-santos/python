class User:
    
    def __init__(self,  user_name, user_id):
        self.name = user_name
        self.id = user_id
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('john', '0003')
user_2 = User('Monica', '004')

user_1.follow(user_2)

print(user_1.followers)
print(f"{user_1.name} is following {user_1.following} users")

print(user_2.followers)
print(f"{user_2.name} is following {user_2.following} users")
