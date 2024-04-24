from pywinauto.application import Application
import time

# Start the application
app = Application().start(r"C:\Users\Blue\Downloads\visual gene\VisualGeneDeveloper.exe")

# Wait for the program to load
time.sleep(10) # Adjust this value based on how long the program takes to load

# Print the control identifiers
app.window(title='Visual Gene Developer 2.1  Build 797   [Untitled.vgd]').print_control_identifiers()

# Select the menu item
#app.VisualGeneDeveloper.menu_select("File -> Import gene list -> Fasta format")

# Close the application
#app.VisualGeneDeveloper.close()
