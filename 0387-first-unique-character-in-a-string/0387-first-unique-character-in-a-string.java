public class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> charCount = new HashMap<>();
        
        // Count occurrences of each character
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        
        // Find the first unique character
        for (int i = 0; i < s.length(); i++) {
            if (charCount.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        
        // If no unique character is found
        return -1;
    }
}