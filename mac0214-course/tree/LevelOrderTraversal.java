package hackerRank.trees;
import java.util.*;

public class LevelOrderTraversal {
    
    private static class Node {
        Node left;
        Node right;
        int data;
    
        Node(int data) {
            this.data = data;
            left = null;
            right = null;
        }
    }

	public static void levelOrder(Node root) {
        
        Queue<Node> queue = new LinkedList<>();
        if (root != null) queue.add(root);

        Node currentNode = root;
        
        while (!queue.isEmpty()) { 
            currentNode = queue.remove();
            System.out.printf("%d ", currentNode.data);
            
            if (currentNode.left != null) queue.add(currentNode.left);
            if (currentNode.right != null) queue.add(currentNode.right);
        }
    }
}
