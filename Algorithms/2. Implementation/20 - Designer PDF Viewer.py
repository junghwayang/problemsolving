def designerPdfViewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return max(h[alphabet.index(w)] for w in word) * len(word)

# OR

def designerPdfViewer(h, word):
    return max(map(lambda x: h[ord(x) - ord('a')], word)) * len(word)