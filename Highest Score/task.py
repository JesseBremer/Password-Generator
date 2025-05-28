student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_in_list = 0

for score in student_scores:
    if max_in_list < score:
        max_in_list = score

print(max_in_list)