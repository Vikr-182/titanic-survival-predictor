Titanic Survival Predictor
==========================

A list of Titanic passengers and their assosciated information is given and the goal is to write a heuristic that will take in some combination of the passenger's attributes and predict if the passenger survived the Titanic disaster.

Original problem at http://www.kaggle.com/c/titanic-gettingStarted

The available attributes are:
Pclass          Passenger Class
                    (1 = 1st; 2 = 2nd; 3 = 3rd)
    Name            Name
    Sex             Sex
    Age             Age
    SibSp           Number of Siblings/Spouses Aboard
    Parch           Number of Parents/Children Aboard
    Ticket          Ticket Number
    Fare            Passenger Fare
    Cabin           Cabin
    Embarked        Port of Embarkation
                    (C = Cherbourg; Q = Queenstown; S = Southampton)

Age is in years. It is fractional if age is less than one
If the age is estimated, it is in the form xx.5

The data used for this project is available at https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv

My final heuristic yields an accuracy of __80.25%__
