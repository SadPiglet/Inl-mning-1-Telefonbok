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
    return "No matches found."

def list_contacts(phonebook):
  for contact, number in phonebook.items():
    print(f"{contact}: {number}")

def add_contact(phonebook, name, number):
  phonebook[name] = number

def update_number(phonebook, name, new_number):
  if name in phonebook:
    phonebook[name] = new_number
  else:
    return "No matches found."

phonebook = create_phonebook()


print(update_number(phonebook, "Anders", "80085"))