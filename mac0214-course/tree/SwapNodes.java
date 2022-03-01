package hackerrank.trees;

import java.util.*;

public class SwapNodes {

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

    public static Node createTree(Node root, List<List<Integer>> indexes) {

        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        
        int n = indexes.size();

        for (int i = 0; i < n; i++) {
            int a = indexes.get(i).get(0), b = indexes.get(i).get(1);
            
            Node currentNode = queue.remove();

            if (a != -1) {
                currentNode.left = new Node(a);
                queue.add(currentNode.left);
            } 

            if (b != -1) {
                currentNode.right = new Node(b);
                queue.add(currentNode.right);
            } 
        }

        return root;
    }

    public static void swap(Node root, int k, int depth, List<Integer> orderTraversal) {

        // Base case:
        if (root == null) return;

        // If h is a multiple of k, swap the left and right subtrees at that level.
        if (depth+1 % k == 0) {
            Node temp = root.right;
            root.right = root.left;
            root.left = temp;
        }

        // In order traversal:
        swap(root.left, k, depth+1, orderTraversal);
        orderTraversal.add(root.data);
        swap(root.right, k, depth+1, orderTraversal);
    }
    
    public static List<List<Integer>> swapNodes(List<List<Integer>> indexes, List<Integer> queries) {
        
        List<List<Integer>> result = new LinkedList<>(); 

        int t = queries.size();
        
        Node root = new Node(1);
        root = createTree(root, indexes);

        for (int i = 0; i < t; i++) {
            int k = queries.get(i);
            int depth = 1;
            LinkedList<Integer> orderTraversal = new LinkedList<>();
            swap(root, k, depth, orderTraversal);
            result.add(orderTraversal);
        }

        return result;
    }
}
