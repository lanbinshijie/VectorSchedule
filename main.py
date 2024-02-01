# 课程从Chinese I, English Liturature I, Math I, Economics I, World History I, Computer Science I中任选 3-5门
mock_data = [
    {"studentId": "T20270001", "courses": ["Chinese I", "Math I", "Economics I"]},
    {"studentId": "T20270002", "courses": ["English Liturature I", "World History I", "Computer Science I"]},
    {"studentId": "T20270003", "courses": ["Math I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270004", "courses": ["Chinese I", "Math I", "Economics I", "World History I"]},
    {"studentId": "T20270005", "courses": ["English Liturature I", "Math I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270006", "courses": ["Chinese I", "English Liturature I", "Economics I"]},
    {"studentId": "T20270007", "courses": ["English Liturature I", "Math I", "World History I"]},
    {"studentId": "T20270008", "courses": ["Chinese I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270009", "courses": ["Chinese I", "Economics I"]},
    {"studentId": "T20270010", "courses": ["Math I", "Economics I", "World History I", "Computer Science I"]},
    {"studentId": "T20270011", "courses": ["English Liturature I", "Math I", "Computer Science I"]},
    {"studentId": "T20270012", "courses": ["Chinese I", "Math I"]},
    {"studentId": "T20270013", "courses": ["Chinese I", "Economics I", "World History I"]},
    {"studentId": "T20270014", "courses": ["English Liturature I", "Math I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270015", "courses": ["Math I", "Economics I"]},
    {"studentId": "T20270016", "courses": ["Chinese I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270017", "courses": ["Chinese I", "Math I", "Economics I"]},
    {"studentId": "T20270018", "courses": ["English Liturature I", "Math I", "World History I"]},
    {"studentId": "T20270019", "courses": ["Chinese I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270020", "courses": ["Chinese I", "Economics I"]},
    {"studentId": "T20270021", "courses": ["Math I", "Economics I", "World History I", "Computer Science I"]},
    {"studentId": "T20270022", "courses": ["English Liturature I", "Math I", "Computer Science I"]},
    {"studentId": "T20270023", "courses": ["Chinese I", "Math I"]},
    {"studentId": "T20270024", "courses": ["Chinese I", "Economics I", "World History I"]},
    {"studentId": "T20270025", "courses": ["English Liturature I", "Math I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270026", "courses": ["Math I", "Economics I"]},
    {"studentId": "T20270027", "courses": ["Chinese I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270028", "courses": ["Chinese I", "Math I", "Economics I"]},
    {"studentId": "T20270029", "courses": ["English Liturature I", "Math I", "World History I"]},
    {"studentId": "T20270030", "courses": ["Chinese I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270031", "courses": ["Chinese I", "Economics I"]},
    {"studentId": "T20270032", "courses": ["Math I", "Economics I", "World History I", "Computer Science I"]},
    {"studentId": "T20270033", "courses": ["English Liturature I", "Math I", "Computer Science I"]},
    {"studentId": "T20270034", "courses": ["Chinese I", "Math I"]},
    {"studentId": "T20270035", "courses": ["Chinese I", "Economics I", "World History I"]},
    {"studentId": "T20270036", "courses": ["English Liturature I", "Math I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270037", "courses": ["Math I", "Economics I"]},
    {"studentId": "T20270038", "courses": ["Chinese I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270039", "courses": ["Chinese I", "Math I", "Economics I"]},
    {"studentId": "T20270040", "courses": ["English Liturature I", "Math I", "World History I"]},
    {"studentId": "T20270041", "courses": ["Chinese I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270042", "courses": ["Chinese I", "Economics I"]},
    {"studentId": "T20270043", "courses": ["Math I", "Economics I", "World History I", "Computer Science I"]},
    {"studentId": "T20270044", "courses": ["English Liturature I", "Math I", "Computer Science I"]},
    {"studentId": "T20270045", "courses": ["Chinese I", "Math I"]},
    {"studentId": "T20270046", "courses": ["Chinese I", "Economics I", "World History I"]},
    {"studentId": "T20270047", "courses": ["English Liturature I", "Math I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270048", "courses": ["Math I", "Economics I"]},
    {"studentId": "T20270049", "courses": ["Chinese I", "Economics I", "Computer Science I"]},
    {"studentId": "T20270050", "courses": ["Chinese I", "Math I", "Economics I"]}
]


def fill_course_list(data, course_list):
    for item in data:
        for course in item["courses"]:
            if course not in course_list:
                course_list.append(course)
    return course_list

course_list = fill_course_list(mock_data, list())

def rearrangeStudentData(data, course_list):
    datar = []
    for stu in data:
        l = []
        for c in course_list:
            if c in stu["courses"]: l.append(1)
            else: l.append(0)
        datar.append({"studentId": stu["studentId"], "course": l})
    return datar

mock_data = rearrangeStudentData(mock_data, course_list)
print(course_list)
print(mock_data)

from sklearn.cluster import KMeans
import numpy as np

def assign_students(courses, num_classes):
    # 构建特征矩阵
    features = np.array([student['course'] for student in courses])

    # 使用K-means进行聚类
    kmeans = KMeans(n_clusters=num_classes, random_state=0).fit(features)
    
    # 初始化班级字典
    classes = {i: {'students': [], 'course_vector': None} for i in range(num_classes)}
    
    # 分配学生到班级
    for i, label in enumerate(kmeans.labels_):
        student = courses[i]
        classes[label]['students'].append(student['studentId'])
        
        # 更新班级的代表性课程向量
        if classes[label]['course_vector'] is None:
            classes[label]['course_vector'] = student['course']
        else:
            classes[label]['course_vector'] += student['course']
    
    # 打印结果
    for i in range(num_classes):
        class_info = classes[i]
        print(f'班级{i+1}:')
        print(f'学生: {class_info["students"]}')
        print(f'课程向量: {class_info["course_vector"]}')
        print()

assign_students(course_list,mock_data)