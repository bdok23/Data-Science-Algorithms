batch_size - the size of the batch (or number of training instances in the batch)
batch_size is NOT the size of the batch
batch-size usually defaults to 32, can be 16, 64, 128, 256...

training_step/iteration - perform one gradient update (train, calculate error, update parameter)

epoch - the number of times the model sees the entire dataset (once all the batches are drawn from the training dataset, this completes one epoch in training)

batch_size and epochs are the main hyperparameters of the gradient descent alg

steps_per_epoch gives the number of batches looked at per epoch (which will overwrite the default number of batches = total training dataset / batch_size)

batch gradient descent -> batch_size = full training dataset
    - model parameters are updated once after each epoch of training
    - computationally efficient (no need to calculate gradient often)

stochastic gradient descent -> batch_size = 1
    - models parameters are updated after each training example
    - very computationally expensive

mini-batch gradient descent - 1 < batch_size < full training dataset
