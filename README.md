# concept-suggestor
Takes concepts from models and suggests relevant and interesting ones to modelers.

## Install
1. Navigate to the root directory of the project. It should contain `requirements.txt`
2. Open an elevated command prompt.
    - If you want to use a virtual environment to install packages in, activate that now.
3. Run `pip install -r requirements1.txt`
4. Run `pip install -r requirements2.txt`
5. Install NumPy+mkl
	- These instructions are for Windows. If you're not on Windows, you'll have to Google around.
	- Navigate to http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
	- Select the version of Numpy+MLK appropriate for your Python version and OS. cp36-cp36m means Python 3.6.
	- Navigate to the download directory and open an elevated command prompt.
	- Run `pip install <filename>`
6. Install SciPy
	- This depends significantly on your OS and Python version.
	- First, try to run `pip install scipy`. If this works, you're done! If not and you're on Windows, follow the following instructions:
		- Navigate to http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
		- Select the version of SciPy appropriate to your Python version and OS. cp36-cp36m means Python 3.6.
		- Navigate to the download directory and open an elevated command prompt.
		- Run `pip install <filename>`
7. Run `python -m spacy download en_core_web_md`
8. Run `python -m nltk.downloader`
	- Navigate to the `Corpora` tab.
	- Install the `wordnet_ic` corpus.
9. Launch or open the project.
    - Run the `ConceptSuggestor\ConceptSuggestor.py` file to launch the program.
    - Open `ConceptSuggestor.sln` in Visual Studio to open the solution.

## Usage
Concept Suggestor has several options available for use.
When the program is opened, it shows a list of available options.

A variety of settings is contained in `settings.json`. 
If the `reload` value is set to `true`, you can change the settings in between operations.
The settings will be reloaded after the asks whether you want to try again.
