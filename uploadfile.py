import csv

def get_data(file_name):
    rows = []
    data_file = open(file_name , 'r')
    reader = csv.reader(data_file)
    next(reader,None)
    for row in reader:
        circle = Circle(
            name=row[0],
            slug_name=row[1],
            is_public=int(row[2]),
            verified=int(row[3]),
            is_limited = False if int(row[4]) == 0 else True,
            members_limit = row[4]
        )
    circle.save()