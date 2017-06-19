# concept-suggestor
Takes concepts from models and suggests relevant and interesting ones to modelers.

## Install
1. Navigate to the root directory of the project. It should contain `requirements.txt`
2. Open an elevated command prompt.
    - If you want to use a virtual environment to install packages in, activate that now.
3. Run `pip install -r requirements1.txt`
4. Run `pip install -r requirements2.txt`
5. Run `python -m spacy download en_core_web_md`
6. Launch or open the project.
    - Run the `ConceptSuggestor\ConceptSuggestor.py` file to launch the program.
    - Open `ConceptSuggestor.sln` in Visual Studio to open the solution.

## Usage
Concept Suggestor has several options available for use.
When the program is opened, it shows a list of available options.

A variety of settings is contained in `settings.json`. 
If the `reload` value is set to `true`, you can change the settings in between operations.
The settings will be reloaded after the asks whether you want to try again.
