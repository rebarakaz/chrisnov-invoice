# Release Notes - v1.2.0 (Desktop & Backup Update)

We are excited to announce the release of **Chrisnov Invoice v1.2.0**! This update focuses on accessibility for non-technical users and data security.

## 🚀 What's New?

### 🖥️ Native Windows Support (Desktop App)
You no longer need to install Python or use the terminal to run Chrisnov Invoice! 
- We now provide a standalone **Windows Executable (.exe)**. 
- The application runs in its own dedicated window, providing a native desktop experience.
- Simply download, extract, and run `ChrisnovInvoice.exe`.

### 💾 Database Backup & Restore
Your data is precious. You can now easily manage your invoice database from the settings menu.
- **Export**: Download a complete backup of your database (`.db` file) at any time.
- **Restore**: Easily migrate your data to a new computer or recover from a previous state by uploading your backup file.
- Located in: `Settings` → `Manage Data`.

### 🇮🇩 Improved Translation System
- Standardized the localization system using `pybabel`.
- Fixed compatibility issues with Python 3.14 that previously caused "corrupt file" errors.
- Fully translated the new Backup & Restore interface into Bahasa Indonesia.

## 🛠️ Technical Improvements
- Added `run_desktop.py` for standalone mode.
- Added `build_exe.py` for automated building processes.
- Updated `.gitignore` to ensure essential documentation and translation sources are tracked.
- Optimized project structure for better "portable" use.

## 📦 How to use the Desktop Version
1. Download the `ChrisnovInvoice-Windows-v1.2.0.zip` from the Assets below.
2. Extract the ZIP file to a folder of your choice.
3. Double-click `ChrisnovInvoice.exe` to start the app.
4. *Note: As this is an open-source project, Windows may show a "SmartScreen" warning. Click "More Info" then "Run anyway".*

---
*Thank you for using Chrisnov Invoice! If you encounter any bugs, please open an issue on GitHub.*
