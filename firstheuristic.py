import numpy
import pandas

def custom_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        if passenger['Sex'] == 'female':
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0
    return predictions

print custom_heuristic("data/titanic_data.csv")
