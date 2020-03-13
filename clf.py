import os
import joblib

from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer

# scoring in anything
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import f1_score, matthews_corrcoef
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import confusion_matrix

from NewsClf.utils import load_data

PICKLE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pickles", "clf.pkl")


def train(X, Y):
    # Building the Random Forest Classifier (RANDOM FOREST) , Logistic Regression , LinearSVC
    clfs = [RandomForestClassifier(), LogisticRegression(), LinearSVC()]#n_estimators=500 for random forst
    best_f1 = 0
    best_clf = None
    # dividing the X and the Y from the dataset
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.2)

    for clf in clfs:
        print(f"training clf {clf}")
        clf = Pipeline([('clf', clf)])
        clf.fit(x_train, y_train)

        f1 = f1_score(y_test, clf.predict(x_test), average='micro')
        print(f"clf {clf} has f1 score of {f1}")
        if f1 > best_f1:
            best_f1 = f1
            best_clf = clf
    print(f"trained with best f1 of {best_f1} \n\n")

    # get scores information
    # scores(y_test, clf.predict(x_test), average='micro',classfire_name)

    return best_clf


# printing every score of the classifier
def scores(yTest, yPred, average,classfire_name):
    print(f"The model used is {classfire_name}")

    acc = accuracy_score(yTest, yPred, average)
    print("The accuracy is {}".format(acc))

    prec = precision_score(yTest, yPred, average)
    print("The precision is {}".format(prec))

    rec = recall_score(yTest, yPred, average)
    print("The recall is {}".format(rec))

    f1 = f1_score(yTest, yPred)
    print("The F1-Score is {}".format(f1))

    MCC = matthews_corrcoef(yTest, yPred, average)
    print("The Matthews correlation coefficient is{}".format(MCC))

    CFR = classification_report(yTest, yPred)
    print("The Classification Report is{}".format(MCC))

    print("\n\n")

def save_model(clf):
    joblib.dump(clf, PICKLE_DIR, True)


def load_model():
    return joblib.load(PICKLE_DIR)


def run():
    # load the data
    X, Y = load_data()
    clf = train(X, Y)
    save_model(clf)
    print("clf trained !!")
