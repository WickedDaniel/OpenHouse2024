import keras
import tensorflow as tf
from keras._tf_keras.keras.preprocessing.text import Tokenizer
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
import numpy as np
import random
import json
import warnings
warnings.filterwarnings('ignore')

trainingepoch = 100
data = None
model = None
tokenizer = Tokenizer(filters='',oov_token='<unk>')
response_for_intent = {}
index_to_intent = {}
def LoadData():
    global data
    with open('Training\\intents.json', 'r') as f:
        data = json.load(f)
        
def CleanData(line):
    cleaned_line = ''
    for char in line:
        if char.isalpha():
            cleaned_line += char
        else:
            cleaned_line += ' '
    cleaned_line = ' '.join(cleaned_line.split())
    return cleaned_line

def TrainModel():
    global response_for_intent
    global index_to_intent
    global tokenizer
    global model
    LoadData()
    #list of intents
    intents = []                                            
    unique_intents = []
    #all text data to create a corpus
    text_input= []    
    #dictionary mapping intent with appropriate response
    response_for_intent = {}                                
    for intent in data['intents']:
        #list of unique intents
        if intent['intent'] not in unique_intents:            
            unique_intents.append(intent['intent'])  
        for text in intent['text']:
            #cleaning is done before adding text to corpus
            text_input.append(CleanData(text))                    
            intents.append(intent['intent'])
        if intent['intent'] not in response_for_intent:
            response_for_intent[intent['intent']] = [] 
        for response in intent['responses']:
            response_for_intent[intent['intent']].append(response)

    
    tokenizer.fit_on_texts(text_input)
    sequences = tokenizer.texts_to_sequences(text_input)
    padded_sequences = pad_sequences(sequences, padding='pre')

    intent_to_index = {}
    categorical_target = []
    index = 0

    for intent in intents:
        if intent not in intent_to_index:
            intent_to_index[intent] = index
            index += 1
        categorical_target.append(intent_to_index[intent])

    num_classes = len(intent_to_index)
    # Convert intent_to_index to index_to_intent
    index_to_intent = {index: intent for intent, index in intent_to_index.items()}
    index_to_intent

    categorical_vec = keras.utils.to_categorical(categorical_target, 
                                                    num_classes=num_classes)

    categorical_vec = categorical_vec.astype('int32')

    # print('Shape of Ca',categorical_vec.shape)
    categorical_vec[:5]

    epochs=trainingepoch
    embed_dim=300
    lstm_num=50
    output_dim=categorical_vec.shape[1]
    input_dim=len(unique_intents)
    # print("Input Dimension :{},\nOutput Dimension :{}".format(input_dim,output_dim))

    model = keras.models.Sequential([
        keras.layers.Embedding(len(tokenizer.word_index) + 1, embed_dim),
        keras.layers.Bidirectional(keras.layers.LSTM(lstm_num, dropout=0.1)),  
        keras.layers.Dense(lstm_num, activation='relu'),
        keras.layers.Dropout(0.4),
        keras.layers.Dense(output_dim, activation='softmax')
    ])

    optimizer = keras.optimizers.Adam(learning_rate=0.001)  
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    model.fit(padded_sequences, categorical_vec, epochs=epochs, verbose=0)
    return model

model = TrainModel()
def Respuesta(sentence):
    sent_tokens = []
    # Split the input sentence into words
    words = sentence.split()
    # Convert words to their corresponding word indices
    for word in words:                                           
        if word in tokenizer.word_index:
            sent_tokens.append(tokenizer.word_index[word])
        else:
            # Handle unknown words
            sent_tokens.append(tokenizer.word_index['<unk>'])
    sent_tokens = tf.expand_dims(sent_tokens, 0)
    #predict numerical category
    pred = model(sent_tokens)    
    #category to intent
    pred_class = np.argmax(pred.numpy(), axis=1)                
    # random response to that intent
    return random.choice(
        response_for_intent[index_to_intent[pred_class[0]]]), index_to_intent[pred_class[0]]

# while True:                                                
#     query = input('You: ')
#     bot_response, typ = Respuesta(query)
#     print('Geek: {} -- TYPE: {}'.format(bot_response, typ))
#     print()