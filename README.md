# AcquaAltra
A digital map that identifies roads, crosswalks, etc. in Milan that are prone to flooding during heavy rainfall. 

Project Setup and Run Instructions

Prerequisites
1. Python 3.x
2. pip (Python package manager)
3. Virtualenv (optional, recommended)

Setup
1. Clone the Repository
    git clone <repository_url>
    cd <project_directory>

2. Create and Activate Virtual Environment (optional)
    python -m venv venv
        On Windows: venv\Scripts\activate
        On Mac/Linux: source venv/bin/activate

3. Install Dependencies
    pip install -r requirements.txt

4. Set Up Database
    python manage.py migrate


Running the Application
1. Start the Django development server:
    python manage.py runserver
    Access the app at http://127.0.0.1:8000/.
