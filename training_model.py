import pandas as pd

student_answers = pd.read_csv('./STUDENT_ANSWERS.csv')

# Inplement machine learning model here that'll predict whether the student will get a certain question right or wrong based on curriculum that aligns.

# The prediction above will be used to determine whether to provide the student with a question that's the specific topic or not.

# For example, if a student gets multiple questions wrong (indicated by a 0) about second derivative tests, then the model will predict that the student will get the next question wrong that's about second derivative tests. Therefore, the model will provide the student with a question that's about the second derivative test.