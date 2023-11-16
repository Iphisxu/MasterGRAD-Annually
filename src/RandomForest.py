import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def read_data(years, month, region, datapath):
    df = {}

    for year in years:
        df[year] = pd.read_excel(datapath + f'SIM_{region}_{month}_{year}.xlsx', index_col=0)

    data = pd.concat(df, axis=0)
    data.reset_index(level=0, inplace=True)
    data.drop(columns='level_0', inplace=True)

    return data

def rf_importance(df, variants, target, random_state=42, test_size=0.2):
    # Splitting the data
    X = df[variants]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Creating and training the Random Forest Regressor model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=random_state)
    rf_model.fit(X_train, y_train)

    # Predicting results
    y_pred_rf = rf_model.predict(X_test)

    # Mean Squared Error
    mse = mean_squared_error(y_test, y_pred_rf)
    print(f'Mean Squared Error (Random Forest): {mse}')

    # R-squared
    r2 = r2_score(y_test, y_pred_rf)
    print(f'R-squared (Random Forest): {r2}')

    # Getting feature importance
    feature_importance = rf_model.feature_importances_

    # Creating a DataFrame to store feature importance
    df_output = pd.DataFrame (
        index=variants,
        columns=['importance'],
    )
    
    # Matching feature importance with feature names
    for feature, importance in zip(variants, feature_importance):
        df_output.loc[feature, 'importance'] = importance

    # Sorting feature importance in descending order
    feature_importance_dict = dict(zip(variants, feature_importance))
    sorted_feature_importance = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)

    # Printing each variable's impact on O3
    for feature, importance in sorted_feature_importance:
        print(f'{feature}: {importance}')

    return df_output
