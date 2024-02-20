/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    // Calculate the expected sum of numbers in the range [0, n]
    var expectedSum = (nums.length * (nums.length + 1)) / 2;
    
    // Calculate the actual sum of the given array
    var actualSum = nums.reduce((acc, num) => acc + num, 0);
    
    // The missing number is the difference between expected and actual sum
    return expectedSum - actualSum;
};