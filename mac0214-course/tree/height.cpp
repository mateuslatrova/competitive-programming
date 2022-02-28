#include <bits/stdc++.h>

using namespace std;

// The tree node has data, left child and right child 
class Node {
    int data;
    Node* left;
    Node* right;
};

int height(Node* root) {

    if (root == nullptr) return -1;
    
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    
    int h = 1 + max(leftHeight, rightHeight);
    
    return h;
}