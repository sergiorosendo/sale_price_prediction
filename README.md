## Source Code
This project is built with Python 3.7.

For better code modularization and to maintain intuitive and concise notebooks, most of this project's source code is contained in the 'src' folder. Required functions are imported right before usage and their design can be explored in the respective source file.

## Requirements
To interact with and edit the notebooks, Python, Jupyter Notebook, and the following libraries are necessary: 

	- scikit-learn
	- pandas
	- numpy
	- seaborn

The easiest way to install the requirements is to install Anaconda, available at https://www.anaconda.com/distribution/. Once installed the user can execute the notebooks trough bash. 

Alternatively, they can be installed with pip-tools, available in https://pypi.org/project/pip-tools/.
To install a python library, execute the following command in a shell prompt:

	$ pip install <library_name>
	example: $ pip install pandas

## Notebooks

### Data Analisys (1_notebook)

The initial notebooks are for data exploration, they explore the data's quality and help to understand the features's overall behavior before going into predictions.

### Model (2_notebook)
Here the model is built, tested and interpreted. The building steps are logically organized and explained as they happen. The final steps measure the model performance and interpret its results.


## Building and executing models
Executing the '2_notebook', it is possible to go trough the prediction process step by step, from building the model to testing its outcome. 

To do so, trough the notebook IDE:

	-> Kernel
		-> Restart & Clear Outputs 
		# This will restart the notebook keeping only its markdowns and source code
	-> Select the first cell and starting clicking '>| Run'
	# Clicking '>| Run' executes the selected cell's source code

### Testing different models
The project is organized as to allow for easy and quick testing of different models. This is possible due to the code modularization and the usage of advanced tools like sklearn's pipelines, which speed up the prediction's workflow.

Among the classifiers tested during development, Linear Regression was the one that had the best performance and, thus, was the one kept in the final version. 

If the user has some coding experience, it is able explore the outcome to different models, editing the classifier and/or features used.

#### Classifier selection
To test Random Forest for instance, one needs only to edit the corresponding lines in cell number 5:

	from sklearn.ensemble import RandomForestClassifier
	clf = RandomForestClassifier()

One will notice that the Random Forest does not generate so great results, but it could be improved by hard-tweaking its parameters.

#### Feature selection
To test the impact of feature selection, edit Cell 3, taking features in an out of the corresponding list.

For instance, including or excluding latitude, longitude and zip codes, there's a noticeable impact in the prediction's performance.
