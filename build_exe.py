import PyInstaller.__main__
import os
import shutil

def build():
    # Application name
    app_name = "ChrisnovInvoice"
    
    # Path to the main script
    script_path = "run_desktop.py"
    
    # Folders to include (format: 'source_path;destination_path')
    # On Windows, use semicolon ; as separator
    add_data = [
        ("app/templates;app/templates"),
        ("app/static;app/static"),
        ("app/translations;app/translations"),
    ]
    
    # PyInstaller arguments
    args = [
        script_path,
        "--name=" + app_name,
        "--onefile", # Bundle everything into a single .exe
        "--windowed", # Don't show the command prompt window
        "--clean",
    ]
    
    for item in add_data:
        args.append(f"--add-data={item}")
    
    # Optional: Add an icon if you have one (.ico)
    # if os.path.exists("icon.ico"):
    #     args.append("--icon=icon.ico")

    print(f"Building {app_name} desktop application...")
    PyInstaller.__main__.run(args)
    
    print("\nBuild complete! You can find the executable in the 'dist' folder.")

if __name__ == "__main__":
    build()
