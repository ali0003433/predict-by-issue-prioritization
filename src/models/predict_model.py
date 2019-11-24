
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

def create_perf_metrics(y_test, y_pred_test):
    '''
    To create a confusion matrix using actual results versus predicted results. 
    
    Args:
        y_test(arr): This is a numpy array of actual target variable.
        y_pred_test(arr): This is a numpy array of predicted target variable. 
        
    Returns:
        conf_matrix(Dataframe): Comparison of actual results versus predicted. 
    '''
    cm = confusion_matrix(y_test, y_pred_test)
    conf_matrix = pd.DataFrame(cm, index=['Nonvoter/Other','Clinton','Trump'], 
                           columns=['Pred Nonvoter/Other','Pred Clinton','Pred Trump'])
    print(conf_matrix, '\n')
    
    pred_correct_clinton = cm[1][1]
    total_clinton = sum(cm[1])
    perc_correct_clinton = round(pred_correct_clinton/total_clinton, 3)*100
    
    pred_correct_trump = cm[2][2]
    total_trump = sum(cm[2])
    perc_correct_trump = round(pred_correct_trump/total_trump, 3)*100
    
    print('\n', perc_correct_clinton, 'percent that were predicted Clinton were actually Clinton''\n',
          perc_correct_trump, 'percent that were predicted Trump were actually Trump' '\n'),
    score_dict = {'Clinton': perc_correct_clinton,
                  'Trump': perc_correct_trump}
    return score_dict