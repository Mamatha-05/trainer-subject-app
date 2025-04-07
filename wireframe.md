# Application Wire-frame (Basic Text Representation)

This provides a basic text-based representation of the application's user interface flow.

## 1. Welcome Page (`/`)

* Heading: Welcome to the Trainer and Subject Management App
* Navigation Links:
    * [Add Trainer](/add_trainer)
    * [List Trainers](/list_trainers)
    * [Find Trainer by ID](/get_trainer_form)
    * [Delete Trainer by ID](/delete_trainer_form)
    * [Find Trainers by Subject](/find_trainers_by_subject_form)
    * [Add Subject](/add_subject)
    * [List Subjects](/list_subjects)
    * [Find Subject by ID](/get_subject_form)

## 2. Add Trainer Page (`/add_trainer`)

* Heading: Add New Trainer
* Form:
    * Label: Name
    * Input: Text field (`id="name"`)
    * Label: Expertise (comma-separated)
    * Input: Text field (`id="expertise"`)
    * Button: Add Trainer (Submit)
* Message Area (`id="message-area"`) for success/error messages.
* Link: [View All Trainers](/list_trainers)

## 3. List Trainers Page (`/list_trainers`)

* Heading: All Trainers
* (Placeholder for Trainer List - e.g., a table would go here showing ID, Name, Expertise)
* Link: [Add New Trainer](/add_trainer)

## 4. Find Trainer by ID Page (`/get_trainer_form`)

* Heading: Find Trainer by ID
* Form:
    * Label: Trainer ID
    * Input: Text field (`id="trainer_id"`)
    * Button: Find Trainer
* Display Area for Trainer Details or "Not Found" message.

## 5. Delete Trainer by ID Page (`/delete_trainer_form`)

* Heading: Delete Trainer by ID
* Form:
    * Label: Trainer ID
    * Input: Text field (`id="trainer_id"`)
    * Button: Delete Trainer
* Message Area for success/error messages.
* Link: [View All Trainers](/list_trainers)

## 6. Find Trainers by Subject Page (`/find_trainers_by_subject_form`)

* Heading: Find Trainers by Subject
* Form:
    * Label: Subject Name
    * Input: Text field (`id="subject_name"`)
    * Button: Find Trainers
* Display Area for list of matching trainers.

## 7. Add Subject Page (`/add_subject`)

* Heading: Add New Subject
* Form:
    * Label: Subject Name
    * Input: Text field (`id="name"`)
    * Button: Add Subject
* Message Area (`id="message-area"`) for success/error messages.
* Link: [View All Subjects](/list_subjects)

## 8. List Subjects Page (`/list_subjects`)

* Heading: All Subjects
* (Placeholder for Subject List - e.g., a table would go here showing ID, Name)
* Link: [Add New Subject](/add_subject)

## 9. Find Subject by ID Page (`/get_subject_form`)

* Heading: Find Subject by ID
* Form:
    * Label: Subject ID
    * Input: Text field (`id="subject_id"`)
    * Button: Find Subject
* Display Area for Subject Details and list of teaching trainers.