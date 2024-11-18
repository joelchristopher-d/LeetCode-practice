import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class RemoveUnbalancedParentheses {

    public static String removeparenthesis(String paranthesis){

        Stack<Integer> stack = new Stack<>();
        Set<Integer> invalidIndices = new HashSet<>();

        for(int i=0;i<paranthesis.length();i++){
            char ch = paranthesis.charAt(i);
            if (ch =='('){
                stack.push(i);
            } else if (ch==')') {
                if(!stack.isEmpty()){
                    stack.pop();
                }
                else {
                    invalidIndices.add(i);
                }

            }
        }
        while (!stack.isEmpty()){
            invalidIndices.add(stack.pop());
        }
        String result = "";
        for (int i = 0; i < paranthesis.length(); i++) {
            if(!invalidIndices.contains(i)){
                result += paranthesis.charAt(i);
            }

        }


        return result;
    }

}


public class Main {
    public static void main(String[] args) {

        Search obj = new Search();
        int[] arr = {0,1,2,3,4,5,6,7,8,9};
        int tar = 0;
//        System.out.println(obj.BinarySearch(arr,tar));

//        RemoveUnbalancedParentheses remove = new RemoveUnbalancedParentheses();
        System.out.println(RemoveUnbalancedParentheses.removeparenthesis("((abc)((de))"));
        System.out.println(RemoveUnbalancedParentheses.removeparenthesis(")(((ab)"));
    }

}
