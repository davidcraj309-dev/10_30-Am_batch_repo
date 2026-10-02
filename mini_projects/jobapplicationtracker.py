

class JobApplication:

    def __init__(self,company,role,status,date):
        self.company = company
        self.role = role
        self.status = status
        self.date = date
       

class AIJobApplication(JobApplication):

    def __init__(self,company,role,status,date,type):
        super(). __init__(company,role,status,date)
        self.type = type
        print(f"Company:{self.company}")
        print(f"Role:{self.role}")
        print(f"status:{self.status}")
        print(f"date:{self.date}")
        print(f"Type:{self.type}")

    @classmethod
    def from_string(cls,data):
        values = data.split(",")

        company = values[0]
        role = values[1]
        status = values[2]
        date = values[3]
        type = values[4]

        return cls(company,role,status,date,type)     


# Storage
applications = []


# Add Application

def add_application():

    print("\n--- ADD APPLICATION ---")

    company = input("Enter company name: ").strip()
    role = input("Enter role: ").strip()
    status = input("Enter status: ").strip()
    date = input("Enter date: ").strip()
    job_type = input("Enter job type: ").strip()

    application = AIJobApplication(company,role,status,date,job_type)
    applications.append(application)

    print("\nApplication added successfully!")



while True:

    print("\n")
    print("=" * 45)
    print("            JOB APPLICATION TRACKER")
    print("=" * 45)

    print("1. Add Application")
    print("2. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_application()

    elif choice == "2":
        print("\nThank you for using Job Application Tracker!")
        break

    else:
        print("\nInvalid choice. Please try again.")