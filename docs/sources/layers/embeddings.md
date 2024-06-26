
## Embedding

```python
neuromind.layers.embeddings.Embedding(input_dim, output_dim, init='uniform', weights=None)
```

Turn positive integers (indexes) into denses vectors of fixed size,
eg. `[[4], [20]] -> [[0.25, 0.1], [0.6, -0.2]]`

- __Input shape__: 2D tensor with shape: `(nb_samples, maxlen)`.

- __Output shape__: 3D tensor with shape: `(nb_samples, maxlen, output_dim)`.

- __Arguments__:

    - __input_dim__: int >= 0. Size of the vocabulary, ie. 1+maximum integer index occuring in the input data.
    - __output_dim__: int >= 0. Dimension of the dense embedding.
    - __init__: name of initialization function for the weights of the layer (see: [initializations](../initializations.md)), or alternatively, Theano function to use for weights initialization. This parameter is only relevant if you don't pass a `weights` argument.
    - __weights__: list of numpy arrays to set as initial weights. The list should have 1 element, of shape `(input_dim, output_dim)`.


## WordContextProduct

```python
neuromind.layers.embeddings.WordContextProduct(input_dim, proj_dim=128, 
        init='uniform', activation='sigmoid', weights=None)
```

This layer turns a pair of words (a pivot word + a context word, ie. a word from the same context as a pivot, or a random, out-of-context word), indentified by their indices in a vocabulary, into two dense reprensentations (word representation and context representation).

Then it returns `activation(dot(pivot_embedding, context_embedding))`, which can be trained to encode the probability of finding the context word in the context of the pivot word (or reciprocally depending on your training procedure).

For more context, see Mikolov et al.: [Efficient Estimation of Word reprensentations in Vector Space](http://arxiv.org/pdf/1301.3781v3.pdf)

- __Input shape__: 2D tensor with shape: `(nb_samples, 2)`.

- __Output shape__: 2D tensor with shape: `(nb_samples, 1)`.

- __Arguments__:

    - __input_dim__: int >= 0. Size of the vocabulary, ie. 1+maximum integer index occuring in the input data.
    - __proj_dim__: int >= 0. Dimension of the dense embedding used internally.
    - __init__: name of initialization function for the embeddings (see: [initializations](../initializations.md)), or alternatively, Theano function to use for weights initialization. This parameter is only relevant if you don't pass a `weights` argument.
    - __activation__: name of activation function to use (see: [activations](../activations.md)), or alternatively, elementwise Theano function.
    - __weights__: list of numpy arrays to set as initial weights. The list should have 2 element, both of shape `(input_dim, proj_dim)`. The first element is the word embedding weights, the second one is the context embedding weights.
