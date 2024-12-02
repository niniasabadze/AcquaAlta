# AcquaAlta
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

2. Sign Up and Log In
    You can sign up with your own new account or use the one already created for testing purposes, with the following credentials:
    Username: jane_doe
    Password: TestUser@1

Important Note on Load Time:

Please note that when the web page is loaded, it may take approximately 8 seconds for the page to fully load. This is due to the fact that the web app fetches a significant amount of data from external APIs, including weather and geographical information.

We are aware of this delay, and we are actively working to optimize the app's performance. This issue will be addressed in future updates to reduce the load time and improve the overall user experience.

We appreciate your understanding and encourage you to bear with the slight delay during the initial load.
