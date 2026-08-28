students = [("Priya", 78, 3), ("aaron", 91, 1), ("Zoe", 78, 2), ("bella", 65, 3), ("Chen", 91, 2)]
# (name, score, year)

stock = {"widget": 12, "bolt": 340, "flange": 12, "gasket": 5, "washer": 88}

files = ["Report.PDF", "notes.txt", "IMAGE.png", "data.csv", "Archive.zip"]

# 1
# print(sorted(students, key= lambda student: student[1]))

# 2
# def get_student_name(name):
#     return name[0].lower()
# print(sorted(students, key= get_student_name))

# 3
# print(sorted(students, key= lambda name: len(name[0])))

# 4
# Non conventional way
# print(sorted(files, key= lambda file: file.split(".")[-1].lower()))
# Conventional way
# print(sorted(files, key= lambda file : file.rsplit(".", maxsplit= 1)[1].lower()))

# 5
# print(sorted(files, key= lambda file : file.rsplit(".", maxsplit= 1)[0].lower()))

# 6
# print(sorted(students, key= lambda student: (-student[1], student[0].lower())))

# 7
# print(sorted(students, key= lambda student: (student[2], -student[1])))

# 8
# print(sorted(students, key= lambda student: (student[2], student[0].lower(), -student[1])))

# 9
# print(sorted(students, key= lambda student: (-student[1], student[2])))

# 10
# print(sorted(stock.items(), key= lambda stocks: -stocks[1]))

# 11
# print(sorted(stock.items(), key= lambda stocks: (stocks[1], stocks[0])))

# 12
# print(sorted(stock.items(), key= lambda stocks: (len(stocks[0]), stocks[0])))

# 13
# print(sorted(stock.items(), key= lambda stocks: stocks[1])[0:3])

# 14
# print(dict(sorted(stock.items(), key= lambda stocks: -stocks[1])))

# 15
# print(sorted(students, key= lambda student: (-student[2], student[0].lower())))

# 16
# def image_first(name):
#     ext = name.split(".")[-1].lower()
#     is_image = ext in {"png", "jpg"}
#     return (not is_image, name.lower())

# print(sorted(files, key=image_first))