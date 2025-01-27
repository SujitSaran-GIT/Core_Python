# A spam comment is defined as a text containing following keywords
# "Make a lot of money","Buy now","Subscribe this","Click This",

comment = ["Make a lot of money","Buy now","Subscribe this","Click This"]

message = input("Enter your comment:")
for i in range(len(comment)):
    if comment[i] in message:
        print("Spam Content")
        break