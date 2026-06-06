import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        self.vocab = []
        self.vocab.append(self.pad_token)
        self.vocab.append(self.unk_token)
        self.vocab.append(self.bos_token)
        self.vocab.append(self.eos_token)
        self.vocabb = []
        for sentence in texts:
            for word in sentence.split():
                if word.lower() not in self.vocabb:
                    self.vocabb.append(word.lower())
        self.vocab_size = len(self.vocabb) + 4
        self.vocabb = sorted(self.vocabb)
        self.vocab = self.vocab + self.vocabb
        for idx,word in enumerate(self.vocab):
            self.word_to_id[word] = idx
            self.id_to_word[idx] = word
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        tokenList = []
        for word in text.split():
            if word.lower() in self.vocab:
                tokenList.append(self.word_to_id[word.lower()])
            else:
                tokenList.append(self.word_to_id[self.unk_token])
        return tokenList
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        decoded = []
        for token_id in ids:
            decoded.append(self.id_to_word.get(token_id, self.unk_token))
        return " ".join(decoded)
