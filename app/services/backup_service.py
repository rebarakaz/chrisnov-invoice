import os
import shutil
from datetime import datetime
from flask import current_app

class BackupService:
    @staticmethod
    def get_db_path():
        """Get the absolute path to the SQLite database file."""
        # Config says 'sqlite:///chrisnov_invoice.db'
        # Usually this means it's in the instance folder if using Flask-SQLAlchemy correctly
        return os.path.join(current_app.instance_path, 'chrisnov_invoice.db')

    @staticmethod
    def create_backup_copy():
        """Create a timestamped backup copy and return its path."""
        db_path = BackupService.get_db_path()
        if not os.path.exists(db_path):
            return None, "Database file not found."

        backup_dir = os.path.join(current_app.instance_path, 'backups')
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f"backup_{timestamp}.db"
        backup_path = os.path.join(backup_dir, backup_filename)

        try:
            shutil.copy2(db_path, backup_path)
            return backup_path, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def restore_from_file(uploaded_file_path):
        """Replace the current database with the uploaded file."""
        db_path = BackupService.get_db_path()
        
        try:
            # Create a safety backup of current state
            safety_backup = db_path + ".tmp"
            if os.path.exists(db_path):
                shutil.copy2(db_path, safety_backup)

            # Copy uploaded file to db path
            shutil.copy2(uploaded_file_path, db_path)
            
            # Remove safety backup if everything went well
            if os.path.exists(safety_backup):
                os.remove(safety_backup)
                
            return True, None
        except Exception as e:
            # Attempt to restore safety backup if it exists
            safety_backup = db_path + ".tmp"
            if os.path.exists(safety_backup):
                shutil.copy2(safety_backup, db_path)
                os.remove(safety_backup)
            return False, str(e)
