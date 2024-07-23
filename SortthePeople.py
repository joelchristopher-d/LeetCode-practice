class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        def Partition(arr,low,high):
            pivot = arr[high][1]
            i = low-1
            for j in range(low,high):
                if arr[j][1]>=pivot:
                    i+=1
                    arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[high]=arr[high],arr[i+1]
            return i+1


        def QuickSort(arr,low,high):
            if low<high:
                pi = Partition(arr,low,high)
                QuickSort(arr,low,pi-1)
                QuickSort(arr,pi+1,high)

        
        dicti=[]
        for i in range(len(names)):
            dicti.append((names[i],heights[i]))
        n=len(dicti)
        QuickSort(dicti,0,n-1)
        l = [i[0] for i in dicti]
        return l     
