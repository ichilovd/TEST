import csv

images = []
thunder = []

with open('filename.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if len(row) == 2:
            try:
                im_name = row[0]
                im_time = int(row[1])
                images.append((im_name, im_time))
            except ValueError as e:
                print(f"Error parsing image data: {e}")

with open('thunder.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if len(row) == 2:
            try:
                th_light = int(row[0])
                th_time = float(row[1])
                thunder.append((th_light, th_time))
            except ValueError as e:
                print(f"Error parsing thunder data: {e}")

thunder_times = []

for th_light, th_time in thunder:
    if th_light == 1:
        thunder_times.append(th_time)

result = []

for im_name, im_time in images:
    for th_time in thunder_times:
        if abs(im_time - th_time) < 0.1:
            result.append(im_name)
            break

for i in result:
    print(i)
