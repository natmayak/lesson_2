school_scores = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '7b', 'scores': [5,4,3,5,5]}, {'school_class': '8c', 'scores': [2,3,4,5,5]}, {'school_class': '11a', 'scores': [5,5,3,5,2]}, {'school_class': '9d', 'scores': [3,4,4,4,3]}]
amount_of_classes = len(school_scores)
scores_sum = 0

# for class_scores in school_scores:
#     av_school_score = sum(class_scores[:(amount_of_classes - 1)])
#I didn't guess how to count school average prior to class average.  Still thinking

for score in school_scores[amount_of_classes - 1]["scores"]:
    scores_sum = sum(school_scores[amount_of_classes - 1]["scores"])
    scores_avg = scores_sum / len(school_scores[amount_of_classes - 1]["scores"])
    class_name = school_scores[amount_of_classes - 1]['school_class']
    print(f"GPA per {class_name} {scores_avg}, total sum: {scores_sum}")
    amount_of_classes = amount_of_classes - 1

