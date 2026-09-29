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

phonebook = create_phonebook()

print(search_phone_number(phonebook, "Hapi"))
print(search_phone_number(phonebook, "Erik"))