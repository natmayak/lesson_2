school_scores = [{'school_class': '4a', 'scores': [3,4,4,4,5,2]}, {'school_class': '7b', 'scores': [5,4,3,5]}, {'school_class': '8c', 'scores': [2,3,4,5,5]}, {'school_class': '11a', 'scores': [5,5,3,5,2]}, {'school_class': '9d', 'scores': [3,4,4,4,3]}]
class_scores_sum = 0
school_scores_sum = 0
class_scores_amount = 0
school_scores_amount = 0

for class_scores in school_scores:
    school_scores_sum += sum(class_scores['scores'])
    school_scores_amount += len(class_scores['scores'])
    class_scores_sum = sum(class_scores['scores'])
    class_scores_amount = len(class_scores['scores'])
    scores_avg = class_scores_sum / class_scores_amount
    class_name = class_scores['school_class']
    print(f"GPA per {class_name} {scores_avg}, total sum: {class_scores_sum}")
school_result = str(school_scores_sum)
school_average = str (school_scores_sum/school_scores_amount)
print(f'Total GPA per school is {school_average}, total sum being {school_result}')