# Datathon

**What the Project Does**

This project provides an automated solution for text cleaning and named entity extraction. It processes large datasets of unstructured text (e.g., news_exerpts_parsed.xlsx or wikileaks_parsed.xlsx), ensuring consistency in cleaning by removing stopwords, lemmatizing words, and identifying meaningful entities. Beyond simple keyword extraction, the project uses dependency parsing and named entity recognition (NER) to identify relationships between entities.

**Why is this project useful?**

🔹It helps to extract entities and relationship from unstructured data efficiently, making it easier for users to understand and derive insights from large datasets
  
**How can user get started?**

🔹 Firstly, users will have to install the required libraries, pandas, spacy, nltk and ensure that the modules from the respective libraries are installed. 

🔹From NLTK, users have to ensure that modules nltk.corpus and nltk.stem.wordnet are installed.

🔹From spaCy, users have to ensure that en_core_web_sm is installed.

🔹To conduct installation, users have to go to Command Line Prompt and run 'pip install [library name]' and to download the modules, users have to run 'python -m [library name]download [module name]'

🔹If the installation does not work on Command Line prompt, users can use Anaconda Prompt and run "conda install [library name]". To install the respective modules, they can run 'python -m [library name] download [module name]'.

🔹After the relevant installation is completed, users can load their dataset into our tool and must ensure their dataset are in excel format. After running their datasets using our tool, users can use tools like Tableau to analyse and visualise the insights extracted from their data. 

To get help with the project, users can use the discussion forum for community support.

This project is maintained by The Data Crew
