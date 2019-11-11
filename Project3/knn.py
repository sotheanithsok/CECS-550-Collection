import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
pd.set_option('display.max_rows', None)


class KNN(object):
    def __init__(self):
        pass

    def load_data(self):
        data = pd.read_csv(
            "./prompts/wine_quality.csv",
            skiprows=14,
            header=None,
            names=[
                "fa",
                "va",
                "ca",
                "rs",
                "chlor",
                "fsd",
                "tsd",
                "density",
                "pH",
                "sulphates",
                "alcohol",
                "quality",
            ],
        )

        data = data.fillna(value = 0)

        x = data.drop(columns=["quality"])
        y = data["quality"]
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            x, y, test_size=0.2
        )
        pass

    def run(self):
        self.model = KNeighborsClassifier(n_neighbors=5, weights="distance")
        self.model.fit(self.x_train, self.y_train)
        accuracy = self.model.score(self.x_test, self.y_test)
        predicted_result = self.model.predict(self.x_test)
        print(pd.DataFrame({"predicted_result":predicted_result, "expected_result":self.y_test}))
        print(accuracy)
        pass


m=KNN()
m.load_data()
m.run()