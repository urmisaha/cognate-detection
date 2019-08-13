# cognate-detection
We have two csv files, one containing hindi words, another containing marathi words.

The data format is:
> id, word, gloss, example

Words of two different languages are cognates if they have the same word id.

We create non-cognates from these two data files by running mismatch.py