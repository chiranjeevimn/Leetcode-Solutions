public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        // Create a dictionary to store groups of anagrams
        Dictionary<string, List<string>> anagramGroups = new Dictionary<string, List<string>>();

        // Iterate through each string in the array
        foreach (string str in strs) {
            // Convert the string to a char array, sort it, and convert it back to a string
            char[] charArray = str.ToCharArray();
            Array.Sort(charArray);
            string sortedStr = new string(charArray);

            // Check if the sorted string is already a key in the dictionary
            // If not, add a new key with an empty list as the value
            if (!anagramGroups.ContainsKey(sortedStr)) {
                anagramGroups[sortedStr] = new List<string>();
            }

            // Add the original string to the corresponding group in the dictionary
            anagramGroups[sortedStr].Add(str);
        }

        // Convert the dictionary values to a list and return
        return anagramGroups.Values.ToList<IList<string>>();
    }
}
