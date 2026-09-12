
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv(
    "ml/all-data.csv",
    encoding="latin-1",
    header=None,
    names=["sentiment", "text"]
)


# ============================================================
# X AND y
# ============================================================

X = df["text"]
y = df["sentiment"]


# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ============================================================
# TF-IDF
# ============================================================

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)


X_train_tfidf = vectorizer.fit_transform(X_train)

X_test_tfidf = vectorizer.transform(X_test)


# ============================================================
# LOGISTIC REGRESSION
# ============================================================

model = LogisticRegression(
    max_iter=1000
)


model.fit(
    X_train_tfidf,
    y_train
)


# ============================================================
# PREDICTION
# ============================================================

y_pred = model.predict(
    X_test_tfidf
)


# ============================================================
# ACCURACY
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(
    f"Accuracy: {accuracy:.4f}"
)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# ============================================================
# CONFUSION MATRIX
# ============================================================

print("\nConfusion Matrix:\n")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


# ============================================================
# SAVE MODEL
# ============================================================

joblib.dump(
    model,
    "ml/sentiment_model.pkl"
)


joblib.dump(
    vectorizer,
    "ml/tfidf_vectorizer.pkl"
)


print("\nModel saved successfully.")

print(
    "Saved: ml/sentiment_model.pkl"
)

print(
    "Saved: ml/tfidf_vectorizer.pkl"
)

