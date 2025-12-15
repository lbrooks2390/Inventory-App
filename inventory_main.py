"""
Sources:
For how to on QTextBrowser: https://www.tutorialspoint.com/pyqt/pyqt_qtextbrowser.htm
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from inventory_gui import Ui_Inventory
import inventory_logic as logic

class InventoryApp(QWidget):
    def __init__(mod_var)-> None:
        """Activate the Inventory GUI and connect buttons"""
        QWidget.__init__(mod_var)

        mod_var.ui = Ui_Inventory()
        mod_var.ui.setupUi(mod_var)
        mod_var.setWindowTitle("Inventory")

        mod_var.ui.pushButton_3.clicked.connect(mod_var.add_item)
        mod_var.ui.pushButton_4.clicked.connect(mod_var.remove_item)
        mod_var.ui.pushButton.clicked.connect(mod_var.view_inventory)
        mod_var.ui.pushButton_2.clicked.connect(mod_var.delete_inventory)

    def add_item(mod_var) -> None:
        """Handle adding items, validate input, then update"""
        if logic.add_item(mod_var):
            mod_var.view_inventory()

    def remove_item(mod_var) -> None:
        """Handle removing items, validate input, then update"""
        if logic.remove_item(mod_var):
            mod_var.view_inventory()

    def delete_inventory(mod_var) -> None:
        """Handle delete inventory button and clear inventory"""
        if logic.delete_inventory(mod_var):
            mod_var.view_inventory()

    def view_inventory(mod_var) -> None:
        """Dispaly current inventory in the text browser"""
        mod_var.ui.textBrowser.clear()
        if not logic.inventory:
            mod_var.ui.textBrowser.append("Inventory empty")
            return
        mod_var.ui.textBrowser.append("Inventory:")
        for entry in logic.inventory:
            mod_var.ui.textBrowser.append(f"{entry[0].title()}: {entry[1]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    window.view_inventory()
    sys.exit(app.exec())
