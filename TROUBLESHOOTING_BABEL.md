# Troubleshooting Flask-Babel Installation

## Issue

If you get `ModuleNotFoundError: No module named 'flask_babel'` when running `python run.py`, it means Flask-Babel isn't installed in your current Python environment.

## Solution 1: Install in Virtual Environment

If you're using a virtual environment, make sure to install Flask-Babel:

```bash
# Activate your virtual environment (if not already active)
# On Windows:
venv\Scripts\activate

# Install Flask-Babel
pip install Flask-Babel
```

## Solution 2: Install Globally

If not using virtual environment:

```bash
pip install Flask-Babel
```

## Solution 3: Use Python from Virtual Environment

Make sure you're running Python from the virtual environment:

```bash
# Activate virtual environment first
venv\Scripts\activate

# Then run the app
python run.py
```

## Solution 4: Check Python Environment

Verify which Python you're using:

```bash
# Check Python path
where python

# Check if Flask-Babel is available
python -c "from flask_babel import Babel; print('Flask-Babel is available')"
```

## Solution 5: Install All Requirements

Make sure all requirements are installed:

```bash
pip install -r requirements.txt
```

## Quick Fix Command

If you want to install everything at once:

```bash
pip install Flask==3.0.0 Flask-SQLAlchemy==3.1.1 Flask-Mail==0.9.1 Flask-Babel==4.0.0 reportlab==4.0.7 python-dateutil==2.8.2 Flask-Migrate==4.0.8
```

## After Installation

Once Flask-Babel is properly installed, your app should run with:

```bash
python run.py
```

Then visit <http://127.0.0.1:5000> and use the language selector in the top-right corner to switch between English and Indonesian!
