package hackerrank.stacks;
import java.util.Stack;
import java.util.HashMap;
public class BalancedBrackets {
    
    public static String isBalanced(String s) {
        
        HashMap<Character, Character> matchingPairs = new HashMap<>();
        matchingPairs.put(')', '(');
        matchingPairs.put(']', '[');
        matchingPairs.put('}', '{');

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return "NO";
                Character possibleMatch = stack.pop();
                if (possibleMatch != matchingPairs.get(c))
                    return "NO";
            }
        }

        return (stack.isEmpty()) ? "YES" : "NO";
    }
}
