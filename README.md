# Report Card 

This README provides an overview of the Student Management System Report Card project, which is developed using Python, MySQL connectivity, and Tkinter for the frontend. The project aims to create a user-friendly application for managing student details and generating report cards.

## Table of Contents
 

- [Project Overview](#project-overview)
- [Features](#features)
- [Insert Students' Personal Details](#insert-students-personal-details)   
- [Insert Students' Exam Marks](#insert-students-exam-marks)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Configuration](#configuration) 
- [Prerequisites](#prerequisites)      
- [Installation](#installation)
- [Usage](#usage)
  
## Project Overview

The Student Management System Report Card project is designed to efficiently manage student information and generate report cards for educational institutions. The project utilizes Python programming for the backend logic, MySQL for database storage, and Tkinter for the graphical user interface.

## Features

- Add, update, and delete student records.
- Store student details such as name, roll number, marks, and other relevant information.
- Calculate total marks, average, and generate report cards based on student performance.
- User-friendly interface using Tkinter.
- MySQL database connectivity for seamless data storage and retrieval.
This project is a Student Report Card Management System built using Python's Tkinter library for the graphical user interface (GUI) and MySQL for database management. This system provides a convenient way to manage student information and examination marks efficiently. It offers two main functionalities:

## Insert Students' Personal Details

This feature allows users to input personal details of students, including:
- Admission number
- Exam number
- Name
- Class
- Date of birth
- Gender
- Parents' names
- School information
- Contact details

The details are then stored in a MySQL database.

## Insert Students' Exam Marks

Users can input students' exam marks for various subjects and practicals, including:
- English
- Mathematics
- Physics
- Chemistry
- Biology
- Computer Science

Additionally, practical marks for each subject can be entered. The marks are stored in the MySQL database.

## Getting Started

1. **Database Setup**: Ensure you have MySQL installed and running. Modify the database connection details in the code to match your MySQL configuration. The application will create a new database named `report_card` with necessary tables on first run.

2. **Inserting Personal Details**: Launch the application and click on "Insert Students' Personal Details." Enter the required details and click "SAVE" to store them in the database.

3. **Inserting Exam Marks**: Similarly, click on "Insert Students' Exam Marks." Enter admission number, exam number, student name, and subject/practical marks. Click "SAVE" to store the marks in the database.

4. **Quitting the Application**: Use the "QUIT" button in the respective windows to exit.

## Dependencies

- Python 3.x
- Tkinter library (usually pre-installed with Python)
- MySQL database

## Configuration

Modify the database connection parameters in the code to match your MySQL configuration:

```python
mycon = mysqltor.connect(host='localhost', user='root', password='your_password_here')
```
## Prerequisites

Before running the project, make sure you have the following components installed:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- MySQL: [Download MySQL](https://dev.mysql.com/downloads/)


## Installation

To use the Student Report Card Management System, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/your-username/student-report-card.git`.

2. Install the required dependencies using the following command:
   ```bash
   pip install mysql-connector-python
   ```

## Usage
Run the application by executing the main Python script:
```
python main.py
```
The application's GUI will open, providing options to insert students' personal details and exam marks.

To insert/update student records, fill in the required details in the provided fields and click the "SAVE" button.

To edit existing student records, click the "Edit" button and follow the prompts.
