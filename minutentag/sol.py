"""
A video transcoder was implemented with different presets to process different videos in the application. The videos should be
encoded with a given configuration done by this function. Can you explain what this function is detecting from the params
and returning based in its conditionals?
"""
def fn(config, w, h):
    v = None
    # ar is the aspect ratio
    ar = w / h # width - height / (ancho - alto)

    if ar < 1:
        v = [r for r in config['p'] if r['width'] <= w]
    elif ar > 4 / 3:
        v = [r for r in config['l'] if r['width'] <= w]
    else:
        v = [r for r in config['s'] if r['width'] <= w]

    return v

if __name__ == '__main__':
    conf = {
        'p':[
            {'id': 'portrait_1', 'width': 200},
            {'id': 'portrait_2', 'width': 5100},
            {'id': 'portrait_3', 'width': 4003},
            {'id': 'portrait_4', 'width': 5}
        ],
        'l':[
            {'id': 1, 'width': 350},
            {'id': 2, 'width': 780},
            {'id': 3, 'width': 1280},
            {'id': 4, 'width': 4820}
        ],
        's':[
            {'id': 1, 'width': 9120},
            {'id': 2, 'width': 701},
            {'id': 3, 'width': 20},
            {'id': 4, 'width': 15000}
        ]
    }
    print(fn(conf, 1000, 1000))