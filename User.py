class User:
    all_posts = []
    
    def __init__(self, first_name, last_name, user_id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id_number = user_id_number
        self.email = first_name + '.' + last_name + "@website.com"
        self.posts = []

    def user_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def profile_name(self):
        return f'{self.first_name}{self.last_name[0]}'

    def create_post(self, title, content):
        post = {'title': title, 'content': content}
        self.posts.append(post)
        User.all_posts.append(post)



user_1 = User('Darren', 'Berg', 12120)
user_2 = User('John', 'Evans', 12121)
user_3 = User('Tyler', 'McHaley', 12122)

user_1.create_post('I Love Dogs', 'I love dogs that are brown, energetic, and trained well.')
user_2.create_post('i love cats', 'i love cats')

create_post = User.all_posts.append('asdsaasdsadd')


print(user_1.posts)
print(user_2.posts)
print(User.all_posts)



# def create_a_post(self):
#         id=len(self.posts)+1
#         user_title=input("Please enter the title of your post:\n")
#         user_body=input("Please enter the content of your post:\n")
#         self.posts.append({"id":id,"title":user_title, "content":user_body})
#         self.User_posts.append({"id":id,"title":user_title, "content":user_body})