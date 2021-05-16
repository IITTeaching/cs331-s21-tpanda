import urllib

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii', 'replace')
    return bookascii.split()


def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    allWords = book_to_words()  # list of all words
    longest = len(allWords[0])

    for i in range(len(allWords)):
        if len(allWords[i]) > longest:
            longest = len(allWords[i])

    for i in range(len(allWords)):
        allWords[i] += '\0'.encode('ascii', 'replace') * (longest - len(allWords[i]))

    for i in range(longest - 1, -1, -1):
        allWords = radixSort(allWords, i)

    for i in range(len(allWords)):
        allWords[i] = allWords[i].decode('ascii').replace('\x00', '')
        allWords[i] = bytes(allWords[i], encoding='ascii')

    return allWords


def radixSort(arr, arrIndex):
    count = [0] * 127
    output = [0] * len(arr)

    for word in arr:
        count[word[arrIndex]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        idx = arr[i][arrIndex]
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

    return arr

if __name__ == '__main__':
    print(radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'))