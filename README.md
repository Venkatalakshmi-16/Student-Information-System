**Student Information System**
 **Overview**

This project is a web-based Student Information System developed using Django. It is designed to manage student details and their academic performance in an organized and secure manner. The system allows users to store, update, and analyze student records efficiently.

 **Authentication**

The application includes a login and logout system using Django’s built-in authentication. Only authenticated users can access the dashboard and other pages. This ensures that student data is protected and secure.

**Dashboard**

After login, users can view a dashboard that displays the total number of students and total marks entries. This provides a quick summary of the system data.

**Student Management**

The system supports full CRUD operations for students. Users can add new students, view the list of students, edit existing details, and delete records when needed. A search feature is implemented to easily find students by name. Pagination is also added to manage large numbers of student records efficiently.

 **Marks Management**

Users can add subject-wise marks for each student. The system prevents duplicate subject entries for the same student using database constraints. This ensures data accuracy and integrity.

**Report Generation**

For each student, the system generates a report that displays subject-wise marks, total marks, percentage, and grade. The percentage is calculated as the average of all subject marks.

**Grading System**

Grades are assigned based on percentage. For example, 90 and above is A+, 80–89 is A, 70–79 is B, and below 40 is considered Fail. This grading logic is implemented dynamically in the backend.

**Technologies Used**

The project is developed using Python and Django. SQLite is used as the database. HTML and Bootstrap are used to create a clean and responsive user interface.

**Conclusion**

This project demonstrates practical knowledge of Django models, form handling, authentication, database relationships, search functionality, pagination, and dynamic report generation. It showcases backend development skills along with structured data management.