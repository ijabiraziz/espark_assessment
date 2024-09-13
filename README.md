# Assessment
## Setup Instructions

### 1. Clone the Repository
- git clone repo_link
- cd repo_directory

### 2. Create and Activate Virtual Environment
#### Create a virtual environment
- python -m venv venv

- Activate the virtual environment
- For Linux/macOS:
- source venv/bin/activate
- For Windows: 
- venv\Scripts\activate

### 3. Install Dependencies
- pip install -r requirements.txt


### 4. Run the Development Server
- start the Django development server
- python manage.py runserver
- Now, visit http://127.0.0.1:8000/reward_review_admin/ in your browser and log in with the superuser credentials to access the admin panel.

### 4. Check Endpoint
- visit http://127.0.0.1:8000/api/upload/ on postman
- select body
- select form-data
- set key to "file" and value to intented upload file.
