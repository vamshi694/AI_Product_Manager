def change_role(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
         
def emoji(user_role):
    if user_role == "model":
        return "👨🏻‍💻"
    else: 
        return "👤"