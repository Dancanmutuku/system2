
class Employee:
    def __init__(self, employee_id, name, date_of_birth, contact_info, employment_history, qualifications, certifications):
        self.employee_id = employee_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.contact_info = contact_info
        self.employment_history = employment_history
        self.qualifications = qualifications
        self.certifications = certifications

    def update_personal_info(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update_employment_details(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self.employment_history, key, value)

    def view_employee_info(self):
        return {
            "Employee ID": self.employee_id,
            "Name": self.name,
            "Date of Birth": self.date_of_birth,
            "Contact Information": self.contact_info,
            "Employment History": self.employment_history,
            "Qualifications": self.qualifications,
            "Certifications": self.certifications
        }