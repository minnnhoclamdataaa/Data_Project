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
#create list for average score and total score
average_score = [0]*12
total_score = [0]*12
#loop through students list who take subject 
for student in students:
    for i in range(4,16):
        if student[i] != "-1":
            average_score[i-4] += 1
            total_score[i-4] += float(student[i])
for i in range(12):
    if average_score[i] != 0:
        average_score[i] =round(total_score[i]/average_score[i],2)

#draw plot using bar chart
import matplotlib.pyplot as plt
import numpy 

figure, axis = plt.subplots()

# list from 0-11
y_pos = numpy.arange(len(subjects))

# plot the bar chart using 2 list
plt.bar(y_pos, average_score,color=(0.1, 0.1, 0.1, 0.1),  edgecolor='black')

# change horizontal category name
plt.xticks(y_pos, subjects,)

# label and title
plt.ylabel('Score',fontdict={'fontname':'Comic Sans MS',})
plt.xlabel('All Subjects',fontdict={'fontname':'Comic Sans MS',})
plt.title('Average Score Of Subject ',fontdict={'fontname':'Comic Sans MS',})

# Draw number of student on top of each bar
rects = axis.patches
for rect, label in zip(rects, average_score):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 0.15, label, ha='center', va='bottom')
# show the plot
plt.show()