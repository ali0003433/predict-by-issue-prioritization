# functions to run model 
import pickle
import numpy as np


def make_prediction(chat_in):
    if input == 1:
       probs = {'res': 'You chose 1.'}
    elif input == 2:
       probs = {'res': 'You chose 2'}
    else:
       probs = {'res': 'Where is my answer?'}
    return (chat_in, probs)


if __name__ == '__main__':
    from pprint import pprint
    print('Checking to see what empty string predicts')
    print('input string is ')
    chat_in = 'bob'
    pprint(chat_in)

    x_input, probs = make_prediction(chat_in)
    print(f'Input values: {x_input}')
    print('Output possibilities')
    print(probs)