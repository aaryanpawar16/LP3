import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# emails.csv: "Email No." + word-count columns + "Prediction" (1 = spam)
df = pd.read_csv("emails.csv")
X, y = df.drop(columns=["Email No.", "Prediction"]), df["Prediction"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for name, model in {"KNN": KNeighborsClassifier(n_neighbors=5), "SVM": SVC(kernel="linear")}.items():
    pred = model.fit(X_train, y_train).predict(X_test)
    print(f"\n=== {name} ===")
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred))


# ======================= VIVA QUESTIONS =======================
# Q: What type of problem is spam detection?
# A: Binary classification (spam = 1, not spam = 0), supervised learning.
# Q: How is the email represented?
# A: Bag-of-words: each column is a word and each cell is the word's count in that email.
# Q: Explain the KNN algorithm.
# A: Store all training data; for a new point, find the k nearest points (Euclidean distance) and take a majority vote.
# Q: Why is KNN called a lazy learner?
# A: It does no training - all computation happens at prediction time.
# Q: How do you choose k?
# A: Try several values and pick the one with the best validation accuracy; use odd k to avoid ties.
#    Small k -> overfits (noisy); large k -> underfits (too smooth).
# Q: Explain SVM.
# A: Finds the hyperplane that separates classes with the maximum margin; the closest points are the support vectors.
# Q: What are support vectors and margin?
# A: Support vectors = training points closest to the boundary that define it; margin = distance between the boundary and them.
# Q: What is the kernel trick? Kernel types?
# A: Implicitly maps data to a higher dimension so non-linear data becomes separable. Linear, polynomial, RBF, sigmoid.
# Q: Why use a linear kernel here?
# A: Text data has many features (high-dimensional, sparse) and is usually linearly separable.
# Q: What do parameters C and gamma do?
# A: C = penalty for misclassification (large C -> narrow margin, overfit); gamma = reach of a single point for RBF.
# Q: Define confusion matrix, TP, FP, TN, FN.
# A: Table of actual vs predicted. TP = spam caught; FP = good mail flagged as spam; TN = good mail passed;
#    FN = spam missed.
# Q: Accuracy, precision, recall, F1?
# A: Accuracy = (TP+TN)/all; Precision = TP/(TP+FP); Recall = TP/(TP+FN); F1 = harmonic mean of precision and recall.
# Q: Which metric matters most for spam filtering?
# A: Precision - a false positive (a real mail lost) is worse than letting some spam through.
# Q: KNN vs SVM comparison?
# A: KNN: simple, no training, slow prediction, sensitive to scaling and the curse of dimensionality.
#    SVM: slower to train, fast prediction, works well in high dimensions.
# Q: What is the curse of dimensionality?
# A: In many dimensions, distances become less meaningful, so KNN degrades.
# Q: What if the dataset is imbalanced?
# A: Accuracy misleads; use precision/recall/F1, resampling (SMOTE) or class weights.
# Q: Other methods for spam?
# A: Naive Bayes (classic), logistic regression, TF-IDF features, deep learning.
# Q: How can you improve the models?
# A: Hyperparameter tuning (GridSearchCV), feature scaling/selection, TF-IDF, cross-validation.
# Q: Why split data into train and test?
# A: To evaluate on unseen data and detect overfitting.
