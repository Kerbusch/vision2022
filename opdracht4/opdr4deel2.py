import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100)
X, y = digits.data[:-10], digits.target[:-10]

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.33, random_state=44 )
clf.fit(X_train, y_train)  # train

y_predicted = list()
for i in range(len(X_test)):
    y_predicted.append(clf.predict(X_test[i:i+1])[0])

#print(y_predicted)
#print(y_test)

#print("prediction: {}".format(clf.predict(digits.data[-6:-5])))
print("accuracy_score: {}%".format(accuracy_score(y_test, y_predicted)*100))

#plt.imshow(digits.images[-6], cmap=plt.cm.gray_r, interpolation='nearest')
#plt.show()
