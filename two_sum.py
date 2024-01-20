'''
Dada una lista de números (num) y una entero (target), devuelve los
índices de los dos números qué sumen target.
'''

nums = []
target = None

class Solution:
    def twoSum(self, nums, target):
        solucion = []
        for num in range(len(nums)):
            for n in range(num+1, len(nums)):

                if nums[num] + nums[n] == target:
                    solucion.append(num-1)
                    solucion.append(n-1)
                
                    return solucion




resultado = Solution()
print(resultado.twoSum(nums, target))