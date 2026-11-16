import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# --- Pre-process ---
df = pd.read_csv("uber.csv").drop(columns=["Unnamed: 0", "key"], errors="ignore").dropna()
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df["hour"] = df["pickup_datetime"].dt.hour
df["weekday"] = df["pickup_datetime"].dt.weekday
df["month"] = df["pickup_datetime"].dt.month
df["year"] = df["pickup_datetime"].dt.year


def haversine(lat1, lon1, lat2, lon2):  # distance in km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    a = np.sin((lat2 - lat1) / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2) ** 2
    return 6371 * 2 * np.arcsin(np.sqrt(a))


df["distance"] = haversine(df.pickup_latitude, df.pickup_longitude,
                           df.dropoff_latitude, df.dropoff_longitude)
df = df.drop(columns="pickup_datetime")

# --- Outliers: invalid values, then IQR rule on fare and distance ---
df = df[(df.fare_amount > 0) & (df.passenger_count.between(1, 6)) & (df.distance > 0)]
for col in ["fare_amount", "distance"]:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    df = df[df[col].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)]

# --- Correlation ---
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.show()

# --- Models ---
X, y = df.drop(columns="fare_amount"), df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {"Linear Regression": LinearRegression(),
          "Random Forest": RandomForestRegressor(n_estimators=50, n_jobs=-1, random_state=42)}
for name, model in models.items():
    pred = model.fit(X_train, y_train).predict(X_test)
    print(f"{name}: R2 = {r2_score(y_test, pred):.4f}, "
          f"RMSE = {np.sqrt(mean_squared_error(y_test, pred)):.4f}")


# ======================= VIVA QUESTIONS =======================
# Q: Is this a regression or classification problem? Why?
# A: Regression - the target (fare_amount) is a continuous number.
# Q: Explain linear regression.
# A: Fits y = b0 + b1*x1 + ... + bn*xn by minimizing the sum of squared errors (ordinary least squares).
# Q: Assumptions of linear regression?
# A: Linearity, independent errors, constant variance (homoscedasticity), normally distributed residuals, no multicollinearity.
# Q: Explain random forest regression.
# A: Ensemble of many decision trees trained on bootstrap samples with random feature subsets (bagging);
#    the prediction is the average of all trees. Reduces variance/overfitting of a single tree.
# Q: Why does random forest often beat linear regression here?
# A: It captures non-linear relationships and feature interactions (e.g. time of day x distance).
# Q: What is R2 (coefficient of determination)?
# A: 1 - SS_res / SS_tot: fraction of variance in the target explained by the model. 1 = perfect, 0 = predicts the mean;
#    it can be negative for a model worse than the mean.
# Q: What is RMSE?
# A: Square root of the mean of squared errors, in the same unit as the target (dollars). Penalizes large errors.
# Q: RMSE vs MAE vs MSE?
# A: MSE = mean squared error; RMSE = sqrt(MSE); MAE = mean absolute error (less sensitive to outliers).
# Q: What is an outlier and how did you detect it?
# A: A value far from the rest. Used invalid-value filters (fare <= 0, bad passenger count) and the IQR rule:
#    outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR]. Others: z-score, boxplot.
# Q: Why remove outliers?
# A: They distort the fitted line and inflate the error, especially for linear regression.
# Q: What is the haversine formula and why use it?
# A: Gives the great-circle distance between two lat/long points on a sphere; Euclidean distance on raw
#    coordinates is wrong because the Earth is curved.
# Q: What is correlation? Range?
# A: Pearson correlation measures linear relationship between two variables, from -1 to +1. The heatmap shows which
#    features relate to fare (distance has the highest).
# Q: What is multicollinearity?
# A: Highly correlated input features, which make linear regression coefficients unstable.
# Q: Why extract hour, weekday, month, year from pickup_datetime?
# A: Models cannot use raw timestamps; these capture rush hour, weekend and yearly price effects.
# Q: Why drop null values / the "key" and "Unnamed" columns?
# A: Missing values break the models; key/index columns carry no predictive information.
# Q: Why split into train and test sets? What is random_state?
# A: To measure performance on unseen data (avoid overfitting). random_state makes the split reproducible.
# Q: What are overfitting and underfitting?
# A: Overfitting = good on train, poor on test (too complex). Underfitting = poor on both (too simple).
# Q: Is feature scaling needed?
# A: Not for random forest; for plain linear regression it is optional (it does not change predictions).
# Q: Important random forest hyperparameters?
# A: n_estimators, max_depth, min_samples_split, max_features. n_jobs=-1 uses all CPU cores.
# Q: Bagging vs boosting?
# A: Bagging trains trees independently in parallel and averages them; boosting trains sequentially, each tree fixing the
#    previous one's errors.
# Q: How can you check model robustness?
# A: K-fold cross-validation and comparing train vs test scores.
# Q: How does a regression tree split?
# A: Picks the feature/threshold that gives the largest reduction in variance (MSE) of the target.
