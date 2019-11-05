def designerPdfViewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return max(h[alphabet.index(w)] for w in word) * len(word)

# OR

def designerPdfViewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return max(map(lambda x: h[alphabet.index(x)], word)) * len(word)