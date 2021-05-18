import numpy as np

#Here we are going to do two steps
# 1 - Calculate the Output
# 2 - Compare the output to the expected Output

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derrivative(x):
    return x * (1 - x)

training_inputs = np.array([
    [0,0,1],
    [1,1,1],
    [1,0,1],
    [0,1,1]
])

# .T Transpose the matrix so its a 1 x 4
training_outputs = np.array(
    [[0,1,1,0]]
).T

np.random.seed(1)

# How many weights do we have?
# in1, in2, in3 each need their own weight... so 3!
# Create random weights
synaptic_weights = 2 * np.random.random((3,1)) - 1

print('Random starting synaptic weights')
print(synaptic_weights)

for iteration in range(20000):

    input_layer = training_inputs

    # Take each input and multiply it times our weights
    unsquished_outputs = np.dot(input_layer, synaptic_weights)

    # Squish our result between 0 and 1 by using our normalizing fn
    normalized_outputs = sigmoid(unsquished_outputs)
    #print('Normalized Outputs')
    #print(normalized_outputs)

    # 2 - Calc error by checking the training outputs with our calulated ones
    error = training_outputs - normalized_outputs
    #print('Error')
    #print(error)

    adjustments = error * sigmoid_derrivative(normalized_outputs)
    #print('Adjustments')
    #print(adjustments)

    # For next section...
    synaptic_weights += np.dot(input_layer.T, adjustments)


print('Outputs after training')
print(normalized_outputs)

print('Weights')
print(synaptic_weights)


# Wow so we entered some data and created some ARBITRARY weights for
# each column and now we test those weights... How do we test those weights?

# Well if you say as part of your output:
# Column 1 should be 1 and the output should be 1
# Column 2 doesnt matter
# Column 3 needs to be a 0 when output is 1
# Then your weights are [1, 0, 0]?  Is this correct?
# TODO - Manially assign weights!


# Now we calculate HOW MUCH our error was off the result we wanted


# Then we adjust our weights and try again
# 1 - For a HUGE error, we want a HUGE adjustment! (so we multiply * error)
# 2 - We want them to relate to the INPUTS in some way, so we multiply them by the
#   inputs. (i.e. if an input is 0 we DONT change that input!)
