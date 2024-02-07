class Solution:
    def frequencySort(self, s: str) -> str:
        # Create a dictionary to store the frequency of each character
        frequency_dict = Counter(s)
        
        # Sort the characters based on their frequency
        sorted_chars = sorted(s, key=lambda x: (-frequency_dict[x], x))
        
        # Join the sorted characters to form the final string
        return ''.join(sorted_chars)