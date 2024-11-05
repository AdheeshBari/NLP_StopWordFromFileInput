# NLP_StopWordFromFileInput
This script reads text from a file, tokenizes it into sentences and words, removes English stop words, and displays the filtered tokens and removed stop words.

This Python script reads text from a specified file, tokenizes it into sentences and words, and removes English stop words, displaying the filtered tokens and removed stop words.
Steps:
1. Library Setup: Downloads necessary NLTK data files (punkt for tokenization and stopwords for filtering).
2. File Reading: Prompts the user to enter the file path and reads the file content using UTF-8 encoding.
3. Tokenization: Tokenizes the file content into sentences and words with sent_tokenize and word_tokenize.
4. Stop Word Filtering: Defines English stop words and filters them out from the word tokens. Outputs both the filtered word tokens (without stop words) and the removed stop words for analysis.
Examples: For given file content, the script outputs sentence tokens, word tokens, filtered tokens, and removed stop words to illustrate its functionality.
This code is useful for basic text preprocessing in Natural Language Processing (NLP) tasks.
