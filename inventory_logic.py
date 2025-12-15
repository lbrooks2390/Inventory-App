import csv
from PyQt6.QtWidgets import QWidget

inventory: list[list] = []

def write_csv()->None:
    """Write current inventory to inventory.csv"""
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for item in inventory:
            writer.writerow(item)

def add_item(mod_var: QWidget) -> bool:
    """Add an item to the inventory or update quantitiy"""
    name = mod_var.ui.lineEdit_2.text().strip().lower()
    number_text = mod_var.ui.lineEdit.text().strip()

    if not name or not number_text:
        mod_var.ui.textBrowser.append("Error: empty fields")
        return False
    try:
        number = int(number_text)
    except:
        mod_var.ui.textBrowser.append("Error: quantity must be a number")
        return False

    for entry in inventory:
        if entry[0] == name:
            entry[1] += number
            mod_var.ui.textBrowser.append(f"Updated: {name.title()} {entry[1]}")
            write_csv()
            mod_var.ui.lineEdit.clear()
            mod_var.ui.lineEdit_2.clear()
            return True

    inventory.append([name, number])
    mod_var.ui.textBrowser.append(f"Added: {name.title()} {number}")
    write_csv()
    mod_var.ui.lineEdit.clear()
    mod_var.ui.lineEdit_2.clear()
    return True

def remove_item(mod_var: QWidget) -> bool:
    """Remove a quantity of item from inventory"""
    name = mod_var.ui.lineEdit_2.text().strip().lower()
    number_text = mod_var.ui.lineEdit.text().strip()

    if not name or not number_text:
        mod_var.ui.textBrowser.append("Error: empty fields")
        return False
    try:
        number = int(number_text)
    except:
        mod_var.ui.textBrowser.append("Error: quantity must be a number")
        return False

    for entry in inventory:
        if entry[0] == name:
            if entry[1] < number:
                mod_var.ui.textBrowser.append("Error: not enough items to remove")
                return False
            entry[1] -= number
            mod_var.ui.textBrowser.append(f"Removed: {name.title()} {number}")
            if entry[1] == 0:
                inventory.remove(entry)
                mod_var.ui.textBrowser.append(f"{name.title()} removed completely")
            write_csv()
            mod_var.ui.lineEdit.clear()
            mod_var.ui.lineEdit_2.clear()
            return True

    mod_var.ui.textBrowser.append("Error: item not found")
    return False

def delete_inventory(mod_var: QWidget) -> bool:
    """Clear the whole inventory"""
    if not inventory:
        mod_var.ui.textBrowser.append("Inventory is already empty")
        return False
    inventory.clear()
    mod_var.ui.textBrowser.append("Inventory cleared")
    write_csv()
    return True
