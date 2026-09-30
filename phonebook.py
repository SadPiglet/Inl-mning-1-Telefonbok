def create_phonebook():
  phonebook = {
    "Hapi": "070-123 45 67",
    "Hana": "073-284 91 36",
    "Sam": "076-517 82 04",
    "Dean": "072-639 15 28",
    "Jo": "079-451 73 90",
    "John": "070-846 29 15",
    "Malin": "073-915 64 82",
  }
  return phonebook

def search_phone_number(phonebook, name):
  try:
    return phonebook[name]
  except KeyError:
    return "No contact matching that name was found."

def list_contacts(phonebook):
  for contact, number in phonebook.items():
    print(f"{contact}: {number}")

def add_contact(phonebook, name, number):

  if name == "":
    print("Name cannot be empty")
    return

  elif number == "":
    print("Number cannot be empty")
    return

  elif name in phonebook:
    print(f"{name} already exists.")
    answer = input("Do you want to update the phone number? (y/n):").lower()

    if answer == "y":
      phonebook[name] = number
      print("Contact was updated successfully!")

    else:
      print("Contact was not added.")

  else:
    phonebook[name] = number
    print("Contact added successfully!")
      

def update_number(phonebook, name, new_number):
  if name in phonebook:
    phonebook[name] = new_number
    print("Contact was updated successfully!")
  else:
    print("No contact matching that name was found.")

def remove_contact(phonebook, name):
  try:
    phonebook.pop(name)
    print("Contact was removed successfully!")
  except KeyError:
    print("No contact matching that name was found.")
