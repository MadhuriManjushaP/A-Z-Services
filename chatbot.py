//building the chatbot(put # for commenting in python)



//importing the lib
import numpy as np
import tensorflow as tf
import re
import time


//importing the dataset
lines = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore' ).read().split('\n')
conversations = open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore' ).read().split('\n')

//creating a dictonary that maps each line an itsID

id2line = {}
for line in lines:
    _line = line.split( ' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]
        
//creating a List of every convo(only getting  IDS of all convo)
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split( ' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    conversations_ids.append(_conversation.split(','))


//getting question an answers seperately
questions = []
answers = []
for conversation in conversations_ids:
      for i in range(len(conversation) -1):
          questions.append(id2line[conversation[i]])
          answers.append(id2line[conversation[i+1]])
         
//Cleaning Process
//doing cleaning of texts
  def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
    return text

//cleaning the qns
clean_questions = []
for question in questions:
     clean_questions.append(clean_text(question))   
         
  //cleaning the ans
clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))       
         
 //creating a dicti that maps each word to the time it appears
word2count = {}
for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1        
         
//creating two dicti that maps the qns words an the ans words to a unique integer(tokenization n filtering of non frequent words)
threshold_questions = 20
questionswords2int = {}
word_number = 0
for word, count in word2count.items():
    if count >= threshold_questions:
        questionswords2int[word] = word_number
        word_number += 1
threshold_answers = 20
answerswords2int = {}
word_number = 0
for word, count in word2count.items():
    if count >= threshold_answers:
        answerswords2int[word] = word_number
        word_number += 1      
        
         
//Adding the last tokens to these two dicti, pad is same length and used for encoding in seq2seq model
tokens = ['<PAD>', '<EOS>', '<OUT>', '<SOS>']
for token in tokens:
    questionswords2int[token] = len(questionswords2int) + 1
for token in tokens:
    answerswords2int[token] = len(answerswords2int) + 1
    
//creating the inverse dicti of the answerswords2int dicti
answersints2word = {w_i: w for w, w_i in answerswords2int.items()}


// Adding the EOS token to the end of every answer
for i in range(len(clean_answers)):
    clean_answers[i] += ' <EOS>'
   
//Translating the qns n ans into integers & Replacing the words that were filtered out by <OUT> 
questions_into_int = []
for question in clean_questions:
    ints = [] 
    for word in question.split():
        if word not in questionswords2int:
            ints.append(questionswords2int['<OUT>'])
        else:
            ints.append(questionswords2int[word])
    questions_into_int.append(ints)
answers_into_int = []
for answer in clean_answers:
    ints = []
    for word in answer.split():
        if word not in answerswords2int:
            ints.append(answerswords2int['<OUT>'])
        else:
            ints.append(answerswords2int[word])
    answers_into_int.append(ints)       
         
 
// Sorting qns & ans by  length of qns
sorted_clean_questions = []
sorted_clean_answers = []
for length in range(1, 25 + 1):
    for i in enumerate(questions_into_int):
        if len(i[1]) == length:
            sorted_clean_questions.append(questions_into_int[i[0]])
            sorted_clean_answers.append(answers_into_int[i[0]])
            



#Building the chatbot in seq2seq model
            
            
            
//creating placeholders for the inputs & targets tf means tensorflow,keep prob is the parameter that controls the drop out rate of neurons
def model_inputs():
    inputs = tf.placeholder(tf.int32, [None, None], name = 'input')
    targets = tf.placeholder(tf.int32, [None, None], name = 'target')
    lr = tf.placeholder(tf.float32, name = 'learning_rate')
    keep_prob = tf.placeholder(tf.float32, name = 'keep_prob')
    return inputs, targets, lr, keep_prob           


// preprocessing the targets, the targets are the answers and the nueral n/w takes batches of size like 10ans & not single ans
def preprocess_targets(targets, word2int, batch_size):
    left_side = tf.fill([batch_size, 1], word2int['<SOS>'])
    right_side = tf.strided_slice(targets, [0,0], [batch_size, -1], [1,1])
    preprocessed_targets = tf.concat([left_side, right_side], 1)
    return preprocessed_targets















      