from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def train_all_models(X_train, y_train):
    models = {}

    models["Logistic Regression"] = LogisticRegression(
        max_iter=500, C=0.5
    )

    models["Decision Tree"] = DecisionTreeClassifier(
        max_depth=5, min_samples_split=50
    )

    models["Random Forest"] = RandomForestClassifier(
        n_estimators=50, max_depth=7, min_samples_split=50
    )

    models["SVM"] = SVC(
        C=0.5, kernel="rbf"
    )

    for model in models.values():
        model.fit(X_train, y_train)

    return models
