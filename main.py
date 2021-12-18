import csv
import random as r
from pandas import *

def load_file(file_name):
    try:
        data = read_csv(file_name, encoding='Latin1')
        Show_Number = data['Show_Number'].tolist()
        Air_Date = data['Air_Date'].tolist()
        Round = data['Round'].tolist()
        Category = data['Category'].tolist()
        Value = data['Value'].tolist()
        Question = data['Question'].tolist()
        Answer = data['Answer'].tolist()
        rating = []
        #Difficulty Value
        # 1         0-1000
        # 2         1001-2500
        # 3         2501-5000
        # 4         5001-7500
        # 5         7500-
        remove = "$,"

        #Remove special characters and set any none values to 500 as the
        #default value for the questions giving it the rating 1
        for char in remove:
            Value = list(map(lambda x: x.replace(char,""), Value))
        Value = [500 if i == 'None' else i for i in Value]
        #Convert from string to int
        Value = list(map(int, Value))
        for i in Value:
            if i <= 1000:
                rating.append(1)
            elif i>1000 and i<=2500:
                rating.append(2)
            elif i>2500 and i<=5000:
                rating.append(3)
            elif i>5000 and i<=7500:
                rating.append(4)
            elif i>7500:
                rating.append(5)

        return Show_Number, Air_Date, Round, Category, Value, rating, Question, Answer

    except FileNotFoundError as e:
        print(e)
        raise


if __name__ == "__main__":
    show_num, air_date, round, category, value, rating, ques, ans = \
    load_file('JEOPARDY_CSV.csv')
    number_of_rounds = int(input("How many rounds: "))
    difficulty = int(input("Select difficulty(1-5): "))
    ques_list = r.choices([i for i in range(len(rating)) if rating[i] == difficulty], k = number_of_rounds)
    for i in ques_list:
        print(ques[i])
