#open data
with open("/Users/thanhminn/data for data analyst/data_project/project thi học sinh giỏi cấp tphcm 2023/Main Data/final_data.csv") as file:
    data = file.read().split("\n")
import csv 
#set data for header and each student:
header = data[0]
students = data[1:]
#total students:
total_students = len(students)
#split header into list:
header = header.split(",")
subjects = header[5:]
#split student into list:
for i in range(len(students)):
    students[i] = students[i].split(",")
#create students not take exam list:
student_not_take_subjects = [0,0,0,0,0,0,0,0,0,0,0]
#loop through students list who not take subject
for student in students:
    for i in range(5,16):
        if student[i] == "-1":
            student_not_take_subjects[i-5] += 1
#create student not take subjects percentage list
student_not_take_subjects_percentage = [0,0,0,0,0,0,0,0,0,0,0]
#loop through student not take subject
for i in range(0,11):
    student_not_take_subjects_percentage[i] = round(student_not_take_subjects[i]*100/total_students,2)
print(student_not_take_subjects_percentage)
print(subjects)
print(student_not_take_subjects)


#make a plot barchart

import matplotlib.pyplot as plt
import numpy 

fig, ax = plt.subplots()

# list from 0-11
y_pos = numpy.arange(len(subjects))

# plot the barchart using 2 list
plt.bar(y_pos, student_not_take_subjects_percentage,color=(0.1, 0.1, 0.1, 0.1),  edgecolor='black')

# change horizontal category name
plt.xticks(y_pos, subjects,)

# set limit 
ax.set_ylim(0,110)

# label and title of plot
plt.ylabel('Percentage',fontdict={'fontname':'Comic Sans MS',})
plt.title('Student not take subject or cancel ',fontdict={'fontname':'Comic Sans MS',})

# Draw number of student on top of each bar
rects = ax.patches
for rect, label in zip(rects, student_not_take_subjects_percentage):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')
# show the plot
plt.show()
   