import requests as rq
import time


def login(user_pass, session: rq.Session):
    for i in user_pass:
        if user_pass[i] == "":
            return False

    global t
    attempts = 0
    print("Logging in...")
    while attempts < 5:
        try:
            url = "https://sis.squ.edu.om/sis/webreg/3s/login.jsp"
            time.sleep(1)
            t = session.post(url, data=user_pass)
            break
        except Exception as e:
            print(f"ERROR: {e}")
            attempts += 1
    if "Authentication failed; invalid user name or password" in str(t.content):
        return False
    return True


def status(session: rq.Session):
    session.get('https://sis.squ.edu.om/sis/webreg/reg.jsp')
    if "Access to Online Registration is disabled" in session.get("https://sis.squ.edu.om/sis/webreg/addSect.jsp").text:
        return False
    return True


def add_course(course, session: rq.Session):
    # to avoid error "enternal error 500".
    session.get('https://sis.squ.edu.om/sis/webreg/reg.jsp')

    regpage2 = session.get(
        f'https://sis.squ.edu.om/sis/webreg/addSect2.jsp?crsno={course[0]}&sectno={course[1]}')

    regcodepage = str(regpage2.content)
    regcodepage = regcodepage[regcodepage.find(
        "name=\"regcode\"", len(regcodepage) // 4 * 3) + 32:]
    regcode = regcodepage[:regcodepage.find("\"")]

    if 2 <= len(course) <= 3:
        regi = ""
        if len(course) == 2:
            regi = session.get(
                f"https://sis.squ.edu.om/sis/webreg/saveSect.jsp?crsno={course[0]}&noOfSections=1&sectno1={course[1]}&regcode={regcode}")
        else:
            regi = session.get(
                f"https://sis.squ.edu.om/sis/webreg/saveSect.jsp?crsno={course[0]}&noOfSections=2&sectno1={course[1]}&sectno2={course[2]}&regcode={regcode}")

        if "Course/Section has been added successfully." in str(regi.content):
            return True
    return False
