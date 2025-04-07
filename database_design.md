# Database Design

This document outlines the conceptual database design for the Trainer and Subject Management Application, intended for persistent storage using a relational database (conceptually like SQLite).

## Entities and Tables

### 1. `trainers` Table

| Column     | Data Type         | Constraints          | Description                     |
|------------|-------------------|----------------------|---------------------------------|
| `trainer_id` | INTEGER           | PRIMARY KEY AUTOINCREMENT | Unique identifier for each trainer |
| `name`       | TEXT              | NOT NULL             | Full name of the trainer        |
| `expertise`  | TEXT              |                      | Comma-separated list of expertise |

### 2. `subjects` Table

| Column     | Data Type         | Constraints       | Description                     |
|------------|-------------------|-------------------|---------------------------------|
| `subject_id` | INTEGER           | PRIMARY KEY AUTOINCREMENT | Unique identifier for each subject |
| `name`       | TEXT              | NOT NULL UNIQUE   | Name of the subject             |

### 3. `trainer_subject` Table (Linking Table)

| Column     | Data Type         | Constraints                     | Description                                     |
|------------|-------------------|---------------------------------|-------------------------------------------------|
| `id`         | INTEGER           | PRIMARY KEY AUTOINCREMENT       | Unique identifier for the relationship          |
| `trainer_id` | INTEGER           | FOREIGN KEY referencing `trainers.trainer_id` | Foreign key linking to the `trainers` table |
| `subject_id` | INTEGER           | FOREIGN KEY referencing `subjects.subject_id` | Foreign key linking to the `subjects` table |
|            |                   | UNIQUE (`trainer_id`, `subject_id`) | Ensures a trainer-subject combination is unique |

## Relationships

The design implements a many-to-many relationship between `trainers` and `subjects` using the `trainer_subject` linking table. A trainer can be associated with multiple subjects, and a subject can be associated with multiple trainers.