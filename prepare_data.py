#prepare data for project from diemthi.hcm.edu.vn
#01001->09724 khoảng cách số báo danh
#10001->12037 khoảng cách số báo danh
#lấy điểm thi học sinh giỏi 2022 - 2023 TPHCM
import subprocess
start_1 = 1001
end_1 = 9725
start_2 = 10001
end_2 = 12038
file = open("/Users/thanhminn/data test/raw_data.txt", "a")
for i in range (start_2,end_2):
    command = ['curl', '-F', 'SoBaoDanh=' + str(i), 'diemthi.hcm.edu.vn/Home/Show']
    result = subprocess.run(command, capture_output=True, text=True)
    file.write(str(result) + "\n")

