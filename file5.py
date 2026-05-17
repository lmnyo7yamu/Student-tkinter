import customtkinter as ctk
from tkinter import messagebox


def submit_form():
    first_name = entry_name.get()
    last_name = entry_surname.get()

    if not first_name or not last_name:
        messagebox.showwarning("Error", "Name and Surname are required!")
        return

    selected_interests = []
    if var_prog.get():
        selected_interests.append("Programming")
    if var_gaming.get():
        selected_interests.append("Gaming")
    if var_sports.get():
        selected_interests.append("Sports")
    if var_music.get():
        selected_interests.append("Music")

    summary = "STUDENT DATA\n\n"
    summary += "Name: " + first_name + "\n"
    summary += "Surname: " + last_name + "\n"
    summary += "Study Mode: " + mode_var.get() + "\n"
    summary += "Faculty: " + faculty_combo.get() + "\n"

    if selected_interests:
        summary += "Interests: " + ", ".join(selected_interests)
    else:
        summary += "Interests: None"

    messagebox.showinfo("Student Summary", summary)


def clear_form():
    entry_name.delete(0, 'end')
    entry_surname.delete(0, 'end')
    mode_var.set("Full-time")
    var_prog.set(False)
    var_gaming.set(False)
    var_sports.set(False)
    var_music.set(False)
    faculty_combo.set("Computer Science")


def toggle_mode():
    if switch_var.get() == "Dark":
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("Light")


app = ctk.CTk()
app.title("Student Registration Form")
app.geometry("450x580")
app.resizable(False, False)

title_label = ctk.CTkLabel(app, text="Student Registration Form", font=("Arial", 18, "bold"))
title_label.pack(pady=15)

form_frame = ctk.CTkFrame(app)
form_frame.pack(padx=20, pady=10, fill="both", expand=True)

ctk.CTkLabel(form_frame, text="Name:").grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry_name = ctk.CTkEntry(form_frame, width=180)
entry_name.grid(row=0, column=1, padx=15, pady=10)

ctk.CTkLabel(form_frame, text="Surname:").grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry_surname = ctk.CTkEntry(form_frame, width=180)
entry_surname.grid(row=1, column=1, padx=15, pady=10)

ctk.CTkLabel(form_frame, text="Study Mode:", font=("Arial", 11, "bold")).grid(row=2, column=0, padx=15, pady=10,
                                                                              sticky="w")
mode_var = ctk.StringVar(value="Full-time")
rb1 = ctk.CTkRadioButton(form_frame, text="Full-time", variable=mode_var, value="Full-time")
rb1.grid(row=3, column=0, padx=25, pady=5, sticky="w")
rb2 = ctk.CTkRadioButton(form_frame, text="Part-time", variable=mode_var, value="Part-time")
rb2.grid(row=4, column=0, padx=25, pady=5, sticky="w")

ctk.CTkLabel(form_frame, text="Interests:", font=("Arial", 11, "bold")).grid(row=2, column=1, padx=15, pady=10,
                                                                             sticky="w")
var_prog = ctk.BooleanVar()
var_gaming = ctk.BooleanVar()
var_sports = ctk.BooleanVar()
var_music = ctk.BooleanVar()

cb1 = ctk.CTkCheckBox(form_frame, text="Programming", variable=var_prog)
cb1.grid(row=3, column=1, padx=25, pady=5, sticky="w")
cb2 = ctk.CTkCheckBox(form_frame, text="Gaming", variable=var_gaming)
cb2.grid(row=4, column=1, padx=25, pady=5, sticky="w")
cb3 = ctk.CTkCheckBox(form_frame, text="Sports", variable=var_sports)
cb3.grid(row=5, column=1, padx=25, pady=5, sticky="w")
cb4 = ctk.CTkCheckBox(form_frame, text="Music", variable=var_music)
cb4.grid(row=6, column=1, padx=25, pady=5, sticky="w")

ctk.CTkLabel(form_frame, text="Faculty:").grid(row=7, column=0, padx=15, pady=15, sticky="w")
faculty_combo = ctk.CTkComboBox(form_frame,
                                values=["Computer Science", "Mechanical Engineering", "Mathematics", "Physics"],
                                state="readonly")
faculty_combo.set("Computer Science")
faculty_combo.grid(row=7, column=1, padx=15, pady=15)

button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

btn_submit = ctk.CTkButton(button_frame, text="Submit", command=submit_form, width=120)
btn_submit.pack(side="left", padx=10)

btn_clear = ctk.CTkButton(button_frame, text="Clear", command=clear_form, width=120)
btn_clear.pack(side="left", padx=10)

switch_var = ctk.StringVar(value="Dark")
mode_switch = ctk.CTkSwitch(app, text="Dark Mode", command=toggle_mode, variable=switch_var, onvalue="Dark",
                            offvalue="Light")
mode_switch.pack(pady=10)
mode_switch.select()

app.mainloop()

