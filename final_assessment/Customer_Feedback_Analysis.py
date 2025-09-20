def positive_feedback_percentage(ratings):
    if(not ratings):
        print("No ratings available.")
        return
    else:
        positive_ratings=((ratings.count(4)+ratings.count(5))/len(ratings))*100
        return positive_ratings
ratings=eval(input("Enter the ratings : "))
percentage=positive_feedback_percentage(ratings)
print(f"Positive Feedback: {percentage}%")