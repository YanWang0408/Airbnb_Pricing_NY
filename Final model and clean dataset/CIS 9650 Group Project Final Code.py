# import dataset 
import pandas as pd
df = pd.read_csv("Final_dataset.csv")

# independent variables and dependent variable
x = df.iloc[:, 0:15].values
y = df.iloc[:, 15].values

 # traing set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

# fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(x_train, y_train)

# predict y value using x test set
y_pred = regressor.predict(x_test)

# find correlation between y predict and y test
from sklearn.metrics import r2_score
R2 = r2_score(y_test, y_pred)
# more info, please refer to https://en.wikipedia.org/wiki/Entropy_(information_theory)

df2 = df
#change column names to make it clearer 
df2.rename(columns={'bathrooms':'Number of bathrooms:'},inplace=True)
df2.rename(columns={'bedrooms':'Number of bedrooms:'},inplace=True)
df2.rename(columns={'beds':'Number of beds:'},inplace=True)
df2.rename(columns={'security_deposit':'Amount of security deposits ($):'},inplace=True)
df2.rename(columns={'cleaning_fee':'Amount of cleaning fee ($):'},inplace=True)
df2.rename(columns={'guests_included':'Number of guests:'},inplace=True)
df2.rename(columns={'extra_people':'Number of extra people:'},inplace=True)
df2.rename(columns={'number_of_reviews':'Number of reviews:'},inplace=True)
df2.rename(columns={'review_scores_rating':'Review scores rating (0-100):'},inplace=True)

# asking house owners to provide details of their house and predict price for him/her
collists = list(df2.columns)
collists.remove('price')
test_values = pd.DataFrame(columns = collists)

neighborhood = input("Enter your neighborhood : M for Manhattan, B for Brooklyn, Q for Queens: ")
neighborhood = neighborhood.upper()
if neighborhood == "M":
    test_values.loc[0,'Manhattan'] = 1
    test_values.loc[0,'Brooklyn'] = 0
    test_values.loc[0,'Queens'] = 0
elif neighborhood == "B":
    test_values.loc[0,'Manhattan'] = 0
    test_values.loc[0,'Brooklyn'] = 1
    test_values.loc[0,'Queens'] = 0
elif neighborhood == "Q":
    test_values.loc[0,'Manhattan'] = 0
    test_values.loc[0,'Brooklyn'] = 0
    test_values.loc[0,'Queens'] = 1
    
room_type = input("Enter your room type : E for Entire home, P for Private room, S for Shared room : ")
room_type = room_type.upper()
if room_type == "E":
    test_values.loc[0,'Entire_home'] = 1
    test_values.loc[0,'Private_room'] = 0
    test_values.loc[0,'Shared_room'] = 0
elif room_type == "P":
    test_values.loc[0,'Entire_home'] = 0
    test_values.loc[0,'Private_room'] = 1
    test_values.loc[0,'Shared_room'] = 0
elif room_type == "S":
    test_values.loc[0,'Entire_home'] = 0
    test_values.loc[0,'Private_room'] = 0
    test_values.loc[0,'Shared_room'] = 1
    
print("Please enter the following values")    
for collist in collists:
    if (collist != 'Manhattan' and collist != 'Brooklyn' and collist != 'Queens') and (collist != 'Entire_home' and collist != 'Private_room' and collist != 'Shared_room'):
        inputData = input(collist)
        test_values.loc[0,collist] = float(inputData)
    
new_pred = regressor.predict(test_values)
print("You entered: \n", test_values)
print("we suggest price $",new_pred[0],"per night")


