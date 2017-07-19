def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!

    # 19. GaussianNB Deployment on Terrain Data

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    return clf

    # 20. Calculating NB Accuracy
    from sklearn.metrics import accuracy_score
    print(accuracy_score(pred, lables_test))
