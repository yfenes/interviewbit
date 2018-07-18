class Solution:
	###########################################
	###########################################
	####### THIS IS NOT A GOOD SOLUTION #######
	###########################################
	###########################################

    def del_zeros(self,A):
        delzeros = 0
        for i in range(len(A)):
            if A[i] == 0:
                delzeros += 1
            else:
                break
        A = A[delzeros:]
        return A
    
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if A == [0]:
            return [1]
        
        A = self.del_zeros(A)

        #A = A[1:]
        last_change = len(A) - 1
        
        if A[-1]!=9:
            A[-1] += 1
            return A
        
        while (A[last_change]==9 and last_change >= 0):
            
            # if most significant digit
            if last_change == 0:
                A[0] = 0
                A = [1] + A
                return A
            else:
                A[last_change] = 0
            
            last_change -= 1
        
        A[last_change] += 1
        
        return A