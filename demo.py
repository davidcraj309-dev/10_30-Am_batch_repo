print("=" * 45)
print("        JOB APPLICATION TRACKER")
print("=" * 45)


# -----------------------------
# Parent Class
# -----------------------------

class JobApplication:

    def __init__(self, company, role, status, date):
        self.company = company
        self.role = role
        self.status = status
        self.date = date


# -----------------------------
# Child Class
# -----------------------------

class AIJobApplication(JobApplication):

    def __init__(self, company, role, status, date, job_type):
        super().__init__(company, role, status, date)
        self.job_type = job_type

    # Display one application
    def display(self, number):
        print("\n" + "-" * 45)
        print(f"Application #{number}")
        print("-" * 45)
        print(f"Company : {self.company}")
        print(f"Role    : {self.role}")
        print(f"Status  : {self.status}")
        print(f"Date    : {self.date}")
        print(f"Type    : {self.job_type}")

    # Create object from comma-separated string
    @classmethod
    def from_string(cls, data):
        values = data.split(",")

        company = values[0].strip()
        role = values[1].strip()
        status = values[2].strip()
        date = values[3].strip()
        job_type = values[4].strip()

        return cls(company, role, status, date, job_type)


# -----------------------------
# Storage
# -----------------------------

applications = []


# -----------------------------
# Add Application
# -----------------------------

def add_application():

    print("\n--- ADD APPLICATION ---")

    company = input("Enter company name: ").strip()
    role = input("Enter role: ").strip()
    status = input("Enter status: ").strip()
    date = input("Enter date: ").strip()
    job_type = input("Enter job type: ").strip()

    application = AIJobApplication(
        company,
        role,
        status,
        date,
        job_type
    )

    applications.append(application)

    print("\nApplication added successfully!")


# -----------------------------
# View Applications
# -----------------------------

def view_applications():

    if not applications:
        print("\nNo applications found.")
        return

    print("\n" + "=" * 45)
    print("           ALL APPLICATIONS")
    print("=" * 45)

    for index, application in enumerate(applications, start=1):
        application.display(index)


# -----------------------------
# Update Status
# -----------------------------

def update_status():

    if not applications:
        print("\nNo applications available.")
        return

    view_applications()

    try:
        number = int(input("\nEnter application number: "))

        if number < 1 or number > len(applications):
            print("Invalid application number.")
            return

        new_status = input("Enter new status: ").strip()

        applications[number - 1].status = new_status

        print("\nStatus updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# Delete Application
# -----------------------------

def delete_application():

    if not applications:
        print("\nNo applications available.")
        return

    view_applications()

    try:
        number = int(input("\nEnter application number to delete: "))

        if number < 1 or number > len(applications):
            print("Invalid application number.")
            return

        deleted = applications.pop(number - 1)

        print(f"\nDeleted application for {deleted.company}.")


    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# Search Application
# -----------------------------

def search_application():

    if not applications:
        print("\nNo applications available.")
        return

    keyword = input("\nEnter company or role to search: ").strip().lower()

    found = False

    for index, application in enumerate(applications, start=1):

        if (keyword in application.company.lower()
                or keyword in application.role.lower()):

            application.display(index)
            found = True

    if not found:
        print("\nNo matching application found.")


# -----------------------------
# Main Menu
# -----------------------------

while True:

    print("\n")
    print("=" * 45)
    print("              MAIN MENU")
    print("=" * 45)

    print("1. Add Application")
    print("2. View Applications")
    print("3. Update Status")
    print("4. Delete Application")
    print("5. Search Application")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_application()

    elif choice == "2":
        view_applications()

    elif choice == "3":
        update_status()

    elif choice == "4":
        delete_application()

    elif choice == "5":
        search_application()

    elif choice == "6":
        print("\nThank you for using Job Application Tracker!")
        break

    else:
        print("\nInvalid choice. Please try again.")