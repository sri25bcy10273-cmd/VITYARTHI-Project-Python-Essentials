# Python-Essentials-VITYARTHI-Project
 VITYARTHI Project 1: Fundamentals of Python A CRUD (Create, Read, Update, and Delete) system for pharmacy store stock is included in the attached Python file.
 An explanation of  The Illustration  Use at the Code's Bottom
 Instantiation  By doing this, a new PharmacyStock class object (instance) is created.  This initiates the __init__ method, which creates an empty dictionary (self.stock = {}) to store the data.
 Make (C):  This initiates the process of adding "Aspirin" at a cost of 5.99 and a quantity of 100.

 A success message string is returned, which is printed to the console.
 Read (R):  "Aspirin" is looked up using the stock dictionary.

 The dictionary {'quantity': 100, 'price': 5.99} is returned because it exists, and it is then printed.
 Update (U):  This changes the current "Aspirin"
entry.
 Observe that while quantity=150 is passed, the price is not.  The method maintains the price at 5.99 while updating the quantity to 150.  The success message is printed.
 Remove (D):  This completely eliminates the dictionary's "Aspirin" key and all of its related information.  A confirmation message is returned (and printed).

 Code Lines 1 through 26  Class explanation  Pharmacy Stock:  This establishes your system's blueprint.
 __init__:  The builder is this person.  When you create a new instance (as on line 28), it executes automatically.
 self.stock = {}:  An empty Python dictionary is initialized as a result.  Consider this as a blank ledger or an empty shelf where all of the medication data will be kept.
 The Check  It first determines whether the name is in self.stock.  You don't want to inadvertently replace data that already exists.
The Action: A nested dictionary is created if the name is new.  "Aspirin": {'price': 5.99, 'quantity': 100}.
 The Return: A text message verifying the action is sent back.
 The Check: It confirms the existence of the medication.  If not, an error message is returned.
 The Action: It returns the dictionary with the quantity and cost of that medication if it is located.
 The Flexibility: Take note of the definition's quantity=None and price=None.  These arguments are therefore optional.
 The reasoning is that the quantity is updated if you supply a different amount.
 It updates the price if you provide a new one.
 If you provide both, it updates both.
 This allows you to change the price without accidentally deleting the quantity count.
Action: The del keyword permanently deletes the key (the name of the medicine) and its value (the information) from the dictionary.
Summary of Operations 
Function	Action	Dictionary Operation Used
create_medicine	Add new item	dict[key] = value
read_medicine	Get item details	dict[key]
update_medicine	Change details	dict[key]['sub_key'] = new_value
delete_medicine	Remove item	del dict[key]
