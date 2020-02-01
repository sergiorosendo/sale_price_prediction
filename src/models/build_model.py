from sklearn.pipeline import Pipeline

def build_model(preprocessor, classifier):

    model = Pipeline([
        ('preprocess', preprocessor),
        ('classify', classifier)
    ])

    return model