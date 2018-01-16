#Assignment: Hospital
#You're going to build a hospital with patients in it! Create a hospital class.
#Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?
#Patient:
#Attributes:
#- Id: an id number
#- Name
#- Allergies
#- Bed number: should be none by default
class Patient(object):
    def __init__(self,id,name,allergies,bed_number):
        self.id = id
        self.name=name
        self.allergies = allergies
        self.bed_number = bed_number
        self.admitted = False
#Hospital
#Attributes:
#- Patients: an empty array
#- Name: hospital name
#- Capacity: an integer indicating the maximum number of patients the hospital can hold.

#Methods:
#- Admit: add a patient to the list of patients. Assign the patient a bed number. 
# If the length of the list is >= the capacity do not admit the patient. 
# Return a message either confirming that admission is complete or saying the hospital is full.
#
#- Discharge: look up and remove a patient from the list of patients. 
# Change bed number for that patient back to none.
#
# This is a challenging assignment. Ask yourself what input each method requires and what output you will need.

class Hospital(object):
    def __init__(self, name, capacity=10, *these_patients):
        self.patients = []
        self.name = name
        self.capacity = capacity
        for this_patient in these_patients:
            self.Admit(this_patient)

    def Admit(self,this_patient):
        admitted_count=0
        for patient in self.patients:
            if patient.admitted:
                admitted_count += 1        
        if admitted_count < self.capacity:            
            this_patient.admitted = True
            self.patients.append(this_patient)
            print this_patient.name, "admitted"
        else:
            print "Hospital full."
            print "Sorry ", this_patient.name,", your in the streeet"                
        return self

            
    def Discharge(self,patient_name):
        for this_patient in self.patients:
            if patient_name == this_patient.name:
                this_patient.admitted = False
                this_patient.bed_number = 0
                print this_patient.name, "discharged"
                break
 
# prove Patient class workds.
#newPatient = Patient(23,"Carl Bruise","Peanuts",1)
HATCHET_MEDICAL = Hospital("Hatchet Medical",3 ,Patient(23,"Carl Bruise", "Peanuts",1), Patient(24, "Sally Lame", "Walnuts", 1), Patient(25, "Bob Broken", "Filburts", 3),Patient(26, "Larry Largesore", "Peanuts", 1),Patient(27, "Shirly Bruise", "Peanuts", 4))
HATCHET_MEDICAL.Discharge("Carl Bruise")
HATCHET_MEDICAL.Admit(Patient(28,"Rocky Life", "none",1))