# Q 51: Email Address Validator
# Write a function is_valid_email(email) that accepts an email address as a string and checks if it follows a valid format 
# (contains "@" and "."). Return True if valid, otherwise False.
def is_valid_email(email):
    if "@" and "." not in email:
        return False
    else:
        return True
print(is_valid_email('mustved@gmai.com'))