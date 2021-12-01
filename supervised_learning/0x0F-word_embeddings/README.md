# Natural Language Processing - Word Embeddings 


### What is natural language processing?
 Natural Language Processing, or NLP for short, is broadly defined as the automatic manipulation of natural language, like speech and text, by software.
 in particular how to program computers to process and analyze large amounts of natural language data. The result is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves.

###  What is a word embedding?

Word embeddings are a type of word representation that allows words with similar meaning to have a similar representation.
A bag-of-words model, or BoW for short, is a way of extracting features from text for use in modeling, such as with machine learning algorithms.
![alt text](https://miro.medium.com/max/700/1*hLvya7MXjsSc3NS2SoLMEg.png)

 
### What is TF-IDF?
 tf–idf, TF*IDF, or TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus
 tf = number of repetition of word in sentence / total number of words in in the same sentence
 idf = log (sum of  all sentences/ sum number of  all sentences containing the word)
### What is CBOW?
The CBOW model architecture tries to predict the current target word (the center word) based on the source context words (surrounding words).
### What is a skip-gram?
Skip-gram is one of the unsupervised learning techniques used to find the most related words for a given word.
Skip-gram is used to predict the context word for a given target word. It’s reverse of CBOW algorithm. Here, target word is input while context words are output.
### What is an n-gram?
an n-gram is a contiguous sequence of n items from a given sample of text or speech. The items can be phonemes, syllables, letters, words or base pairs according to the application. The n-grams typically are collected from a text or speech corpus. When the items are words, n-grams may also be called shingles.

![alt text](https://i.stack.imgur.com/8ARA1.png)
### What is negative sampling?
Negative sampling allows us to only modify a small percentage of the weights, rather than all of them for each training sample. We do this by slightly modifying our problem.
### word2vec
Word2Vec is a better successor to the neural probabilistic model. We still use a statistical computation method to learn from a text corpus, however, its method of training is more efficient than just simple embedding training. It is more or less the standard method for training embeddings the days.
use :
* Continuous Bag-of-Words (CBOW)
* Continuous Skip-Gram

### GloVe
GloVe is also a very popular unsupervised algorithm for word embeddings that is also based on distributional hypothesis – “words that occur in similar contexts likely have similar meanings”.

GloVe learns a bit differently than word2vec and learns vectors of words using their co-occurrence statistics.
### FastText
Now, with FastText we enter into the world of really cool recent word embeddings. What FastText did was decide to incorporate sub-word information. It did so by splitting all words into a bag of n-gram characters (typically of size 3-6). It would add these sub-words together to create a whole word as a final feature. The thing that makes this really powerful is it allows FastText to naturally support out-of-vocabulary words!

## what i learned from this chapter

-    What is natural language processing?
-    What is a word embedding?
-    What is bag of words?
-    What is TF-IDF?
-    What is CBOW?
-    What is a skip-gram?
-    What is an n-gram?
-    What is negative sampling?
-   What is word2vec, GloVe, fastText, ELMo?

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)