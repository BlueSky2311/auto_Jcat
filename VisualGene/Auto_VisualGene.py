from pywinauto.application import Application
import time

# Start the application
app = Application().start(r"C:\Users\Blue\Downloads\visual gene\VisualGeneDeveloper.exe")

# Wait for the program to load
time.sleep(10) # Adjust this value based on how long the program takes to load

# Select the menu item
app.VisualGeneDeveloper.menu_select("File -> Import gene list -> Fasta format")
