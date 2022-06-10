# from distutils.dep_util import newer_pairwise
# from turtle import st
# from zlib import MAX_WBITS


student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


# Locate max value with MAX function    
print(max(student_scores))

# Manual way to find max value using FOR LOOP
high_score = 0
for num in student_scores:
    if(num > high_score):
        high_score = num

print(high_score)





