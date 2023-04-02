# read file
with open("/Users/thanhminn/data for data analyst/data_project/project thi học sinh giỏi cấp tphcm 2023/Main Data/final_data.csv") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]



total_student = len(students)

# split header
header = header.split(",")
subjects = header[4:]
print(len(subjects))


# turn each student to a list
for i in range(len(students)):
	students[i] = students[i].split(",")
print(students[1])
# number of students who took 0,1,2,3,...12 arr
highest_score = [0]*12

for student in students:
     for i in range(12):
        score = float(student[i+4])
        if score > highest_score[i]:
                highest_score [i] = score
print(highest_score)
print(len(highest_score))



import matplotlib.pyplot as plt
import numpy 

figure, axis = plt.subplots()

# list from 0-11
y_pos = numpy.arange(len(subjects))

# plot the barchart using 2 list
plt.bar(y_pos, highest_score,color=(0.1, 0.1, 0.1, 0.1),  edgecolor='black')

# change horizontal category name
plt.xticks(y_pos, subjects,)

# set limit to vertical axis
# axis.set_ylim(0,105)

# label and title
plt.ylabel('Score',fontdict={'fontname':'Comic Sans MS',})
plt.xlabel('All Subjects',fontdict={'fontname':'Comic Sans MS',})
plt.title('Top Highest Score ',fontdict={'fontname':'Comic Sans MS',})

# Draw number of student on top of each bar
rects = axis.patches
for rect, label in zip(rects, highest_score):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 0.15, label, ha='center', va='bottom')
# show the plot
plt.show()
   