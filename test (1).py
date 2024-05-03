
import tkinter as tk
from tkinter import messagebox
import pickle


class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id

class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests




def add_employee_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Employee")

    name_label = tk.Label(add_window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)

    employee_id_label = tk.Label(add_window, text="Employee ID:")
    employee_id_label.grid(row=1, column=0)
    employee_id_entry = tk.Entry(add_window)
    employee_id_entry.grid(row=1, column=1)

    department_label = tk.Label(add_window, text="Department:")
    department_label.grid(row=2, column=0)
    department_entry = tk.Entry(add_window)
    department_entry.grid(row=2, column=1)

    job_title_label = tk.Label(add_window, text="Job Title:")
    job_title_label.grid(row=3, column=0)
    job_title_entry = tk.Entry(add_window)
    job_title_entry.grid(row=3, column=1)

    def add_employee():
        name = name_entry.get()
        employee_id = employee_id_entry.get()
        department = department_entry.get()
        job_title = job_title_entry.get()

        employee = Employee(name, employee_id, department, job_title)
        try:
            with open('employees.pkl', 'ab') as file:
                pickle.dump(employee, file)
            messagebox.showinfo("Success", "Employee added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        add_window.destroy()

    add_button = tk.Button(add_window, text="Add Employee", command=add_employee)
    add_button.grid(row=4, columnspan=2)

def view_employees_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Employees")

    try:
        with open('employees.pkl', 'rb') as file:
            employees = pickle.load(file)
            row = 0
            while employees:
                tk.Label(view_window, text="Name: " + employees.name).grid(row=row, column=0)
                tk.Label(view_window, text="Employee ID: " + employees.employee_id).grid(row=row+1, column=0)
                tk.Label(view_window, text="Department: " + employees.department).grid(row=row+2, column=0)
                tk.Label(view_window, text="Job Title: " + employees.job_title).grid(row=row+3, column=0)
                tk.Label(view_window, text="-------------------------------------").grid(row=row+4, column=0)
                row += 5
                employees = pickle.load(file)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No employees found.")

def delete_employee_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Employee")

    id_label = tk.Label(delete_window, text="Employee ID:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1)

    def delete_employee():
        employee_id = id_entry.get()

        try:
            with open('employees.pkl', 'rb') as file:
                employees = []
                while True:
                    try:
                        employee = pickle.load(file)
                        if employee.employee_id != employee_id:
                            employees.append(employee)
                    except EOFError:
                        break
            with open('employees.pkl', 'wb') as file:
                for employee in employees:
                    pickle.dump(employee, file)
            messagebox.showinfo("Success", "Employee deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No employees found.")

        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete Employee", command=delete_employee)
    delete_button.grid(row=1, columnspan=2)



def add_event_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Event")

    # Labels and Entry fields for Event details
    event_id_label = tk.Label(add_window, text="Event ID:")
    event_id_label.grid(row=0, column=0)
    event_id_entry = tk.Entry(add_window)
    event_id_entry.grid(row=0, column=1)

    event_type_label = tk.Label(add_window, text="Event Type:")
    event_type_label.grid(row=1, column=0)
    event_type_entry = tk.Entry(add_window)
    event_type_entry.grid(row=1, column=1)

    theme_label = tk.Label(add_window, text="Theme:")
    theme_label.grid(row=2, column=0)
    theme_entry = tk.Entry(add_window)
    theme_entry.grid(row=2, column=1)

    date_label = tk.Label(add_window, text="Date:")
    date_label.grid(row=3, column=0)
    date_entry = tk.Entry(add_window)
    date_entry.grid(row=3, column=1)

    time_label = tk.Label(add_window, text="Time:")
    time_label.grid(row=4, column=0)
    time_entry = tk.Entry(add_window)
    time_entry.grid(row=4, column=1)

    duration_label = tk.Label(add_window, text="Duration:")
    duration_label.grid(row=5, column=0)
    duration_entry = tk.Entry(add_window)
    duration_entry.grid(row=5, column=1)

    venue_label = tk.Label(add_window, text="Venue Address:")
    venue_label.grid(row=6, column=0)
    venue_entry = tk.Entry(add_window)
    venue_entry.grid(row=6, column=1)

    client_id_label = tk.Label(add_window, text="Client ID:")
    client_id_label.grid(row=7, column=0)
    client_id_entry = tk.Entry(add_window)
    client_id_entry.grid(row=7, column=1)

    # Function to add event
    def add_event():
        event_id = event_id_entry.get()
        event_type = event_type_entry.get()
        theme = theme_entry.get()
        date = date_entry.get()
        time = time_entry.get()
        duration = duration_entry.get()
        venue_address = venue_entry.get()
        client_id = client_id_entry.get()

        event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id)
        try:
            with open('events.pkl', 'ab') as file:
                pickle.dump(event, file)
            messagebox.showinfo("Success", "Event added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        add_window.destroy()

    # Button to add event
    add_button = tk.Button(add_window, text="Add Event", command=add_event)
    add_button.grid(row=8, columnspan=2)


def view_events_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Events")

    try:
        with open('events.pkl', 'rb') as file:
            row = 0
            while True:
                try:
                    event = pickle.load(file)
                    tk.Label(view_window, text="Event ID: " + event.event_id).grid(row=row, column=0)
                    tk.Label(view_window, text="Event Type: " + event.event_type).grid(row=row+1, column=0)
                    tk.Label(view_window, text="Theme: " + event.theme).grid(row=row+2, column=0)
                    tk.Label(view_window, text="Date: " + event.date).grid(row=row+3, column=0)
                    tk.Label(view_window, text="Time: " + event.time).grid(row=row+4, column=0)
                    tk.Label(view_window, text="Duration: " + event.duration).grid(row=row+5, column=0)
                    tk.Label(view_window, text="Venue Address: " + event.venue_address).grid(row=row+6, column=0)
                    tk.Label(view_window, text="Client ID: " + event.client_id).grid(row=row+7, column=0)
                    tk.Label(view_window, text="-------------------------------------").grid(row=row+8, column=0)
                    row += 9
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No events found.")


def delete_event_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Event")

    id_label = tk.Label(delete_window, text="Event ID:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1)

    def delete_event():
        event_id = id_entry.get()

        try:
            with open('events.pkl', 'rb') as file:
                events = []
                while True:
                    try:
                        event = pickle.load(file)
                        if event.event_id != event_id:
                            events.append(event)
                    except EOFError:
                        break
            with open('events.pkl', 'wb') as file:
                for event in events:
                    pickle.dump(event, file)
            messagebox.showinfo("Success", "Event deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No events found.")

        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete Event", command=delete_event)
    delete_button.grid(row=1, columnspan=2)


def add_client_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Client")

    # Labels and Entry fields for Client details
    client_id_label = tk.Label(add_window, text="Client ID:")
    client_id_label.grid(row=0, column=0)
    client_id_entry = tk.Entry(add_window)
    client_id_entry.grid(row=0, column=1)

    name_label = tk.Label(add_window, text="Name:")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)

    address_label = tk.Label(add_window, text="Address:")
    address_label.grid(row=2, column=0)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=2, column=1)

    contact_label = tk.Label(add_window, text="Contact Details:")
    contact_label.grid(row=3, column=0)
    contact_entry = tk.Entry(add_window)
    contact_entry.grid(row=3, column=1)

    budget_label = tk.Label(add_window, text="Budget:")
    budget_label.grid(row=4, column=0)
    budget_entry = tk.Entry(add_window)
    budget_entry.grid(row=4, column=1)

    # Function to add client
    def add_client():
        client_id = client_id_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        contact_details = contact_entry.get()
        budget = budget_entry.get()

        client = Client(client_id, name, address, contact_details, budget)
        try:
            with open('clients.pkl', 'ab') as file:
                pickle.dump(client, file)
            messagebox.showinfo("Success", "Client added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        add_window.destroy()

    # Button to add client
    add_button = tk.Button(add_window, text="Add Client", command=add_client)
    add_button.grid(row=5, columnspan=2)


def view_clients_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Clients")

    try:
        with open('clients.pkl', 'rb') as file:
            row = 0
            while True:
                try:
                    client = pickle.load(file)
                    tk.Label(view_window, text="Client ID: " + client.client_id).grid(row=row, column=0)
                    tk.Label(view_window, text="Name: " + client.name).grid(row=row+1, column=0)
                    tk.Label(view_window, text="Address: " + client.address).grid(row=row+2, column=0)
                    tk.Label(view_window, text="Contact Details: " + client.contact_details).grid(row=row+3, column=0)
                    tk.Label(view_window, text="Budget: " + client.budget).grid(row=row+4, column=0)
                    tk.Label(view_window, text="-------------------------------------").grid(row=row+5, column=0)
                    row += 6
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No clients found.")


def delete_client_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Client")

    id_label = tk.Label(delete_window, text="Client ID:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1)

    def delete_client():
        client_id = id_entry.get()

        try:
            with open('clients.pkl', 'rb') as file:
                clients = []
                while True:
                    try:
                        client = pickle.load(file)
                        if client.client_id != client_id:
                            clients.append(client)
                    except EOFError:
                        break
            with open('clients.pkl', 'wb') as file:
                for client in clients:
                    pickle.dump(client, file)
            messagebox.showinfo("Success", "Client deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No clients found.")

        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete Client", command=delete_client)
    delete_button.grid(row=1, columnspan=2)



def add_supplier_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Supplier")

    # Labels and Entry fields for Supplier details
    supplier_id_label = tk.Label(add_window, text="Supplier ID:")
    supplier_id_label.grid(row=0, column=0)
    supplier_id_entry = tk.Entry(add_window)
    supplier_id_entry.grid(row=0, column=1)

    name_label = tk.Label(add_window, text="Name:")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)

    address_label = tk.Label(add_window, text="Address:")
    address_label.grid(row=2, column=0)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=2, column=1)

    contact_label = tk.Label(add_window, text="Contact Details:")
    contact_label.grid(row=3, column=0)
    contact_entry = tk.Entry(add_window)
    contact_entry.grid(row=3, column=1)

    # Function to add supplier
    def add_supplier():
        supplier_id = supplier_id_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        contact_details = contact_entry.get()

        supplier = Supplier(supplier_id, name, address, contact_details)
        try:
            with open('suppliers.pkl', 'ab') as file:
                pickle.dump(supplier, file)
            messagebox.showinfo("Success", "Supplier added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        add_window.destroy()

    # Button to add supplier
    add_button = tk.Button(add_window, text="Add Supplier", command=add_supplier)
    add_button.grid(row=4, columnspan=2)


def view_suppliers_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Suppliers")

    try:
        with open('suppliers.pkl', 'rb') as file:
            row = 0
            while True:
                try:
                    supplier = pickle.load(file)
                    tk.Label(view_window, text="Supplier ID: " + supplier.supplier_id).grid(row=row, column=0)
                    tk.Label(view_window, text="Name: " + supplier.name).grid(row=row+1, column=0)
                    tk.Label(view_window, text="Address: " + supplier.address).grid(row=row+2, column=0)
                    tk.Label(view_window, text="Contact Details: " + supplier.contact_details).grid(row=row+3, column=0)
                    tk.Label(view_window, text="-------------------------------------").grid(row=row+4, column=0)
                    row += 5
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No suppliers found.")


def delete_supplier_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Supplier")

    id_label = tk.Label(delete_window, text="Supplier ID:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1)

    def delete_supplier():
        supplier_id = id_entry.get()

        try:
            with open('suppliers.pkl', 'rb') as file:
                suppliers = []
                while True:
                    try:
                        supplier = pickle.load(file)
                        if supplier.supplier_id != supplier_id:
                            suppliers.append(supplier)
                    except EOFError:
                        break
            with open('suppliers.pkl', 'wb') as file:
                for supplier in suppliers:
                    pickle.dump(supplier, file)
            messagebox.showinfo("Success", "Supplier deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No suppliers found.")

        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete Supplier", command=delete_supplier)
    delete_button.grid(row=1, columnspan=2)


def add_guest_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Guest")

    # Labels and Entry fields for Guest details
    guest_id_label = tk.Label(add_window, text="Guest ID:")
    guest_id_label.grid(row=0, column=0)
    guest_id_entry = tk.Entry(add_window)
    guest_id_entry.grid(row=0, column=1)

    name_label = tk.Label(add_window, text="Name:")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)

    address_label = tk.Label(add_window, text="Address:")
    address_label.grid(row=2, column=0)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=2, column=1)

    contact_label = tk.Label(add_window, text="Contact Details:")
    contact_label.grid(row=3, column=0)
    contact_entry = tk.Entry(add_window)
    contact_entry.grid(row=3, column=1)

    # Function to add guest
    def add_guest():
        guest_id = guest_id_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        contact_details = contact_entry.get()

        guest = Guest(guest_id, name, address, contact_details)
        try:
            with open('guests.pkl', 'ab') as file:
                pickle.dump(guest, file)
            messagebox.showinfo("Success", "Guest added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        add_window.destroy()

    # Button to add guest
    add_button = tk.Button(add_window, text="Add Guest", command=add_guest)
    add_button.grid(row=4, columnspan=2)


def view_guests_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Guests")

    try:
        with open('guests.pkl', 'rb') as file:
            row = 0
            while True:
                try:
                    guest = pickle.load(file)
                    tk.Label(view_window, text="Guest ID: " + guest.guest_id).grid(row=row, column=0)
                    tk.Label(view_window, text="Name: " + guest.name).grid(row=row+1, column=0)
                    tk.Label(view_window, text="Address: " + guest.address).grid(row=row+2, column=0)
                    tk.Label(view_window, text="Contact Details: " + guest.contact_details).grid(row=row+3, column=0)
                    tk.Label(view_window, text="-------------------------------------").grid(row=row+4, column=0)
                    row += 5
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No guests found.")


def delete_guest_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Guest")

    id_label = tk.Label(delete_window, text="Guest ID:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1)

    def delete_guest():
        guest_id = id_entry.get()

        try:
            with open('guests.pkl', 'rb') as file:
                guests = []
                while True:
                    try:
                        guest = pickle.load(file)
                        if guest.guest_id != guest_id:
                            guests.append(guest)
                    except EOFError:
                        break
            with open('guests.pkl', 'wb') as file:
                for guest in guests:
                    pickle.dump(guest, file)
            messagebox.showinfo("Success", "Guest deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No guests found.")

        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete Guest", command=delete_guest)
    delete_button.grid(row=1, columnspan=2)


def add_venue_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Venue")

    # Labels and Entry fields for Venue details
    venue_id_label = tk.Label(add_window, text="Venue ID:")
    venue_id_label.grid(row=0, column=0)
    venue_id_entry = tk.Entry(add_window)
    venue_id_entry.grid(row=0, column=1)

    name_label = tk.Label(add_window, text="Name:")
    name_label.grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)

    address_label = tk.Label(add_window, text="Address:")
    address_label.grid(row=2, column=0)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=2, column=1)

    contact_label = tk.Label(add_window, text="Contact:")
    contact_label.grid(row=3, column=0)
    contact_entry = tk.Entry(add_window)
    contact_entry.grid(row=3, column=1)

    min_guests_label = tk.Label(add_window, text="Minimum Guests:")
    min_guests_label.grid(row=4, column=0)
    min_guests_entry = tk.Entry(add_window)
    min_guests_entry.grid(row=4, column=1)

    max_guests_label = tk.Label(add_window, text="Maximum Guests:")
    max_guests_label.grid(row=5, column=0)
    max_guests_entry = tk.Entry(add_window)
    max_guests_entry.grid(row=5, column=1)

    # Function to add venue
    def add_venue():
        venue_id = venue_id_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        contact = contact_entry.get()
        min_guests = min_guests_entry.get()
        max_guests = max_guests_entry.get()

        venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
        try:
            with open('venues.pkl', 'ab') as file:
                pickle.dump(venue, file)
            messagebox.showinfo("Success", "Venue added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        add_window.destroy()

    # Button to add venue
    add_button = tk.Button(add_window, text="Add Venue", command=add_venue)
    add_button.grid(row=6, columnspan=2)


def view_venues_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Venues")

    try:
        with open('venues.pkl', 'rb') as file:
            row = 0
            while True:
                try:
                    venue = pickle.load(file)
                    tk.Label(view_window, text="Venue ID: " + venue.venue_id).grid(row=row, column=0)
                    tk.Label(view_window, text="Name: " + venue.name).grid(row=row+1, column=0)
                    tk.Label(view_window, text="Address: " + venue.address).grid(row=row+2, column=0)
                    tk.Label(view_window, text="Contact: " + venue.contact).grid(row=row+3, column=0)
                    tk.Label(view_window, text="Minimum Guests: " + venue.min_guests).grid(row=row+4, column=0)
                    tk.Label(view_window, text="Maximum Guests: " + venue.max_guests).grid(row=row+5, column=0)
                    tk.Label(view_window, text="-------------------------------------").grid(row=row+6, column=0)
                    row += 7
                except EOFError:
                    break
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No venues found.")


def delete_venue_window():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Venue")

    id_label = tk.Label(delete_window, text="Venue ID:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1)

    def delete_venue():
        venue_id = id_entry.get()

        try:
            with open('venues.pkl', 'rb') as file:
                venues = []
                while True:
                    try:
                        venue = pickle.load(file)
                        if venue.venue_id != venue_id:
                            venues.append(venue)
                    except EOFError:
                        break
            with open('venues.pkl', 'wb') as file:
                for venue in venues:
                    pickle.dump(venue, file)
            messagebox.showinfo("Success", "Venue deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No venues found.")

        delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Delete Venue", command=delete_venue)
    delete_button.grid(row=1, columnspan=2)






def search_client_by_id(client_id):
    try:
        with open('clients.pkl', 'rb') as file:
            while True:
                try:
                    client = pickle.load(file)
                    if client.client_id == client_id:
                        messagebox.showinfo("Client Details", f"Name: {client.name}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}")
                        return
                except EOFError:
                    break
        messagebox.showinfo("Information", "Client not found.")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No clients found.")

def search_supplier_by_id(supplier_id):
    try:
        with open('suppliers.pkl', 'rb') as file:
            while True:
                try:
                    supplier = pickle.load(file)
                    if supplier.supplier_id == supplier_id:
                        messagebox.showinfo("Supplier Details", f"Name: {supplier.name}\nAddress: {supplier.address}\nContact Details: {supplier.contact_details}")
                        return
                except EOFError:
                    break
        messagebox.showinfo("Information", "Supplier not found.")
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No suppliers found.")




# Define main window
root = tk.Tk()
root.title("Event Management System")


# Buttons to control different functionalities
add_event_button = tk.Button(root, text="Add Event", command=add_event_window)
add_event_button.grid(row=0,column=0)

view_events_button = tk.Button(root, text="View Events", command=view_events_window)
view_events_button.grid(row=0,column=1)

delete_event_button = tk.Button(root, text="Delete Event", command=delete_event_window)
delete_event_button.grid(row=0,column=2)

add_client_button = tk.Button(root, text="Add Client", command=add_client_window)
add_client_button.grid(row=1,column=0)

view_clients_button = tk.Button(root, text="View Clients", command=view_clients_window)
view_clients_button.grid(row=1,column=1)

delete_client_button = tk.Button(root, text="Delete Client", command=delete_client_window)
delete_client_button.grid(row=1,column=2)

add_supplier_button = tk.Button(root, text="Add Supplier", command=add_supplier_window)
add_supplier_button.grid(row=2,column=0)

view_suppliers_button = tk.Button(root, text="View Suppliers", command=view_suppliers_window)
view_suppliers_button.grid(row=2,column=1)

delete_supplier_button = tk.Button(root, text="Delete Supplier", command=delete_supplier_window)
delete_supplier_button.grid(row=2,column=2)

add_guest_button = tk.Button(root, text="Add Guest", command=add_guest_window)
add_guest_button.grid(row=3,column=0)

view_guests_button = tk.Button(root, text="View Guests", command=view_guests_window)
view_guests_button.grid(row=3,column=1)

delete_guest_button = tk.Button(root, text="Delete Guest", command=delete_guest_window)
delete_guest_button.grid(row=3,column=2)

# Entry and Button for searching client by ID
search_client_label = tk.Label(root, text="Search Client by ID:")
search_client_label.grid(row=4,column=0)
search_client_entry = tk.Entry(root)
search_client_entry.grid(row=4,column=1)
search_client_button = tk.Button(root, text="Search", command=lambda: search_client_by_id(search_client_entry.get()))
search_client_button.grid(row=4,column=2)

# Entry and Button for searching supplier by ID
search_supplier_label = tk.Label(root, text="Search Supplier by ID:")
search_supplier_label.grid(row=5,column=0)
search_supplier_entry = tk.Entry(root)
search_supplier_entry.grid(row=5,column=1)
search_supplier_button = tk.Button(root, text="Search", command=lambda: search_supplier_by_id(search_supplier_entry.get()))
search_supplier_button.grid(row=5,column=2)

root.mainloop()
