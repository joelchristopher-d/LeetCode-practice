class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # self.Selectionsort(nums,0)
        return self.Selectionsort(nums)


    def Selectionsort(self,l):
        for i in range(0,len(l)):
            min_ind=i
            for j in range(i,len(l),2):
                if j%2==0 and l[min_ind]>l[j] or j%2!=0 and l[min_ind]<l[j]:
                    min_ind=j
            l[i],l[min_ind]=l[min_ind],l[i]
        return l

    # def Selectionsort(self,l,start):
    #     for i in range(start,len(l),2):
    #         min_ind=i
    #         for j in range(i+2,len(l),2):
    #             if j%2==0 and l[min_ind]>l[j] or j%2!=0 and l[min_ind]<l[j]:
    #                 min_ind=j
    #         l[i],l[min_ind]=l[min_ind],l[i]
    #     return l
    
        
