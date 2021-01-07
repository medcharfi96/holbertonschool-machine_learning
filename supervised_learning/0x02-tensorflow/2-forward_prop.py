#!/usr/bin/env python3
""" task 2 """


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    fonction de propagation
    :param x: int
    :param activation:list
    :return:
    """
    create_layer = __import__('1-create_layer').create_layer
    hmed = create_layer(x, layer_sizes[0], activations[0])
    for i in range(len(layer_sizes)):
        hmed = create_layer(hmed, layer_sizes[i], activations[i])

    return (hmed)
