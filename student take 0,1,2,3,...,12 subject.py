# read file
with open("/Users/thanhminn/data for data analyst/data_project/project thi học sinh giỏi cấp tphcm 2023/Main Data/final_data.csv") as file:
    data = file.read().split("\n")

#set data for code
header = data[0]
students = data[1:]
total_student = len(students)

# split header
header = header.split(",")
arr = header[4:]

# turn each student into a list
for i in range(len(students)):
	students[i] = students[i].split(",")

# number of students who took 0,1,2,3,...12 
num_of_subject_taken = [0]*12

for student in students:
	count = 0
	for i in range(12):
		if student[i+4] != "-1":
			count += 1
	num_of_subject_taken[count] += 1
 
#Drawing bar chart plot
import matplotlib.pyplot as plt
import numpy  

#create y axis label using arr list
arr = ["0 Subject","1 Subject","2 Subject","3 Subject","4 Subject","5 Subject","6 Subject","7 Subject","8 Subject","9 Subject","10 Subject","11 Subject"]
fig, ax = plt.subplots()

# list form y label
y_pos = numpy.arange(len(arr))

# plot the bar chart using 2 list
plt.bar(y_pos, num_of_subject_taken,color=(0.1, 0.1, 0.1, 0.1),  edgecolor='black')

# change horizontal category name
plt.xticks(y_pos, arr,)

# label and title
plt.ylabel('Numbers of Student',fontdict={'fontname':'Comic Sans MS',})
plt.title('Student Take 1,2,..... Subject ',fontdict={'fontname':'Comic Sans MS',})

# draw number of student 
rects = ax.patches
for rect, label in zip(rects, num_of_subject_taken):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 0.75, label, ha='center', va='bottom')
    
# show the plot
plt.show()
