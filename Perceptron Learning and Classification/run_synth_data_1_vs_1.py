"""run_2_class_2_feature_iris_data.py
YOU SHOULD NOT NEED TO EDIT THIS FILE OR TURN IT IN.
HOWEVER, YOU ARE WELCOME TO EDIT THE FILE TO EXPLORE
POSSIBLE ADJUSTMENTS TO PARAMETERS.

Train a perceptron on the first 10 examples of iris setosa
and the first 10 examples of iris versicolor, considering
only sepal length and petal length as features.

Then test with the remaining 40 examples of each.
Extends the Class PlotBinaryPerceptron

Version 1.1, Prashant Rangarajan and S. Tanimoto, May 11, 2021. Univ. of Washington.
"""

from binary_perceptron import BinaryPerceptron  # Your implementation of binary perceptron
from plot_bp import PlotBinaryPerceptron
import csv  # For loading data.
from matplotlib import pyplot as plt  # For creating plots.


class PlotMultiBPOneVsAll(PlotBinaryPerceptron):
    """
    Plots the Binary Perceptron after training it on the Iris dataset
    ---
    Extends the class PlotBinaryPerceptron
    """

    def __init__(self, bp, plot_all=False, n_epochs=50):
        super().__init__(bp, plot_all, n_epochs)  # Calls the constructor of the super class
        self.CLASSES = (1, 2)

    def read_data(self):
        """
        Read data from the Iris dataset with 2 features and 2 classes
        for both training and testing.
        ---
        Overrides the method in PlotBinaryPerceptron
        """
        data_as_strings = list(csv.reader(open('synthetic_data.csv'), delimiter=','))
        new_data = []
        for i in range(len(data_as_strings)):
            if int(data_as_strings[i][-1]) == self.CLASSES[0] or int(data_as_strings[i][-1]) == self.CLASSES[1]:
                new_data.append(data_as_strings[i])

        self.TRAINING_DATA = [[float(f1), float(f2), int(c)] for [f1, f2, c] in list(new_data)]
        for i in range(len(self.TRAINING_DATA)):
            if self.TRAINING_DATA[i][-1] == self.CLASSES[0]:
                self.TRAINING_DATA[i][-1] = 1
            elif self.TRAINING_DATA[i][-1] == self.CLASSES[1]:
                self.TRAINING_DATA[i][-1] = -1


    def plot(self):
        """
        Plots the dataset as well as the binary classifier
        ---
        Overrides the method in PlotBinaryPreceptron
        """
        plt.title(f"Plot with class {self.CLASSES[0]} and {self.CLASSES[1]}")
        plt.legend(loc='best')
        plt.show()


if __name__ == '__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5)
    pbp = PlotMultiBPOneVsAll(binary_perceptron)
    pbp.train()
    pbp.plot()

