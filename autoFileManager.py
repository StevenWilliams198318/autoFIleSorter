import os
import shutil

root_directory = os.path.join(os.path.expanduser("~"), "Videos")

extensions = {
    ".lnk": "Shortcuts",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".jfif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mpg": "Videos",
    ".mpeg": "Videos",
    ".flv": "Videos",
    ".gifv": "Videos",
    ".webm": "Videos",
    ".docx": "WordDocs",
    ".doc": "WordDocs",
    ".pdf": "PdfDocs",
    "epub": "PdfDocs",
    ".odt": "WordDocs",
    ".txt": "WordDocs",
    ".csv": "ExcelDocs",
    ".xlsx": "ExcelDocs",
    ".xls": "ExcelDocs",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".7z": "Compressed",
    ".iso": "Compressed",
    ".exe": "Compressed",
    ".msi": "Compressed",
    ".msix": "Compressed",
    ".cab": "Compressed",
    ".dmg": "Compressed",
    ".pkg": "Compressed",
    ".chm": "Compressed",
    ".appinstaller": "Compressed",
    ".torrent": "TorrentFiles",
    ".mp3": "Music",
    ".wav": "Music",
    ".ogg": "Music",
    ".aac": "Music",
    ".flac": "Music",
    ".wma": "Music",
    ".m4a": "Music",
    ".opus": "Music",
    ".ape": "Music",
}

for root, dirs, files in os.walk(root_directory):
    for filename in files:
        file_path = os.path.join(root, filename)

        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]

            #Check the if folder already exists
            existing_foler_path = None
            for dir in dirs:
                if dir.lower() == folder_name.lower():
                    existing_folder_path = os.path.join(root, dir)
                    break

            
            if existing_folder_path:
                #Moving files into pre-existing folder
                destination_path = os.path.join(existing_folder_path, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to existing {folder_name} folder.")
            else:
            #Creating a new folder and moving files into it
                folder_path = os.path.join(root, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to new {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
print(f"File Organization completed! New Folders are {folder_name}, {folder_name}, {folder_name}, and {folder_name}")

""" 
            folder_path = os.path.join(root, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        print(f"Skipped {filename}. No permissions to access restricted directory.")

print("File organization completed!")
"""
