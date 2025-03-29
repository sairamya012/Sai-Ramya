def get_person_details():
  """
  function to read a persons details from the keyboard.
  """
  name=input("Enter your name:")
  address=input("Enter your address:")
  email=input("Enter your email;")
  phone=input("your phone number:")
  return name,address,email,phone
def print_person_details(name,address,email,phone):
  """
  function to print a persons details.
  """
  print("\n---personal Details---")
  print(f"name:{name}")
  print(f"address:{address}")
  print(f"Email:{email}")
  print(f"phone Number:{phone}")

#Get details from the user
name,address,email,phone=get_person_details()

#print the details
print_person_details(name,address,email,phone)
    
    
