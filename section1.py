# TODO: Implement this! (4 points)
def read_cacm_docs(root_folder = "./datasets/"):
    """
        Reads in the CACM documents. The dataset is assumed to be in the folder "./datasets/" by default
        Returns: A list of 2-tuples: (doc_id, document), where 'document' is a single string created by 
            appending the title and abstract (separated by a "\n"). 
            In case the record doesn't have an abstract, the document is composed only by the title
    """
    f = open(root_folder+"cacm.all", "r")
    entries = [] 
    document = ""
    doc_id = ""
    doc = ()
    for line in f:
        if line.startswith(".I"):
            doc_id = line.strip(" .I\n")
        elif line.startswith(".T"):                            
            
            # skip to the next line 
            document = next(f).strip()    
            following = ""
            
            # process the title and abstract with seperate requirements 
            while not(following.startswith(".B")):
                if ".W" in document:
                    following = following.replace("\n", " ")
                document += " "+ following
                following = next(f)  
            document = document.replace(".W", "").replace("\n \n"," ").strip()
        
        # if unique, add tuple to list 
        elif doc and doc not in entries: 
            entries.append(tuple((doc_id, document)))
        doc = tuple((doc_id, document))  
    f.close()
    return entries 

# TODO: Implement this! (3 points)
def read_queries(root_folder = "./datasets/"):
    """
        Reads in the CACM queries. The dataset is assumed to be in the folder "./datasets/" by default
        Returns: A list of 2-tuples: (query_id, query)
    """
    f = open(root_folder+"query.text", "r")
    queries = [] 
    query = ""
    query_id = ""
    doc = ()
    for line in f:
        if line.startswith(".I"):
            query_id = line.strip(" .I\n")
        elif line.startswith(".W"):

            # skip to the next line 
            query = next(f).strip()    
            following = ""

            # check for long queries 
            while not(following.startswith(".N")):
                query += " "+ following.strip()
                following = next(f)    
            query.strip()

        # add tuple to list if unique 
        elif doc and doc not in queries: 
            queries.append(tuple((query_id, query)))
        doc = tuple((query_id, query))  
    f.close()
    return queries 

# TODO: Implement this! (1 point)
def load_stopwords(root_folder = "./datasets/"):
    """
        Loads the stopwords. The dataset is assumed to be in the folder "./datasets/" by default
        Output: A set of stopwords
    """
    f = open(root_folder+"common_words", "r")
    common_words = set()
    for word in f: 
        word = word.strip().lower()
        common_words.add(word)   
    f.close()
    return common_words 

# TODO: Implement this! (4 points)
def tokenize(text):
    """
        Tokenizes the input text. Use the WordPunctTokenizer
        Input: text - a string
        Output: a list of tokens
    """ 
    tokens = nltk.WordPunctTokenizer().tokenize(text)
    return tokens

# TODO: Implement this! (3 points)
def stem_token(token):
    """
        Stems the given token using the PorterStemmer from the nltk library
        Input: a single token
        Output: the stem of the token
    """
    ps = nltk.PorterStemmer() 
    stem_token = ps.stem(token)
    return stem_token
