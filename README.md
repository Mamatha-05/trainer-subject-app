# Trainer and Subject Management Application

This application provides basic functionality for managing trainers and subjects within an educational institute.

## Features

* Add new trainers with their name and expertise.
* List all currently added trainers.
* Find the details of a trainer by their unique ID.
* Delete a trainer from the system using their ID.
* Find trainers who have expertise in a specific subject.
* Add new subjects by name.
* List all currently added subjects.
* Find a subject by its unique ID and see a list of trainers who teach that subject (based on their expertise).
* Basic navigation links to access all features.

## How to Run the Application

1.  Ensure you have Python and Flask installed on your system. You can install Flask using pip:
    ```bash
    pip install Flask
    ```
2.  Navigate to your project directory in the terminal:
    ```bash
    cd your_project_directory
    ```
3.  Run the Flask development server:
    ```bash
    python app.py
    ```
4.  Open your web browser and go to `http://127.0.0.1:5000`. Navigate using the links on the welcome page.

## Database Design

(See `database_design.md` for detailed information)

## Application Wire-frame

(See `wireframe.md` for a basic representation)

## Test Cases and Results

(See `test_cases.md` for details)

## GitHub Repository

The project is available in a public GitHub repository at: https://github.com/Mamatha-05/trainer-subject-app

## Known Issues/Limitations

* Currently, all data is stored in-memory.
* Basic frontend input validation only.
* No formal automated tests implemented.
* Basic error handling.

## Potential Future Enhancements

* Implement persistent data storage.
* Add user authentication and authorization.
* Improve UI/UX.
* Implement comprehensive server-side validation and automated testing.
