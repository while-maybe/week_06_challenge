# 🏆 Python Challenge: Build a Simple To-Do List Application

## 🎯 Challenge

Your task is to develop a functional To-Do List application using Python. This application will allow users to manage their tasks efficiently through a command-line interface. Users will be able to add, view, update, and delete tasks, with the tasks being saved in a JSON file so that data persists even after the application is closed.

## 📚 Key Learnings

By completing this challenge, you will:
- Gain hands-on experience with Python programming by building a real-world application.
- Learn how to use data structures like lists and dictionaries for managing tasks.
- Work with JSON for saving and loading application data.
- Implement functions and error handling to ensure smooth user interaction.
- Gain familiarity with creating command-line interfaces in Python.

## 👤 User Story

As a user of the To-Do List application, I want to easily manage my tasks by adding, viewing, updating, and deleting them so that I can stay organized and keep track of my responsibilities.

## ✅ Acceptance Criteria

### Functionality:
1. **Add a Task**: Users can add a new task with a description and a status (e.g., pending, completed).
2. **View Tasks**: Users can view all existing tasks along with their statuses.
3. **Update a Task**: Users can update the description or status of a task.
4. **Delete a Task**: Users can delete a task from the list.
5. **Persistent Storage**: The application should save tasks to a JSON file when changes are made and load them when the application starts.

### Data Handling:
- Use a list to store tasks, where each task is a dictionary containing a description and a status.
- Load tasks from a JSON file when the application starts.
- Save tasks to the JSON file whenever they are added, updated, or deleted.

### Functions and Error Handling:
- Create functions for each operation (add, view, update, delete).
- Implement error handling to manage invalid user inputs (e.g., updating a task that doesn't exist).

## 🔄 Example Flow

1. **Step 1**: Set up your Python environment and create a JSON file to store the tasks (e.g., `tasks.json`).
2. **Step 2**: Implement the main program structure with a loop that displays a menu to the user.
3. **Step 3**: Create functions for adding, viewing, updating, and deleting tasks, ensuring each function handles the task appropriately.
4. **Step 4**: Incorporate error handling within your functions to manage potential exceptions (e.g., invalid task IDs).
5. **Step 5**: Test your application thoroughly, ensuring all functionalities work as intended.

## 🗂 Sample Task Structure

Each task in the JSON file should follow this structure:

```json
{
    "description": "Example Task",
    "status": "pending"
}