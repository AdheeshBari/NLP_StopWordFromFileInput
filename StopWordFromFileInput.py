import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Download the NLTK data files (only the first time you run this program)
nltk.download('punkt')
nltk.download('stopwords')

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()  
    
    sentence_tokens = sent_tokenize(file_content)
    word_tokens = word_tokenize(file_content)
    stop_words = set(stopwords.words('english'))
    
    filtered_word_tokens = [word for word in word_tokens if word.lower() not in stop_words]
    removed_stop_words = [word for word in word_tokens if word.lower() in stop_words]
    
    print("Sentence Tokens:\n", sentence_tokens)
    print("Word Tokens:\n", word_tokens)
    print("Filtered Word Tokens (without stop words):\n", filtered_word_tokens)
    print("Removed Stop Words:\n", removed_stop_words)


# Output:
# Enter the path to the file: Exp2 StpWrd.txt
# Sentence Tokens: 
#  ['Lorem Ipsum is simply dummy text of the printing and typesetting industry.', "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.", 'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.', 'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.']
# Word Tokens:
#  ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'has', 'been', 'the', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s', ',', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book', '.', 'It', 'has', 'survived', 'not', 'only', 'five', 'centuries', ',', 'but', 'also', 'the', 'leap', 'into', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'It', 'was', 'popularised', 'in', 'the', '1960s', 'with', 'the', 'release', 'of', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages', ',', 'and', 'more', 'recently', 'with', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'of', 'Lorem', 'Ipsum', '.']   
# Filtered Word Tokens (without stop words):
#  ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', '1500s', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book', '.', 'survived', 'five', 'centuries', ',', 'also', 'leap', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'popularised', '1960s', 'release', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages', ',', 'recently', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'Lorem', 'Ipsum', '.']
# Stop Words are:
#  {'these', 'nor', "doesn't", 'here', 'an', 'doing', 'ain', 'their', 'out', 'again', 'shouldn', 'mustn', 'more', "mustn't", "you'd", 'isn', "haven't", "wasn't", 'now', 'hers', 'that', 'about', 'before', 'didn', 'at', 'and', 'you', 'as', 'not', "aren't", 'doesn', 'on', 'of', 'ourselves', "won't", 'ours', 'both', 'down', 'haven', 'which', 're', 'so', 'such', 'y', 'into', 'hadn', 'no', 'all', 'needn', 'those', 'him', 'wouldn', "you'll", 'yourself', 'who', 'he', 'than', "you've", 'himself', 'herself', "couldn't", 't', "weren't", "hasn't", 'did', 'her', 'being', 'aren', 'can', 'but', 'i', 'was', "isn't", 'it', 'yourselves', 'when', 'then', 'from', 'few', "hadn't", 'just', 'is', 'while', 'theirs', 'to', 'only', "it's", "she's", 'most', 'some', 'them', 'this', 'too', "needn't", 've', 'your', 'once', 'further', 'don', 'a', 'between', 'through', 'having', 'll', 'above', 'what', 'had', 'the', 'in', "should've", 'm', 'there', 'couldn', 'off', 'am', 'until', 'after', 'same', "don't", 'weren', 'if', 'yours', "that'll", 'o', 'are', 'd', 'our', "didn't", 'have', 'by', 'any', 'myself', 'why', 'how', 'with', 'up', 'other', 'won', 'whom', 'should', 'its', 'shan', 'they', 'we', 'for', 'ma', 'itself', 's', "shouldn't", 'below', 'because', "shan't", 'been', "wouldn't", 'each', 'be', 'under', 'will', 'his', "you're", 'mightn', 'very', 'were', 'or', 'over', 'during', 'hasn', 'against', 'has', 'own', "mightn't", 'does', 'do', 'she', 'wasn', 'my', 'themselves', 'where', 'me'}