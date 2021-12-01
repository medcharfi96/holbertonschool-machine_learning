# 0x13. QA Bot
## Question Answering
For the Question Answering task, BERT takes the input question and passage as a single packed sequence. The input embeddings are the sum of the token embeddings and the segment embeddings. The input is processed in the following way before entering the model:
* Token embeddings: A [CLS] token is added to the input word tokens at the beginning of the question and a [SEP] token is inserted at the end of both the question and the paragraph.
* Segment embeddings: A marker indicating Sentence A or Sentence B is added to each token. This allows the model to distinguish between sentences. In the below example, all tokens marked as A belong to the question, and those marked as B belong to the paragraph.
![alt text](https://miro.medium.com/max/700/1*yUYAXoXumLQKpfdqRaeXsw.png)

To fine-tune BERT for a Question-Answering system, it introduces a start vector and an end vector. The probability of each word being the start-word is calculated by taking a dot product between the final embedding of the word and the start vector, followed by a softmax over all the words. The word with the highest probability value is considered.
A similar process is followed to find the end-word.
![alt text](https://miro.medium.com/max/700/0*A0TEfNg5p0xjQH78.png)

## Semantic Search
For asymmetric semantic search, you usually have a short query (like a question or some keywords) and you want to find a longer paragraph answering the query. An example would be a query like “What is Python” and you wand to find the paragraph “Python is an interpreted, high-level and general-purpose programming language. Python’s design philosophy …”. For asymmetric tasks, flipping the query and the entries in your corpus usually does not make sense.

## What i learned from  this chapter

- What is Question-Answering?
- What is Semantic Search?
- What is BERT?
- How to develop a QA chatbot
- How to use the transformers library
- How to use the tensorflow-hub library

## Author
* **Mouhamed Charfi** - [medcharfi96](https://github.com/medcharfi96)
