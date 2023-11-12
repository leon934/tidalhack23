# Maths.csv: https://www.kaggle.com/datasets/whenamancodes/student-performance/data
# STUDENT_PERFORMANCE_DEMOG.csv: https://www.kaggle.com/datasets/joebeachcapital/students-performance/
# STUDENT_TEST_GRADE.csv: https://www.kaggle.com/datasets/adithyabshetty100/student-performance

import pandas as pd

college_df = pd.read_csv('./original_training_data/COLLEGE_PERFORMANCE.csv')

# Drop columns that are not needed (1).
college_drop_columns = ['Total salary if available']
college_df = college_df.drop(columns=college_drop_columns, axis=1)

# Replacing outputs. (A and B students get a value of 1, while the rest get a value of 0.)
college_df['GRADE'].replace({0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 1, 6 : 1, 7 : 1}, inplace=True)


middle_school_df = pd.read_csv('./original_training_data/MIDDLE_SCHOOL_PERFORMANCE.csv')

# Drop columns that are not needed (1).
middle_school_drop_columns = ['school']
middle_school_df = middle_school_df.drop(columns=middle_school_drop_columns)

# Columns to replace.
replace_columns = ['address', 'famsize']
hot_one_encode_columns = []

# Replace columns with 0 and 1.
# Columns converted to binary: ['schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
middle_school_df.replace({'yes' : 1, 'no' : 0}, inplace=True)
middle_school_df['address'].replace({'U' : 1, 'R' : 0}, inplace=True)

# Columns to add for hot one encoding.
for column in middle_school_df.columns:
    if middle_school_df[column].dtype == 'object':
        
        hot_one_encode_columns.append(column)

# Hot one encoding.
for column in hot_one_encode_columns:
    for unique in middle_school_df[column].unique().tolist():
        column_name = column + '_' + unique
        middle_school_df[column_name] = 0
        middle_school_df[column_name] = middle_school_df[column_name].astype('bool')

    for i in range(middle_school_df.shape[0]):
        for unique in middle_school_df[column].unique().tolist():
            if middle_school_df.loc[i, column] == unique:
                column_name = column + '_' + unique
                middle_school_df.loc[i, column_name] = True
                
middle_school_df.drop(columns=hot_one_encode_columns, inplace=True)

middle_school_df.to_csv('./cleaned_training_data/CLEAN_SECONDARY_SCHOOL_PERFORMANCE.csv')
college_df.to_csv('./cleaned_training_data/CLEAN_COLLEGE_PERFORMANCE.csv')