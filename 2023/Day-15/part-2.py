from collections import defaultdict


def hash(label):
    label_hash = 0
    for char in label:
        label_hash += ord(char)
        label_hash *= 17
        label_hash %= 256

    return label_hash


with open('input.txt', 'r') as f:
    total, boxes = 0, defaultdict(dict)

    for seq in f.read().strip().split(','):
        if '-' in seq:
            label = seq[:-1]
            boxes[hash(label)].pop(label, None)
        else:
            label, focal_length = seq.split('=')
            boxes[hash(label)][label] = int(focal_length)

    for box, lenses in boxes.items():
        for idx, focal_length in enumerate(lenses.values()):
            total += (box + 1) * (idx + 1) * focal_length
        
    print(total)
