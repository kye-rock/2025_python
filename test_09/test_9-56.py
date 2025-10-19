class User:
    def __init__(self, name):
        self.name = name
    
def update_username(user, new_name):
    user.name = new_name
    
user = User("Kim")
print("Before: ", user.name)

update_username(user, "Lee")
print("After: ", user.name)