class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0]) # Here it sort the interval
        
        m = [] # assigning the empty list
        
        # for loop for iterating through each interval
        
        for i in intervals:
            # check in the m list
            if not m or i[0] > m[-1][1]:
                m.append(i)
            else:
                m[-1][1] = max(m[-1][1], i[1]) # this will pic the highest value 
                
        return m    # Return the merged value