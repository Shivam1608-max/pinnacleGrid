from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Python GUI Registration Form")
root.geometry("500x650")
root.resizable(False, False)

name_var = StringVar()
email_var = StringVar()
phone_var = StringVar()
gender_var = StringVar(value="Male")
course_var = StringVar(value="Select Course")

python_var = IntVar()
java_var = IntVar()
cpp_var = IntVar()


def submit():

    name = name_var.get()
    email = email_var.get()
    phone = phone_var.get()
    gender = gender_var.get()
    course = course_var.get()

    skills = []

    if python_var.get():
        skills.append("Python")

    if java_var.get():
        skills.append("Java")

    if cpp_var.get():
        skills.append("C++")

    # Validation
    if name == "" or email == "" or phone == "":
        messagebox.showerror("Error", "Please fill all required fields.")
        return

    if course == "Select Course":
        messagebox.showerror("Error", "Please select a course.")
        return

    information = f"""
Registration Successful!

Name : {name}
Email : {email}
Phone : {phone}
Gender : {gender}
Course : {course}
Skills : {', '.join(skills) if skills else "None"}
"""

    messagebox.showinfo("Student Information", information)


Label(root,
      text="Python GUI Registration Form",
      font=("Arial", 18, "bold"),
      fg="blue").pack(pady=20)


Label(root, text="Name", font=("Arial", 12)).pack(anchor="w", padx=30)
Entry(root, textvariable=name_var, width=35).pack(padx=30, pady=5)

Label(root, text="Email", font=("Arial", 12)).pack(anchor="w", padx=30)
Entry(root, textvariable=email_var, width=35).pack(padx=30, pady=5)

Label(root, text="Phone", font=("Arial", 12)).pack(anchor="w", padx=30)
Entry(root, textvariable=phone_var, width=35).pack(padx=30, pady=5)


Label(root, text="Gender", font=("Arial", 12)).pack(anchor="w", padx=30)

Frame_gender = Frame(root)
Frame_gender.pack(anchor="w", padx=30)

Radiobutton(Frame_gender,
            text="Male",
            variable=gender_var,
            value="Male").pack(side=LEFT)

Radiobutton(Frame_gender,
            text="Female",
            variable=gender_var,
            value="Female").pack(side=LEFT)

Radiobutton(Frame_gender,
            text="Other",
            variable=gender_var,
            value="Other").pack(side=LEFT)



Label(root, text="Skills", font=("Arial", 12)).pack(anchor="w", padx=30)

Checkbutton(root,
            text="Python",
            variable=python_var).pack(anchor="w", padx=50)

Checkbutton(root,
            text="Java",
            variable=java_var).pack(anchor="w", padx=50)

Checkbutton(root,
            text="C++",
            variable=cpp_var).pack(anchor="w", padx=50)


Label(root, text="Course", font=("Arial", 12)).pack(anchor="w", padx=30, pady=10)

courses = [
    "Select Course",
    "Python",
    "Java",
    "C++",
    "Data Science",
    "Web Development",
    "Machine Learning"
]

OptionMenu(root, course_var, *courses).pack()


Button(root,
       text="Submit",
       command=submit,
       bg="green",
       fg="white",
       font=("Arial", 12, "bold"),
       width=15).pack(pady=30)



root.mainloop()