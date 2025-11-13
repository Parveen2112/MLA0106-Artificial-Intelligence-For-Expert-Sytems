from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=1)

model = DecisionTreeClassifier(criterion='entropy')
model.fit(Xtr, ytr)

print(export_text(model))
print("Accuracy:", accuracy_score(yte, model.predict(Xte)))
