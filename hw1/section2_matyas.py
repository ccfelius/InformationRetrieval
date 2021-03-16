def build_tf_index(documents):
    """
        Build an inverted index (with counts). The output is a dictionary which takes in a token
        and returns a list of (doc_id, count) where 'count' is the count of the 'token' in 'doc_id'
        Input: a list of documents - (doc_id, tokens)
        Output: An inverted index. [token] -> [(doc_id, token_count)]
    """
    inv_index = {}

    for document in documents:
        # Create dict to store token info for this document
        hashtable = {}
        doc_id = int(document[0])
        # Go through all tokens and count them
        for token in document[1]:
            # Initialize or increase count
            if token not in hashtable:
                hashtable[token] = 0
            hashtable[token] += 1
        # Go through tokens and append their count to the index
        for token, count in hashtable.items():
            if token not in inv_index:
                inv_index[token] = []
            inv_index[token].append((doc_id, count))
    return inv_index
