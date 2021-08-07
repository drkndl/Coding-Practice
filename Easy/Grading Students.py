import math
import os
import random
import re
import sys

def gradingStudents(grades):
    base=5
    for item in range(len(grades)):
        if grades[item]>37:
            if round(grades[item]/base)>=(grades[item]/base):
                grades[item]=base*round(grades[item]/base)
    return grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
