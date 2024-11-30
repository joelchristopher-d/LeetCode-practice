package BSwith2darray;

import java.util.Scanner;

public class Searchinasorted2Dmatrix {

//    Scanner scanner = new Scanner(System.in);
    int n = 3;
    int m =4;
    int target = 9;
    int[][] arr = {{1,2,3,4},
                    {5,6,7,8},
                    {9,10,11,12},
                    {13,14,15,16}};

    public boolean binarySearch(int[] arr,int target){
        int low = 0;
        int high = arr.length-1;
        while (low<=high){
            int mid = (low+high)/2;
            if (arr[mid]==target)return true;
            if (arr[mid]<target)low=mid+1;
            if(arr[mid]>target)high=mid-1;
        }
        return false;

    }

//brute
    public void findin2darray(){
        for (int i = 0; i < arr.length; i++) {
            if(binarySearch(arr[i],target)){
                System.out.println(true);
                return;
            }
        }
        System.out.println(false);
    }

//better

    public void findin2darray2(){
        int low = 0;
        int high = arr.length-1;
//        System.out.println((low+high)/2);
        while (low<=high){
            int mid = (low+high)/2;
//            System.out.println(mid);
//            System.out.printf("left: %d right: %d target: %d",arr[mid][0],arr[mid][m-1],target);
            if(arr[mid][m-1]>=target && arr[mid][0]<=target){
                if(binarySearch(arr[mid],target)) {
                    System.out.println(true);
                }
                else {
                    System.out.println(false);
                }
                return;
            } else if (arr[mid][m-1]<target) {
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }
        System.out.println(false);
//        return;
    }


}
