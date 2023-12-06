import os
import shutil
from tkinter import Tk, Button, Label, Frame, PhotoImage

def organize_files():
    # Set the default source folder to the Downloads folder
    source_path = os.path.expanduser('~/Downloads')
    file_list = os.listdir(source_path)

    # Set the destination paths
    documents_path = os.path.expanduser('~/iCloud Drive/Documents')
    

    # Create a dictionary to map file types to their respective destination folders
    folders = {
        "Documents": {
            "Text Files": [".doc", ".docx", ".csv", ".txt", ".RTF"],
            "PDFs": [".pdf"],
            "Spreadsheets": [".xlsx", ".xls"],
            "PowerPoint Presentations": [".ppt", ".pptx"],
            "Compressed Files": [".zip", ".rar"],
            "Images": [".png", ".jpg", ".jpeg"],
            "Audio": [".m4a", ".mp3", ".wav"],
            "Videos": [".mp4", ".avi", ".mov"],
            "GIFs": [".gif"],
            "Icons": [".ico", ".icns"],
            "Links": [".html", ".htm"]
        }
    }

    # Organize files
    for file in file_list:
        # Split the file name and extension
        filename, file_extension = os.path.splitext(file)

        # Iterate through the dictionary to find the destination folder
        for category, extensions in folders["Documents"].items():
            if file_extension in extensions:
                # Create the destination folder if it doesn't exist
                destination_folder = os.path.join(documents_path, category)
                os.makedirs(destination_folder, exist_ok=True)

                # Move the file to the destination folder
                source_file_path = os.path.join(source_path, file)
                destination_file_path = os.path.join(destination_folder, file)
                shutil.move(source_file_path, destination_file_path)

    # Update the label text after organizing files
    label.config(text="Successfully sorted!")

# Create the main window
root = Tk()
root.title("File Organizer")

# Set the window size
window_height = 400
window_width = 700

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position of the window to center it on the screen
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a dictionary to map folder names to their respective icons
folder_icons = {
    
    "Text Files": "FileOrganizer/assets/txt.png",
    "PDFs": "FileOrganizer/assets/pdf.png",
    "Spreadsheets": "FileOrganizer/assets/xls.png",
    "PowerPoint Presentations": "FileOrganizer/assets/ppt.png",
    "Compressed Files": "FileOrganizer/assets/zip.png",
    "Images": "FileOrganizer/assets/img.png",
    "Audio": "FileOrganizer/assets/audio.png" ,
    "Videos": "FileOrganizer/assets/video.png",
    "GIFs": "FileOrganizer/assets/gif.png",
    "Icons": "FileOrganizer/assets/ico.png",
    "Links": "FileOrganizer/assets/link.png",
}

# Create a dictionary to map file types to their respective destination folders
folders = {
    "Documents": {
        "Text Files": [".doc", ".docx", ".csv", ".txt", ".RTF"],
        "PDFs": [".pdf"],
        "Spreadsheets": [".xlsx", ".xls"],
        "PowerPoint Presentations": [".ppt", ".pptx"],
        "Compressed Files": [".zip", ".rar"],
        "Images": [".png", ".jpg", ".jpeg"],
        "Audio": [".m4a", ".mp3", ".wav"],
        "Videos": [".mp4", ".avi", ".mov"],
        "GIFs": [".gif"],
        "Icons": [".ico", ".icns"],
        "Links": [".html", ".htm"],
    }
}

# Create and pack GUI components
frame = Frame(root, padx=20, pady=20)
frame.pack(pady=20)

# Load the image
image_path = "FileOrganizer/assets/FileOrganizer.png"
img = PhotoImage(file=image_path)

# Resize the image to fit the window
# Adjust the subsample factors based on your requirements
img = img.subsample(3, 3)

# Create a label to display the image
image_label = Label(frame, image=img)
image_label.pack(pady=5)

label = Label(root, text="")
label.pack(pady=5)

# Create a button to trigger file organization
organize_button = Button(root, text="Sort Files", command=organize_files)
organize_button.pack(pady=5)

# Update the labels with custom icons
for category, extensions in folders["Documents"].items():
    icon_path = folder_icons.get(category, "/path/to/default_icon.png")  # Use a default icon if not specified
    icon = PhotoImage(file=icon_path)
    icon = icon.subsample(3, 3)
    
    # Create a label with the icon and text
    folder_label = Label(root, text=category, compound="left", image=icon)
    folder_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
