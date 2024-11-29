public class Findtherowwithmaximumnumberof1s {
//    int [][] twod = new int[3][3];
    int [][] twod = {{0, 0, 1}, {0,1,1}, {1, 1, 1}};

    public void brute(){
        int index = -1;
        int init = 0;
        for (int i = 0; i < twod.length; i++) {
            int counter = 0;
            for (int j:twod[i]){
                if(j==1){
                    counter++;
                }
                if(counter>init){
                    index = i;
                    init=counter;
                }
            }
        }
        System.out.println(index);
    }

//    Optimal
    public void max1s(){
        int init = 0;
        int index = -1;
        for (int i = 0; i < twod.length; i++) {
            int ones = 3 - lowerbound(twod[i],twod[i].length,1);
//            System.out.println(ones);
            if(ones>init){
                init = ones;
                index = i;
            }
        }
        System.out.println(index);
    }

    public int lowerbound(int[] arr,int len,int num){
        int low = 1,high = len-1;
        int ans = len;
        while (low<=high){
            int mid = (low+high)/2;
            if(arr[mid]>=num){
                ans = mid;
                high = mid-1;
            }
            else {
                low = mid+1;
            }
        }
        return ans;
    }
}
