package Strings;

import java.util.Stack;

public class RemoveOutermostParentheses {
    String parantheses = "(()())(())(()(()))";

    public void Removeouter(){
        Stack<Character> stack = new Stack<Character>();
        String ans = "";
        for (char i:parantheses.toCharArray()){
            if(stack.isEmpty() && i == '('){
                stack.push(i);
            }
            else if(!stack.isEmpty()){
                if(i=='('){
                    stack.push(i);
                }
                if(i==')'){
                    stack.pop();
                }
                if (!stack.isEmpty()){
                    ans+=i;
                }

            }

        }
        System.out.println(ans);
    }

}
