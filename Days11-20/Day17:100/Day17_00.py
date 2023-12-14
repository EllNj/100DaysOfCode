class User:
    def __init__(self, id, username):     # called everytime we create a new object from this class
        # print("New user being created...")
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following += 1

# user_1 = User()
# user_1.id = "0001"
# user_1.username = "Ellis"
# ^ this can become this...
user_1 = User("0001", "Ellis")
user_2 = User("0002", "Mario")
print(user_1.username)
print(user_1.following)
print(user_2.followers)

# However now when creating an object we must include these class attributes
# we need a way for us to add some attributes later
# what we can do is not include it in the brackets and just add a default value (e.g. the followers attribute)
user_1.follow(user_2)   # running this method increases the followers for user_2 and increases the following for user_1
print(user_1.following)
print(user_2.followers)
