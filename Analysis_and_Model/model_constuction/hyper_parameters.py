h_paras = {
    # maximum number of epochs
    'n_epochs': 100,
    # mini-batch size for dataloader
    'batch_size': 128,
    # optimization algorithm (optimizer in torch.optim)
    'optimizer': 'Adam',
    # hyper-parameters for the optimizer (depends on which optimizer you are using)
    'optim_hparas': {
        # learning rate of Adam
        'lr': 0.0003,
        "weight_decay" : 1e-5
    },
    # your model will be saved here
    'save_path': './model.pth',
    'early_stop': 10,
}