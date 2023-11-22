# Django Smart Note-Taking Application

## Overview
This Django Note-Taking application provides a simple yet effective way to create, manage, and summarize notes. Built using Django and Django REST Framework, and integrated with ChatGPT using LangChain, it offers a range of functionalities accessible via a RESTful API.

## Features
* CRUD Operations: Create, Read, Update, and Delete notes.
* Note Summarization: Utilize LangChain and OpenAI's GPT-3 model to generate summaries of notes.
* API Documentation: Swagger UI for easy visualization and interaction with the API's resources.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
    git clone https://github.com/TimNuga/note-taking-app.git
    cd note-taking-app

2. Set up a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
3. Install the requirements:
    pip install -r requirements.txt

4. Run migrations to create the database schema:
    python manage.py migrate

5. Start the development server:
    python manage.py runserver

## Usage
Once the server is running, you can access the API endpoints. For detailed endpoint documentation, visit [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

## Endpoints
* List/Create Notes: GET and POST requests to /notes/
* Retrieve/Update/Delete Note: GET, PUT, PATCH, and DELETE requests to /notes/{note_id}/
* Summarize Note: GET request to /notes/{note_id}/summarize/

## Technology Stack
* Framework: Django, Django REST Framework
* Database: SQLite (default Django database)
* Summarization: LangChain, OpenAI GPT-3
* API Documentation: Swagger (drf-yasg)

## Testing
To run tests, execute: python manage.py test

## Configuration

### Environment Variables
* OPENAI_API_KEY: API key for OpenAI GPT-3. Set this in a .env file in the root directory, you can copy it in the .env.example file and paste your genrated API key in the .env file.

## Contributing
Contributions to the project are welcome. Please follow the standard fork and pull request workflow.

## License
[MIT License](LICENSE).