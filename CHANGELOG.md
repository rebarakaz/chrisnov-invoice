# Changelog

## [1.2.0] - 2026-01-06
### Added
- **Backup & Restore**: New settings section to export and import database backups (.db files).
- **Desktop Mode Support**: Added `run_desktop.py` using `flaskwebgui` for a native app feel.
- **Standalone Build Script**: Added `build_exe.py` to easily bundle the app into a Windows executable.
- New dependencies: `flaskwebgui`, `pyinstaller`.

### Fixed
- **Translation System**: Standardized translation compilation using official `pybabel`.
- **Git Visibility**: Fixed `.gitignore` to allow tracking of essential translation and documentation files.
- **Corrupt MO Files**: Resolved issue where manual binary generation caused compatibility errors in Python 3.14.

All notable changes to this project will be documented in this file.

## [1.1.0] - 2025-12-30 "Elegant & Global Update"

### Added
- **Internationalization (i18n)**: 
  - Added full support for Bahasa Indonesia.
  - Implemented persistent language switching (stores preference in session).
  - Added language switcher dropdown to the top navigation bar.
- **App Branding**:
  - Implemented Logo display in the App Sidebar (Dashboard).
  - Logo persistence: Uploaded logos are now correctly saved to the database.
- **Elegant PDF Template**:
  - Redesigned "Elegant" template to a classic, serif-based layout.
  - Added centered logo support to the "Elegant" template.

### Improved
- **Settings UI**:
  - Refined PDF Template previews in Settings to accurately reflect "Modern", "Classic/Elegant", and "Professional" layouts.
  - Added "Details" section preview for the Elegant template.
  - Sidebar header spacing: Added padding to "Chrisnov IT Solutions" label to improve readability.
- **Developer Experience**:
  - Moved `translations` directory to standard `app/translations` location for better compatibility.

### Fixed
- **Language Switcher**: Fixed issue where the app would revert to English due to missing session persistence or incorrect translation directory.
- **Logo Display**: Fixed 404 errors for logo images by standardizing file storage to `logo.png`.
- **PDF Generation**: Fixed various layout overlaps in "Modern" and "Professional" templates.
