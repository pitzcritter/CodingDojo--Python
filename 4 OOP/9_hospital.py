
class Patient(object):
    def __init__(self,ID,name,allergies,bed_number="none"):
        self.ID = ID
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

    def display_info(self):
        print self.ID
        print self.name
        print self.allergies
        print self.bed_number


patient1 = Patient(1,"John Dow","dirt")
patient2 = Patient(2,"Stan Lee","flower")
patient3 = Patient(3,"Mary Jane","fish")
patient4 = Patient(4,"Rob Roy","nut")

patients= ["patient"+str(i) for i in range(1,5)]



# for patient in patients:
# 	patient.strip("\"").display_info()
# patient1.display_info()






class Bed(object):
	def __init__(self,ID,bed_number,status="vacant"):
		self.ID = ID
		self.bed_number = bed_number
		self.status = status

	# def change_status(self):
	# 	if


class Hospital(object):
	def __init__(self,name,capacity):
		self.name=name
		self.capacity=capacity
		self.patients=[]
		self.bed_list=[]
		for i in range(1,capacity+1):
			self.bed_list.append(Bed("",i,))

# hospital1 = Hospital("Dallas Memorial",300)
# print hospital1.bed_list

# filter = [bed for bed in hospital1.bed_list if bed.status=="vacant"]
# print len(filter)
	def admit(self, patient):
		if len([bed for bed in bed_list if bed.status=="vacant"]) < self.capacity:
			#alocate first vacant bed in the bed_list
			[bed for bed in bed_list if bed.status=="vacant"][0].ID=patient.ID
			[bed for bed in bed_list if bed.status=="vacant"][0].status="vacant"
			bed_number_list.status="occupied"
			self.patients.append(patient)
			print "Your admission has been confirmed!"
		else:
			print "The hospital is full"
		

	def remove(self,patient):
		patients.remove(patient)
		if bed.ID==patient.ID:
			bed.status="vacant"
# hospital1=Hospital("Dallas Hospital", 10)
# print hospital1.patients
# print patient1.bed_number
# print hospital1.bed_number_list
# hospital1.admit(patient1)