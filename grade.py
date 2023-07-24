scorework = float(input('please enter your work grades'))
scoremid = float(input('please enter your mid grades'))
scorefinal = float(input("please enter your final grades"))
score=scorework + scoremid + scorefinal
if score > 100:
    grade = 'you are lying'
elif score >= 80:
    grade = 'a'
elif score >= 75:
    grade = 'b+'
elif score >= 70:
    grade = 'B'
elif score >= 65:
    grade = 'c+'
elif score >= 60:
    grade = 'C'
elif score >= 55:
    grade = 'D+'
elif score >= 50:
    grade = 'D'
else:
    grade = 'f'
print('your grade is:', grade)
