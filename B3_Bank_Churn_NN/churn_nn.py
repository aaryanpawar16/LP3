import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv("Churn_Modelling.csv").drop(columns=["RowNumber", "CustomerId", "Surname"])
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)  # encode categoricals
X, y = df.drop(columns="Exited").astype("float32"), df["Exited"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train, X_test = scaler.fit_transform(X_train), scaler.transform(X_test)  # fit on train only

model = Sequential([Dense(16, activation="relu", input_shape=(X_train.shape[1],)),
                    Dense(8, activation="relu"),
                    Dense(1, activation="sigmoid")])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])  # Adam = optimizer
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=0)

pred = (model.predict(X_test) > 0.5).astype(int)
print("Accuracy:", accuracy_score(y_test, pred))
print("Confusion matrix:\n", confusion_matrix(y_test, pred))


# ======================= VIVA QUESTIONS =======================
# Q: What is the problem type?
# A: Binary classification - will the customer leave the bank (Exited = 1) or stay (0).
# Q: What is an artificial neural network?
# A: Layers of connected neurons; each computes a weighted sum of inputs + bias and passes it through an activation function.
# Q: What do the layers in your model do?
# A: Dense(16, relu) and Dense(8, relu) are hidden layers that learn features; Dense(1, sigmoid) outputs the churn probability.
# Q: What is an activation function? Why ReLU and sigmoid?
# A: Adds non-linearity. ReLU = max(0, x): fast, avoids vanishing gradients (hidden layers).
#    Sigmoid squashes to 0-1, ideal for a binary probability (output layer).
# Q: What is the loss function used?
# A: Binary cross-entropy - suitable for 2-class problems with sigmoid output.
# Q: What is an optimizer? What is Adam?
# A: Updates the weights to reduce the loss. Adam = adaptive learning rate + momentum; fast and works well by default.
# Q: What is backpropagation and gradient descent?
# A: Backprop computes the gradient of the loss w.r.t. each weight (chain rule); gradient descent moves weights against it.
# Q: Define epoch, batch size, iteration, learning rate.
# A: Epoch = one pass over all training data; batch size = samples per weight update; iteration = one batch update;
#    learning rate = step size of the update.
# Q: Why drop RowNumber, CustomerId, Surname?
# A: They are identifiers with no predictive value (and would add noise).
# Q: Why encode Geography and Gender? What is drop_first?
# A: Networks need numbers; get_dummies makes one-hot columns. drop_first removes one column to avoid the dummy variable trap
#    (perfect multicollinearity).
# Q: Why normalize/standardize the features?
# A: Features on different scales (Balance vs Age) slow or destabilize gradient descent. StandardScaler -> mean 0, std 1.
# Q: Why fit the scaler only on training data?
# A: To avoid data leakage - test data information must not influence preprocessing.
# Q: What does validation_split do?
# A: Holds out part of the training data to monitor performance on unseen data during training.
# Q: Why is accuracy alone not enough here?
# A: The data is imbalanced (~20% churn), so a model predicting "no churn" gets ~80% accuracy; check the confusion matrix,
#    precision, recall, F1, ROC-AUC.
# Q: Why threshold 0.5?
# A: Probability > 0.5 -> class 1. It can be tuned to trade precision against recall.
# Q: How can the model be optimized/improved?
# A: Tune layers/neurons/learning rate/epochs/batch size; add Dropout, L2 regularization, EarlyStopping; handle class imbalance.
# Q: What is overfitting and how do you prevent it?
# A: Model memorizes training data. Use dropout, early stopping, regularization, more data, a smaller network.
# Q: Sigmoid vs softmax?
# A: Sigmoid for binary (single output); softmax for multi-class (probabilities sum to 1).
# Q: What is the vanishing gradient problem?
# A: Gradients shrink through many sigmoid/tanh layers so early layers stop learning; ReLU helps.
# Q: Sequential vs Functional API in Keras?
# A: Sequential = simple linear stack of layers; Functional = complex graphs (multiple inputs/outputs, branches).
# Q: What is a Dense layer?
# A: A fully connected layer - every neuron is connected to all neurons in the previous layer.
# Q: How many parameters does the first layer have?
# A: (inputs x 16) + 16 biases.
