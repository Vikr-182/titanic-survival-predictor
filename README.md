Titanic Survival Predictor
==========================

A list of Titanic passengers and their assosciated information is given and the goal is to write a heuristic that will take in some combination of the passenger's attributes and predict if the passenger survived the 1912 Titanic disaster.

Original problem at [Kaggle](http://www.kaggle.com/c/titanic-gettingStarted)

**Software and Libraries**
- Python 2.7
- NumPy
- pandas

**Introduction**:

In 1912, the ship RMS Titanic struck an iceberg on its maiden voyage and sank, resulting in the deaths of most of its passengers and crew. This project explores a subset of the RMS Titanic passenger manifest to determine which features best predict whether someone survived or did not survive.

The available attributes for the passengers are:
-    __Pclass:__          Passenger's Socio-Economic class
                    (1 = 1st; 2 = 2nd; 3 = 3rd)
-    __Name:__            Name of the passenger
-    __Sex:__             Sex of the passenger
-    __Age:__             Age of the passenger (some entries are NaN)
-    __SibSp:__           Number of Siblings/Spouses Aboard
-    __Parch:__           Number of Parents/Children Aboard
-    __Ticket:__          Ticket Number of the passenger
-    __Fare:__            Fare paid by the passenger
-    __Cabin:__           Cabin number (some entries are NaN)
-    __Embarked:__        Port of Embarkation
                    (C = Cherbourg; Q = Queenstown; S = Southampton)

Age is in years. It is fractional if age is less than one
If the age is estimated, it is in the form xx.5

The data used for this project is available [here](https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv)

My final heuristic yields an accuracy of __80.25%__
