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

student_take_subjects = [0]*12

#loop through students list who take subject
for student in students:
    for i in range(4,16):
        if student[i] != "-1":
            student_take_subjects[i-4] += 1   
highest_score = [0]*12

for student in students:
     for i in range(12):
        score = float(student[i+4])
        if score > highest_score[i]:
                highest_score [i] = score  
                        

import matplotlib.pyplot as plt
import numpy as np
average_score 
highest_score 
print(subjects)
penguin_means = {
    'average_score': average_score,
    'highest_score': highest_score,
}

x = np.arange(len(subjects))  # the label locations
width = 0.35  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Score')
ax.set_title('Highest Score and Average Score')
ax.set_xticks(x+0.17)
ax.set_xticklabels(subjects,)


plt.show() 