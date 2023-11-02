#%conda install -c conda-forge matplotlib
#%conda install -c anaconda numpy
import numpy as np
import matplotlib.pyplot as plt
from get_model import model_acc_record, model_loss_record
def plot_learning_curve_loss(loss_record, title=''):
    #plot1 : train loss
    #plot2 : val loss
    train_data = np.array(loss_record['train']).flatten()
    val_data = np.array(loss_record['val']).flatten()
    #setting index range
    total_steps = len(train_data)
    x_1 = range(total_steps)

    x_2 = x_1[::len(train_data) // len(val_data)]
    #figure size setting
    plt.figure(figsize=(6, 4))
    #plot train data
    plt.plot(x_1, train_data, c='tab:red', label='train')
    #plot val data
    plt.plot(x_2, val_data, c='tab:cyan', label='val')

    plt.ylim(0.0, 4.)
    #title & label setting
    plt.title('Learning curve of {}'.format(title))
    plt.xlabel('Training steps')
    plt.ylabel('Cross Entropy loss')
    #show legend
    plt.legend()
    #show plot
    plt.show()
def plot_learning_curve_acc(acc_record, title=''):
    #plot1 : train acc
    #plot2 : val acc
    train_data = np.array(acc_record['train']).flatten()
    val_data = np.array(acc_record['val']).flatten()
    #setting index range
    x_1 = range(len(train_data))
    x_2 = range(len(val_data))

    #figure size setting
    plt.figure(figsize=(6, 4))
    #plot train data
    plt.plot(x_1, train_data, c='tab:red', label='train')
    #plot val data
    plt.plot(x_2, val_data, c='tab:cyan', label='val')

    plt.ylim(0.0, 1.0)
    #title & label setting
    plt.title('Learning curve of {}'.format(title))
    plt.xlabel('Training steps')
    plt.ylabel('Cross Entropy loss')
    #show legend
    plt.legend()
    #show plot
    plt.show()

plot_learning_curve_loss(model_loss_record, title='deep model')
plot_learning_curve_acc(model_acc_record, title='deep model')