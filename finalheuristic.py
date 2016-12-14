import numpy
import pandas

def custom_heuristic(file_path):
    prediction = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female' and passenger['Pclass'] != 3:
            prediction[passenger_id] = 1
        elif passenger['Age'] < 18 and passenger['Pclass'] != 3:
            prediction[passenger_id] = 1
        elif passenger['Fare'] >= 57:
            prediction[passenger_id] = 1
        elif passenger['Sex'] == 'female' and passenger['Pclass'] == 3 and passenger['Embarked'] != 'S':
            prediction[passenger_id] = 1
        elif passenger['Sex'] == "male" and passenger['Pclass'] == 3 and passenger['Age'] <= 9 and passenger['SibSp'] <= 2:
            prediction[passenger_id] = 1
        else:
            prediction[passenger_id] = 0
    return prediction

print custom_heuristic("data/titanic_data.csv")