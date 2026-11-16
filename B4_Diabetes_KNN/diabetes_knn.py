import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df = pd.read_csv("diabetes.csv")
X, y = df.drop(columns="Outcome"), df["Outcome"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()  # KNN is distance-based, so scale features
X_train, X_test = scaler.fit_transform(X_train), scaler.transform(X_test)

pred = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train).predict(X_test)
acc = accuracy_score(y_test, pred)
print("Confusion matrix:\n", confusion_matrix(y_test, pred))
print("Accuracy:", acc)
print("Error rate:", 1 - acc)
print("Precision:", precision_score(y_test, pred))
print("Recall:", recall_score(y_test, pred))


# ======================= VIVA QUESTIONS =======================
# Q: What is the problem type?
# A: Binary classification - diabetic (Outcome = 1) or not (0). Dataset: Pima Indians diabetes.
# Q: Explain the KNN algorithm step by step.
# A: 1) Choose k. 2) Compute the distance from the test point to every training point. 3) Take the k nearest.
#    4) Predict the majority class among them.
# Q: Why is KNN a lazy, non-parametric learner?
# A: No training phase and no assumption about data distribution; it memorizes the training set.
# Q: Distance metrics?
# A: Euclidean (default), Manhattan, Minkowski (generalization), Hamming for categorical data.
# Q: How to choose k?
# A: Plot error vs k or use cross-validation; odd k avoids ties. k=1 overfits, very large k underfits.
# Q: Why scale the features?
# A: KNN uses distances, so large-valued features (Insulin, Glucose) would dominate small ones (Pregnancies).
# Q: Define confusion matrix.
# A: [[TN, FP], [FN, TP]] - counts of correct and incorrect predictions for each class.
# Q: Formulas: accuracy, error rate, precision, recall, F1?
# A: Accuracy = (TP+TN)/total; Error rate = 1 - accuracy = (FP+FN)/total; Precision = TP/(TP+FP);
#    Recall = TP/(TP+FN); F1 = 2PR/(P+R).
# Q: Which metric is more important for diabetes prediction?
# A: Recall - missing a diabetic patient (false negative) is more harmful than a false alarm.
# Q: Precision vs recall?
# A: Precision = of predicted positives, how many are correct. Recall = of actual positives, how many were found.
# Q: Disadvantages of KNN?
# A: Slow prediction on large data (O(n*d) per query), memory heavy, sensitive to scaling, irrelevant features
#    and the curse of dimensionality.
# Q: What data issues exist in diabetes.csv?
# A: Zeros in Glucose, BloodPressure, SkinThickness, Insulin, BMI are invalid (missing) - replace by median/mean.
# Q: What is weighted KNN?
# A: Closer neighbours get more vote weight (weights="distance").
# Q: Can KNN be used for regression?
# A: Yes - average the target values of the k neighbours.
# Q: Why use stratify in train_test_split (improvement)?
# A: Keeps the class ratio the same in train and test.
# Q: What is overfitting in KNN?
# A: A small k (like 1) follows noise in the training set; high variance.
# Q: Time complexity of prediction?
# A: O(n*d) per sample for brute force; KD-tree / ball tree can speed it up.
