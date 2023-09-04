## The project that emphasizes text preprocessing, Traning the model and also deployment of that so that it can be used for prediction purposes.
## Text cleaning, Model Training and deployment 
##### Installation  
pyenv install 3.10.1  
pyenv global 3.10.1  
pip install --upgrade pip  
##### Running  
- pipenv shell
- python project3.py --document "AK Anchorage.pdf"
- pipenv run python -m pytest (to run test cases)
#### Packages   
- pytest            --used for testing
- pypdf             -- used for reading pdf files
- pandas            -- used for creating dataframes
- nltk              -- used for normalizing text and removing stopwords
- spacy             -- used for text  normalizing
- scikit-learn      -- implementing models
- numpy             -- shaping the arraya
- yellowbrick       -- finding optimal k

#### Folders
- tests --contains the test file "test_functions.py"

#### Recording
![](docs/TA_pj_3.gif)

#### Tree structure 
![]()

#### Assumptions and Considerations

I am keeping the sample PDF file in the current folder structure to test the prediction on the saved model that uploaded the model using the joblib file.
I also used "AK Anchorage.pdf" for testing prediction and also testing the functions.
Please do not remove the  "AK Anchorage.pdf" file as all the test functions are based on it, the test cases will fail if this file is not present.

#### Issues Expected

I have saved the dataframe to tab seperated file ,but since the data is huge, it difficult to track the data in file, so please consider for the evaluation purpose.

#### Important Files
- project3.py --contains the two functions that performs loading of file ,cleaning the data and predicting the new test data for model.

#### Functions in Project2.py

##### load_file(doc_name):

This function takes file name called from the main function and passes the file name, so the extracted from the pdf file using pdfreader of pypdf and data is stored in the data frame and return to calling function.

#####  process_clean(d):

This function takes the dictionary returned from the load file and performs some replacements of characters using the regex. In this functions there are calls for functions lemm_text(), stemming() and delete_stopwords()
and a data frame is returned to a calling function.

##### lemm_text(txt):

lemmatization is performed using spacy and some pronouns are removed using the spacy and the tst s returned.

##### stemming(text):

stemming is performed to normalize the text using the porterStemmer() function and text is returned to calling functon.

##### delete_stopwords(text, is_lower_case=False)

stop words are downloaded using nltk and all stop words are deleted using the nltk library and teext is returned to calling function.

#### Testing
- folder -tests
- file name- test_functions.py
- library used -pytest
#### NOTE : Please do not remove the "AK Anchorage.pdf" file in current folder, it is necessary to pass the test cases.
##### test_load_file()

tests the functionality of load_file in project3.py

##### test_process_clean()

tests the functionality od process clean function in project3.py

##### test_lemm_txt()

tests the functionality of lemm_text() function in project3.py

##### test_stemming()

test the functionality of stemming() function in project3.py

##### test_del_stopwords()

test the functionality of delete_stopwords() function in project3.py





