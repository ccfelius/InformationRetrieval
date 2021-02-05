# TODO: Implement this! (10 points)
def build_tf_index(documents):
    """
        Build an inverted index (with counts). The output is a dictionary which takes in a token
        and returns a list of (doc_id, count) where 'count' is the count of the 'token' in 'doc_id'
        Input: a list of documents - (doc_id, tokens) 
        Output: An inverted index. [token] -> [(doc_id, token_count)]
    """
#     from collections import defaultdict
#     inv_index = default(dict)

    if isinstance(documents, list):
        hashtable = dict()
        inv_index = dict()
        
        for document in documents:
            doc_id = int(document[0])
            for token in document[1]: 
                
                # create element for dictionary 
                if token not in hashtable:
                    hashtable[token] = list() 
                    count = 0 
                count += 1 
                tk = tuple((doc_id, count))
                hashtable[token].append(tk)
                inv_index[token] = hashtable[token]
        return inv_index[token]
    raise NotImplementedError()