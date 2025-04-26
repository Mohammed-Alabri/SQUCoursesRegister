# SQUCoursesRegister

**SQUCoursesRegister** is a lightweight Python desktop application that automates the course registration process at **Sultan Qaboos University (SQU)**.  
It provides a simple graphical user interface (GUI) to help students log in, add courses, and check the registration status, saving time and reducing manual errors.

## Features

- 🎓 **Login to SQU SIS**: Authenticate with your SQU student credentials.
- 📚 **Add Courses Automatically**: Bulk-add courses by specifying course and section numbers.
- 🔍 **Registration Status Check**: Detect whether the online registration is currently open or closed.
- 🖥️ **Simple GUI**: Built using `tkinter` and styled with `sv-ttk` for a clean dark theme.
- 🔒 **User Validation**: Basic validation step before proceeding.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mohammed-Alabri/SQUCoursesRegister.git
   cd SQUCoursesRegister
   ```

2. **Install Required Packages**
   Make sure you have Python 3 installed. Then install the required packages:
   ```bash
   pip install requests sv-ttk
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```

## Usage

1. Launch the app (`main.py`).
2. Enter your **SQU username** and **password**.
3. Enter your desired courses in the following format (one per line):
   ```
   MATH2101 10
   COMP3401 20
   CHEM2101 30
   ```
   (Course Code followed by Section Number.)

4. Click **Register** to start the registration process.  
   A pop-up will display the result for each course: whether it was successfully added or not.
