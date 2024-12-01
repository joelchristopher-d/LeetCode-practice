package BSwith2darray;

public class Searchinarowandcolumnwisesortedmatrix {
//    int[][] arr = {
//            {1, 4, 7, 11, 15},
//            {2, 5, 8, 12, 19},
//            {3, 6, 9, 16, 22},
//            {10, 13, 14, 17, 24},
//            {18, 21, 23, 26, 30}
//    };
    int[][] arr = {{-5}};

    int target = -5;

    public boolean Search_rowandcolumnwise(){
        int rowlen = arr.length;
        int collen = arr[0].length;
        int row = 0;
        int col = collen-1;
        while (row<rowlen && col>=0){
//            System.out.printf("row: %d col: %d",row,col);
            if(arr[row][col]==target){
//                System.out.println(true);
                return true;
            }
            else if (arr[row][col]<target)row++;
            else col--;
        }
//        System.out.println(false);
        return false;
    }
}
