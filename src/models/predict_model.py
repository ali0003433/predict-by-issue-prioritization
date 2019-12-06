
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

def avg_scorer(y, y_pred):
    '''
        To create a confusion matrix using actual results versus predicted results. Return mean of both Clinton and Trump metrics. 
   
    Args:
        y_test(arr): This is a numpy array of actual target variable.
        y_pred_test(arr): This is a numpy array of predicted target variable. 
        
    Returns:
        conf_matrix(Dataframe): Comparison of actual results versus predicted. 
    '''
    cm = confusion_matrix(y, y_pred)
    conf_matrix = pd.DataFrame(cm, index=['Clinton','Trump', 'Nonvoter/Other'], 
                           columns=['Pred Clinton','Pred Trump', 'Pred Nonvoter/Other',])
    #print(cm)
    #print(conf_matrix, '\n')
    pred_correct_clinton = cm[0][0]
    total_clinton = sum(cm[0])
    perc_correct_clinton = round(pred_correct_clinton/total_clinton, 3)*100
    
    '''
    To create a confusion matrix using actual results versus predicted results. 
    
    Args:
        y_test(arr): This is a numpy array of actual target variable.
        y_pred_test(arr): This is a numpy array of predicted target variable. 
        
    Returns:
        conf_matrix(Dataframe): Comparison of actual results versus predicted. 
    '''
    cm = confusion_matrix(y, y_pred)
    conf_matrix = pd.DataFrame(cm, index=['Clinton','Trump', 'Nonvoter/Other'], 
                           columns=['Pred Clinton','Pred Trump', 'Pred Nonvoter/Other',])
    #print(cm)
    #print(conf_matrix, '\n')
    pred_correct_trump = cm[1][1]
    total_trump = sum(cm[1])
    perc_correct_trump = round(pred_correct_trump/total_trump, 3)*100 
    return ((perc_correct_clinton + perc_correct_trump)/2)

def trump_scorer(y, y_pred):
    '''
    To create a confusion matrix using actual results versus predicted results. 
    
    Args:
        y_test(arr): This is a numpy array of actual target variable.
        y_pred_test(arr): This is a numpy array of predicted target variable. 
        
    Returns:
        conf_matrix(Dataframe): Comparison of actual results versus predicted. 
    '''
    cm = confusion_matrix(y, y_pred)
    conf_matrix = pd.DataFrame(cm, index=['Clinton','Trump', 'Nonvoter/Other'], 
                           columns=['Pred Clinton','Pred Trump', 'Pred Nonvoter/Other',])
    print(cm)
    print(conf_matrix, '\n')
    pred_correct_trump = cm[1][1]
    total_trump = sum(cm[1])
    perc_correct_trump = round(pred_correct_trump/total_trump, 3)*100 
    return perc_correct_trump


def clint_scorer(y, y_pred):
    '''
    To create a confusion matrix using actual results versus predicted results. 
    
    Args:
        y_test(arr): This is a numpy array of actual target variable.
        y_pred_test(arr): This is a numpy array of predicted target variable. 
        
    Returns:
        conf_matrix(Dataframe): Comparison of actual results versus predicted. 
    '''
    cm = confusion_matrix(y, y_pred)
    conf_matrix = pd.DataFrame(cm, index=['Clinton','Trump', 'Nonvoter/Other'], 
                           columns=['Pred Clinton','Pred Trump', 'Pred Nonvoter/Other',])
    #print(cm)
    #print(conf_matrix, '\n')
    pred_correct_clinton = cm[0][0]
    total_clinton = sum(cm[0])
    perc_correct_clinton = round(pred_correct_clinton/total_clinton, 3)*100
    return perc_correct_clinton