## Instructions
To run this project some python libraries are required. These are defined in *requirements.txt*.

The recommended way to install them is to use *conda*, or *pip*, and virtual environments.

##### Installing with conda


With Anaconda installed, execute the following in a anaconda command prompt :

1. Change to this project's folder
	
	`$ cd "path/to/folder"`

2. Create a virtual environment.

	`$ conda create -y --name env-name`

3. Activate your new environment.

	`$ conda activate env-name`

4. Install the required libraries.

	`$ conda install --force-reinstall -y --name env-name -c conda-forge --file requirements.txt`


##### Installing with pip

With Python 3+ and *pip* installed, execute the following in a command prompt :

1. Change to this project's folder
	
	`$ cd "path/to/folder"`
2. Create a virtual environment.

	`$ py -m venv env-name`

3. Activate your new environment.

	`$ .\env-name\Scripts\activate`

4. Install the required libraries.

	`$ pip install -r requirements.txt`

Using *conda* is preferred, *pip* may fail to install some libraries like *shap* if some microsoft visual studio resources are not already installed.

### Executing Notebooks

Once you have the libraries installed you can edit the source code and interact with the notebooks yourself.

To open the notebooks, with the virtual environment activated, in this project's folder, execute:

    $ jupyter notebook

This should open a browser tab in which you can select and run the notebooks.

## Notebooks

### Data Analisys (1_notebook)

The initial notebooks are for data exploration, they explore the data's quality and help to understand the features's overall distribution before going into predictions.

### Model (2_notebook)
Here the model is built, tested and interpreted. The steps are explained and logically organized. 

## Rerunning the prediction
It is possible to rerun the prediction process step by step. 

To do so, trough the notebook IDE in notebook #2:

1. Restart the kernel, keeping only markdowns and source code:
	

		Go to Kernel > Restart & Clear Outputs
	
2. Start executing cells:
		

		Click '>| Run' to execute selected cell's source code

### Testing different models

The notebook is designed as to allow for the easy testing of different models. 

With little code edits it is possible to perform feature and classifier selection.  

##### Feature selection
To test the impact of feature selection, edit Cell 3, taking features in and out of the corresponding list.

##### Classifier selection
To use a different classifier import it from scikit's module and use it as *clf*, like so:

	from sklearn.ensemble import RandomForestClassifier
	clf = RandomForestClassifier()

When defining the classifier it is also possible to use different hyper-parameters, using its optional arguments.

This way, with little programming experience, one can build, test and validate its own models and get a good grasp of the machine learning workflow.