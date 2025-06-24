# Gov_security

In this paper, we consider the development of a web application for government employees in order to provide convenient access to information and interaction between department employees.

**Problem**: the lack of a user-friendly web application for secure and unified communication of government employees. Existing analogues for user communication are often limited in their functions and do not allow the user to have all the necessary tools in one project.

## Application Architecture

The application is built in the Python programming language using the Django web development framework.

## Project structure

The project defines various models, each of which represents a specific entity in the context of the application. A more detailed review of each model:

1. **ResourceType:**
    - The model represents the type of resource;
    - Fields:
        - *resource_type*: A string field that stores the name of the resource type; 
        - *resource_file*: A file that is attached to a specific resource.
2. **Resource:**
    - The model describes a specific resource that can be linked to a specific type of resource via a foreign key;
    - Fields:
        - *resource_name*: A string field up to 50 characters long, the name of the resource; 
        - *resource_type*: A foreign key (ForeignKey) for the ResourceType model, indicating the type of this resource.
3. **Position:**
    - The model is responsible for a position within the organization, for example, "Private", "Major", etc.;
    - Fields:
        - *position_name*: A string field up to 20 characters long, stores the title of the position.
4. **Permission:**
    - The model for managing access permissions to resources for different positions;
    - Fields:
        - *resource*: A foreign key for the Resource model; 
        - *position*: A foreign key for the Position model.
5. **Department:**
    - The model describes the departments of the organization;
    - Fields:
        - *department_name*: String field, department name; 
        - *dep_description*: A textfield containing a description of the department; 
        - *emp_num*: Integer field (IntegerField), the number of employees in the department.
6. **Head:**
    - A model of a manager who belongs to a specific department and holds a specific position;
    - Fields:
        - *head_name*: String field, the name of the supervisor; 
        - *department*: A foreign key for the Department model; 
        - *position*: A foreign key for the Position model.
7. **Employee** (inherits from AbstractUser):
    - The employee model, extends the standard Django user model.
    - Fields:
        - *patronymic*: String field for patronymic, optional; 
        - *age*: An integer field for age, optional; 
        - *phone*: A string field for the phone, unique, optional; 
        - *position*: A foreign key for the Position model; 
        - *department*: A foreign key for the Department model.
8. **Task:**
    - The model of the task that the employee must complete;
    - Fields:
        - *task_name*: Task name; 
        - *task_description*: Description of the task; 
        - *head*: A foreign key for the Head model.
9. **TaskList:**
    - The model for tracking tasks assigned to employees;
    - Fields:
        - *task*: A foreign key for the Task model; 
        - *employee*: A foreign key for the Employee model.
10. **Message:**
    - The model of messages related to specific departments.
    - Fields:
        - *department*: A foreign key for the Department model; 
        - *author*: A foreign key for the user model (User); 
        - *message_text*: Message text; 
        - *timestamp*: Date and time when the message was created.

![ER-diagramm](./gov_security/gov_security/media/ER-diagramm.png)

## Security features

The project uses a secure way to manage user accounts and passwords, avoiding common mistakes such as placing session information in cookies where it is vulnerable (instead, cookies contain only the key, and the actual data is stored in a database) or storing passwords directly instead of a password hash.

It provides protection against many vulnerabilities, including SQL injection. 

Password hashing is used. By default, PBKDF2 with a SHA256 hash is used, a password-based key generation algorithm that can significantly slow down brute force attacks. Passwords are stored not in their original form, but as a hash, which makes them useless outside the context of the application.

The project includes CSRF (Cross-Site Request Forgery) tokens to protect against attacks in which an attacker can force a user to perform unwanted actions on the site.

## Interface

After logging in to the site, an authentication page is displayed.

![auth](./gov_security/gov_security/media/auth.png)

After entering the correct username and password, the main page of the web application will open. If an incorrect input is attempted, an error message is displayed.

![main](./gov_security/gov_security/media/main.png)

On the main page there is a chat for users of the department to which the user belongs. The navigation bar contains the buttons "Chat", "Tasks", "Profile", "Resources". There are also functions for sending a message to the chat and logging out of the account. Clicking on the "Tasks" button opens the tasks page.

![tasks](./gov_security/gov_security/media/tasks.png)

The page shows a window that displays all the tasks with their descriptions that have been assigned to the user. Clicking on the "Profile" button opens the user's profile page.

![profile](./gov_security/gov_security/media/profile.png)

Clicking on the link in the Department field opens the page of the department to which the user belongs.

![department](./gov_security/gov_security/media/department.png)

Clicking on the "Resources" button opens a resource page with the name and type of resource that are available to the user according to his position. By clicking on the "Download" link, the required file will be installed on the device.

![resources](./gov_security/gov_security/media/resources.png)

Clicking on the "Log out" button will log out of the account and the authentication page will be displayed. 

The entire interface is designed in the same style. Also, the entire visual part is dynamic and changes according to the size of the window itself.

## Launch

1. Install the repository:

```
git clone git@github.com:fratellou/Gov_security.git
```

2. Go to the project directory:

```
cd Gov_security/gov_security/
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create environment variables in the .env file (an example of environment variables is provided in the `.env.example` file).

5. Apply migrations:
```
python3 manage.py migrate
```

6. Start the server:

```
python3 manage.py runserver
```

7. Create a superuser:

```
python3 manage.py createsuperuser
```
8. Go to *http://127.0.0.1:8000/admin* and create the necessary data

---
> fratellou, 2024