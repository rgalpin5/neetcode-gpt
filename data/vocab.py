from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        # Return (stoi, itos) where:
        # - stoi maps each unique character to a unique integer (sorted alphabetically)
        # - itos is the reverse mapping (integer to character)
        tokens = sorted(set(text))
        stoi = {ch: i for i, ch in enumerate(tokens)}
        itos = {i: ch for ch, i in stoi.items()}
        return stoi, itos


    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        return [stoi[ch] for ch in text]

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        return ''.join(itos[i] for i in ids)
