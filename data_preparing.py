import csv
#open data
file = open("/Users/thanhminn/data for data analyst/data_project/project thi học sinh giỏi cấp tphcm 2023/Data preparing/raw_data.txt", "r")
#read 1 line in raw_data.txt: data = file.readline()
#combine data to csv file
all_data = file.read().split("\n")
with open("/Users/thanhminn/Desktop/final_data.csv", encoding="utf8", mode="w", newline='') as file_csv:
	header = ["Tên-Số báo danh", "Ngày", "Tháng", "Năm", "Ngữ Văn", "Lịch Sử", "Địa Lý", "Toán", "Vật Lý", "Hoá Học", "Sinh Học", "Tin Học", "Tiếng Anh", "Tiếng Pháp", "Tiếng Trung", "Tiếng Nhật"]
	writer = csv.writer(file_csv)
	writer.writerow(header)
#add header for file csv
# file_csv = open("test.csv")
for data in all_data:
    #make data into type list
    data = data.split("\\n") 
    #delete "\\t" 
    for i in range (len(data)):
        data[i] = data[i].replace("\\t", "")
    #delete tags
    # data[i] = 1 line data
    for i in range(len(data)):
        tags = []
        for j in range(len(data[i])):
            if data[i][j] == "<":
                start = j
            if data[i][j] == ">":
                end = j
                tag = data[i][start:end+1]
                tags.append(tag)
        for a in (tags):
            data[i] = data[i].replace(a, "")
    #delete whitespace character
    for i in range(len(data)):
        data[i] = data[i].strip()
    #delete empty line
    unempty = []
    for i in range(len(data)):
        if data[i] != "":
            unempty.append(data[i])
    data = unempty  
    #main data for project
    name = data[6]
    date_of_birth = data[7]
    scores = data[8]
    #unicode convert
    characters = []
    codes = []
    file = open("/Users/thanhminn/data for data analyst/data_project/project thi học sinh giỏi cấp tphcm 2023/Data preparing/unicode_convert.txt", "r")
    #split characters and code
    unicode_table = file.read().split("\n")
    for code in unicode_table:
        x = code.split("\t")
        if len(x) >= 5: # check length of x
            characters.append(x[4])
            codes.append(x[3])
    #rename all unicode character
    for i in range (len(characters)):
        name = name.replace(codes[i],characters[i])
        scores = scores.replace(codes[i],characters[i])
    #change to lower case
    name = name.lower()
    scores = scores.lower()
    #split date_of_bỉth
    date_of_birth_list = date_of_birth.split("/")
    dd = int(date_of_birth_list[0])
    mm = int(date_of_birth_list[1])
    yyyy = int(date_of_birth_list[2])
    #processing the scores
    scores = scores.replace(":", "")
    name = name.replace("_"," ")
    scores = scores.replace("môn","")
    scores = scores.replace("điểm","")
    #split scores list
    scores_list = scores.split("  ")
    #main data 
    data = [name.title(),str(dd),str(mm),str(yyyy)]   
    #add scores to data
    for subject in [" ngữ văn"," lịch sử"," địa lý"," toán"," vật lý"," hóa học"," sinh học"," tin học"," tiếng anh"," tiếng pháp"," tiếng trung"," tiếng nhật"]:
        if subject in scores_list:
            index = scores_list.index(subject) + 1
            if scores_list[index] == "vắng":
                data.append("-1")
            else:
                data.append(str(float(scores_list[index])))
        else:
            data.append("-1")

    # file = open("/Users/thanhminn/Desktop/test1.txt","a")
    # for i in range(len(data)):
    #     file.write(data[i] + ",") 
    # file.write("\n")
    #write file to csv file
    with open("/Users/thanhminn/Desktop/final_data.csv","a",encoding="utf-8",newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(data)
    
