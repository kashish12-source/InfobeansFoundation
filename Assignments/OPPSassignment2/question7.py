
class HospitalManagement:

    patients = 0
    hospital_name = ""
    __data = {}

    def __init__(self, id, name, disease, doctor):

        self.__id = id
        self.__name = name
        self.__disease = disease
        self.__doctor = doctor

        HospitalManagement.patients += 1

        HospitalManagement.__data[self.__id] = {
            "name": self.__name,
            "disease": self.__disease,
            "doctor": self.__doctor
        }

    def display_details(self):

        print(f"\t\t\t{HospitalManagement.hospital_name}")
        print(f"Name : {self.__name}")
        print(f"Patient ID : {self.__id}")
        print(f"Disease : {self.__disease}")
        print(f"Doctor assigned : {self.__doctor}")

    def change_doctor(self):

        patient_id = int(input("Enter the patient ID: "))

        if patient_id in HospitalManagement.__data:

            doctor_name = input("Enter the new doctor's name: ")

            HospitalManagement.__data[patient_id]["doctor"] = doctor_name

            # Update the object whose patient ID matches
            if patient_id == self.__id:
                self.__doctor = doctor_name

            print("Doctor name updated successfully")

        else:
            print("Patient not found")

    def total_patient(self):

        print(f"Total patients in hospital: {HospitalManagement.patients}")

    @classmethod
    def from_string(cls, data):

        patient_id, name, disease, doctor = data.split(",")

        return cls(
            int(patient_id),
            name.strip(),
            disease.strip(),
            doctor.strip()
        )


HospitalManagement.hospital_name = "Mahaveer Hospital"

p1 = HospitalManagement(1, "Taj", "Sugar", "Kashish")
p2 = HospitalManagement(2, "Har", "BP", "Rajkumar")

p1.display_details()
print()

p2.display_details()
print()

p2.change_doctor()
print()

p2.display_details()

print()

p3 = HospitalManagement.from_string(
    "3, Rahul, Fever, Dr. Sharma"
)

p3.display_details()

print()

p1.total_patient()
