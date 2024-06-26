
## SimpleRNN

```python
neuromind.layers.recurrent.SimpleRNN(input_dim, output_dim, 
        init='glorot_uniform', inner_init='orthogonal', activation='sigmoid', weights=None,
        truncate_gradient=-1, return_sequences=False)
```
Fully connected RNN where output is to fed back to input. Not a particularly useful model, included for demonstration purposes.

- __Input shape__: 3D tensor with shape: `(nb_samples, timesteps, input_dim)`.

- __Output shape__: 
    - if `return_sequences`: 3D tensor with shape: `(nb_samples, timesteps, ouput_dim)`.
    - else: 2D tensor with shape: `(nb_samples, output_dim)`.

- __Arguments__:
    - __input_dim__: dimension of the input.
    - __output_dim__: dimension of the internal projections and the final output.
    - __init__: weight initialization function. Can be the name of an existing function (str), or a Theano function (see: [initializations](../initializations.md)).
    - __activation__: activation function. Can be the name of an existing function (str), or a Theano function (see: [activations](../activations.md)).
    - __weights__: list of numpy arrays to set as initial weights. The list should have 3 elements, of shapes: `[(input_dim, output_dim), (output_dim, output_dim), (output_dim,)]`.
    - __truncate_gradient__: Number of steps to use in truncated BPTT. See: [Theano "scan"](http://deeplearning.net/software/theano/library/scan.html).
    - __return_sequences__: Boolean. Whether to return the last output in the output sequence, or the full sequence.

---

## SimpleDeepRNN

```python
neuromind.layers.recurrent.SimpleDeepRNN(input_dim, output_dim, depth=3,
        init='glorot_uniform', inner_init='orthogonal', 
        activation='sigmoid', inner_activation='hard_sigmoid',
        weights=None, truncate_gradient=-1, return_sequences=False)
```
Fully connected RNN where the output of multiple timesteps (up to "depth" steps in the past) is fed back to the input: 

```
output = activation( W.x_t + b + inner_activation(U_1.h_tm1) + inner_activation(U_2.h_tm2) + ... )
```

Not a particularly useful model, included for demonstration purposes.

- __Input shape__: 3D tensor with shape: `(nb_samples, timesteps, input_dim)`.

- __Output shape__:
    - if `return_sequences`: 3D tensor with shape: `(nb_samples, timesteps, ouput_dim)`.
    - else: 2D tensor with shape: `(nb_samples, output_dim)`.

- __Arguments__:
    - __input_dim__: dimension of the input.
    - __output_dim__: dimension of the internal projections and the final output.
    - __depth__: int >= 1. Lookback depth (eg. depth=1 is equivalent to SimpleRNN).
    - __init__: weight initialization function for the output cell. Can be the name of an existing function (str), or a Theano function (see: [initializations](../initializations.md)).
    - __inner_init__: weight initialization function for the inner cells.
    - __activation__: activation function for the output. Can be the name of an existing function (str), or a Theano function (see: [activations](../activations.md)).
    - __inner_activation__: activation function for the inner cells.
    - __weights__: list of numpy arrays to set as initial weights. The list should have depth+2 elements.
    - __truncate_gradient__: Number of steps to use in truncated BPTT. See: [Theano "scan"](http://deeplearning.net/software/theano/library/scan.html).
    - __return_sequences__: Boolean. Whether to return the last output in the output sequence, or the full sequence.


---

## GRU

```python
neuromind.layers.recurrent.GRU(input_dim, output_dim=128, 
        init='glorot_uniform', inner_init='orthogonal',
        activation='sigmoid', inner_activation='hard_sigmoid',
        weights=None, truncate_gradient=-1, return_sequences=False)
```

Gated Recurrent Unit - Cho et al. 2014.

- __Input shape__: 3D tensor with shape: `(nb_samples, timesteps, input_dim)`.

- __Output shape__:
    - if `return_sequences`: 3D tensor with shape: `(nb_samples, timesteps, ouput_dim)`.
    - else: 2D tensor with shape: `(nb_samples, output_dim)`.

- __Arguments__:
    - __input_dim__: dimension of the input.
    - __output_dim__: dimension of the internal projections and the final output.
    - __init__: weight initialization function for the output cell. Can be the name of an existing function (str), or a Theano function (see: [initializations](../initializations.md)).
    - __inner_init__: weight initialization function for the inner cells.
    - __activation__: activation function for the output. Can be the name of an existing function (str), or a Theano function (see: [activations](../activations.md)).
    - __inner_activation__: activation function for the inner cells.
    - __weights__: list of numpy arrays to set as initial weights. The list should have 9 elements.
    - __truncate_gradient__: Number of steps to use in truncated BPTT. See: [Theano "scan"](http://deeplearning.net/software/theano/library/scan.html).
    - __return_sequences__: Boolean. Whether to return the last output in the output sequence, or the full sequence.

- __References__: 
    - [On the Properties of Neural Machine Translation: Encoder–Decoder Approaches](http://www.aclweb.org/anthology/W14-4012)
    - [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](http://arxiv.org/pdf/1412.3555v1.pdf)

---

## LSTM

```python
neuromind.layers.recurrent.LSTM(input_dim, output_dim=128, 
        init='glorot_uniform', inner_init='orthogonal', 
        activation='tanh', inner_activation='hard_sigmoid',
        weights=None, truncate_gradient=-1, return_sequences=False)
```

Long-Short Term Memory unit - Hochreiter 1997.

- __Input shape__: 3D tensor with shape: `(nb_samples, timesteps, input_dim)`.

- __Output shape__:
    - if `return_sequences`: 3D tensor with shape: `(nb_samples, timesteps, ouput_dim)`.
    - else: 2D tensor with shape: `(nb_samples, output_dim)`.

- __Arguments__:
- __input_dim__: dimension of the input.
    - __output_dim__: dimension of the internal projections and the final output.
    - __init__: weight initialization function for the output cell. Can be the name of an existing function (str), or a Theano function (see: [initializations](../initializations.md)).
    - __inner_init__: weight initialization function for the inner cells.
    - __activation__: activation function for the output. Can be the name of an existing function (str), or a Theano function (see: [activations](../activations.md)).
    - __inner_activation__: activation function for the inner cells.
    - __weights__: list of numpy arrays to set as initial weights. The list should have 12 elements.
    - __truncate_gradient__: Number of steps to use in truncated BPTT. See: [Theano "scan"](http://deeplearning.net/software/theano/library/scan.html).
    - __return_sequences__: Boolean. Whether to return the last output in the output sequence, or the full sequence.

- __References__: 
    - [Long short-term memory](http://deeplearning.cs.cmu.edu/pdfs/Hochreiter97_lstm.pdf) (original 1997 paper)
    - [Learning to forget: Continual prediction with LSTM](http://www.mitpressjournals.org/doi/pdf/10.1162/089976600300015015)
    - [Supervised sequence labelling with recurrent neural networks](http://www.cs.toronto.edu/~graves/preprint.pdf)
            
            
                