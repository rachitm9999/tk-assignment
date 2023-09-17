import tkinter as tk
import csv

def save_to_csv():
    name = name_entry.get()
    email = email_entry.get()
    contact_no = contact_entry.get()
    address = address_entry.get()
    
    with open('registrations.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Name', 'Email', 'Contact No', 'Address'])
        writer.writerow([name, email, contact_no, address])
    
    # Clear the entry fields
    name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    contact_entry.delete(0, 'end')
    address_entry.delete(0, 'end')

# Create a Tkinter window
window = tk.Tk()
window.title("Registration Form")
window.geometry("400x300")  # Set the window size to 400x300 pixels

# Create a heading label
heading_label = tk.Label(window, text="Registration Form", font=("Helvetica", 16))
heading_label.pack()

# Create labels and entry widgets for each field
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

contact_label = tk.Label(window, text="Contact No:")
contact_label.pack()
contact_entry = tk.Entry(window)
contact_entry.pack()

address_label = tk.Label(window, text="Address:")
address_label.pack()
address_entry = tk.Entry(window)
address_entry.pack()

# Create a submit button
submit_button = tk.Button(window, text="Submit", command=save_to_csv)
submit_button.pack()

# Start the Tkinter main loop
window.mainloop()
