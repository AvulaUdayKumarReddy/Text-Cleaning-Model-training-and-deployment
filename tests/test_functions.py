import project3
file='AK Anchorage.pdf'
txt="Save earth, Save wildlife."
def test_load_file():
    data=project3.load_file(file)
    assert data is not None
    
def test_process_clean():
    data=project3.load_file(file)
    data=project3.process_clean(data)
    assert data['text_cleaned'] is not None
    
def test_lemm_txt():
    txt_data=project3.lemm_text(txt)
    assert txt_data is not None
    
def test_stemming():
    txt_data=project3.stemming(txt)
    assert txt_data is not None
    
def test_del_stopwords():
    txt_data=project3.delete_stopwords(txt)
    assert txt_data is not None
    