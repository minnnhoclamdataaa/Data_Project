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
subjects = header[4:]

#split student into list:
for i in range(len(students)):
    students[i] = students[i].split(",")

#create student take subjects list
student_take_subjects = [0]*12

#loop through students list who take subject
for student in students:
    for i in range(4,16):
        if student[i] != "-1":
            student_take_subjects[i-4] += 1     
                        
#make a plot barchart
import matplotlib.pyplot as plt
import numpy 

fig, ax = plt.subplots()

# list from 0-11
y_pos = numpy.arange(len(subjects))

# plot the barchart using 2 list
plt.bar(y_pos, student_take_subjects,color=(0.1, 0.1, 0.1, 0.1),  edgecolor='black')

# change horizontal category name
plt.xticks(y_pos, subjects,)

# label and title
plt.ylabel('Numbers of Student',fontdict={'fontname':'Comic Sans MS',})
plt.xlabel('All Subjects',fontdict={'fontname':'Comic Sans MS',})
plt.title('Number of students taking each subject ',fontdict={'fontname':'Comic Sans MS',})
# Draw number of student on top 
rects = ax.patches
for rect, label in zip(rects, student_take_subjects):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 0.75, label, ha='center', va='bottom')
# show the plot
plt.show()
   