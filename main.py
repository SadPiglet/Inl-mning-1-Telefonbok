import phonebook as pb

phonebook = pb.create_phonebook()

def main_menu():
  print("Welcome to the phonebook!")
  print("1. Show all contacts")
  print("2. Search for a phone number")
  print("3. Add a new contact")
  print("4. Update a phone number")
  print("5. Remove contact")
  print("6. Exit")


while True:
  main_menu()
  choice = input("Choose an option: ")

  if choice == "1":
    pb.list_contacts(phonebook)
    input("Press enter to return to the menu...")

  elif choice == "2":
    name = input("Enter a name: ")
    print(pb.search_phone_number(phonebook, name))
    input("Press enter to return to the menu...")

  elif choice == "3":
    name = input("Enter a name for your new contact: ")
    number = input("Enter a number for your new contact: ")

    pb.add_contact(phonebook, name, number)
    input("Press enter to return to the menu...")

  elif choice == "4":
    name = input("Enter a name: ")
    new_number = input("Enter the updated number: ")

    pb.update_number(phonebook, name, new_number)
    input("Press enter to return to the menu...")

  elif choice == "5":
    name = input("Enter name of contact to remove: ")

    pb.remove_contact(phonebook, name)
    input("Press enter to return to the menu...")

  elif choice == "6":
    break