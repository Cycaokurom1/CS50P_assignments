import validators

address = input("What's your email address? ")
if validators.email(address) is True:
    print('Valid')
else:
    print('Invalid')