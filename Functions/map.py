'''
Say we stored our course grades in a list, but some of the grades were on a 
four-point scale (where students score between 0.0 and 4.0) and others were on 
a 100-point scale (where students score between a 0 and 100).To get all the 
grades on the same scale, try using a lambda function inside of the map() 
function. Multiply the grades on the four-point scale by 25 to convert the 
grades to a 100-point-scale.
grade_list = [3.5, 3.7, 2.6, 95, 87]
'''
grade_list = [3.5, 3.7, 2.6, 95, 87]
grades_100scale = map(lambda x: 25 * x if x<=4 else x, grade_list)
updated_grade_list = list(grades_100scale)
print(updated_grade_list)