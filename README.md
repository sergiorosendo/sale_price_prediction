## Instructions
To run this project some python libraries are required. These are defined in *requirements.txt*.

The recommended way to install them is to use pip and virtual environments.

With Python 3+ and pip installed, execute the following in a command prompt :

1. Change to this project's folder
	
	`$ cd "path_to_folder"`
2. Create a virtual environment.

	`$ py -m venv env-name`

3. Activate your new environment.

	`$ .\env-name\Scripts\activate`

4. Install the required libraries.

	`pip install -r requirements.txt`

Once you have the libraries installed you can edit the source code and interact with the notebooks yourself.

To execute the notebooks, with your virtual environment activated, execute:

	$ jupyter notebook

This should open a browser tab in which you can select and run the notebooks.

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

#### Classifier selection
To test Random Forest for instance, one needs only to edit the corresponding lines in cell number 5:

	from sklearn.ensemble import RandomForestClassifier
	clf = RandomForestClassifier()

One will notice that the Random Forest does not generate great results, but it could be improved by hard-tweaking its parameters with a grid search.

#### Feature selection
To test the impact of feature selection, edit Cell 3, taking features in an out of the corresponding list.

For instance, including/excluding latitude, longitude and zip codes, noticeably impacts the model's performance.
