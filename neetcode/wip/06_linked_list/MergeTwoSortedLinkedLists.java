package neetcode;

public class MergeTwoSortedLinkedLists {
    /**
     * Definition for singly-linked list.
     */
    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        return new ListNode();
    }

    public static void main(String[] args) {
        mergeTwoLists();
//        neetcode.DepthOfBinaryTree.TreeNode a = new neetcode.DepthOfBinaryTree.TreeNode(10);
//        neetcode.DepthOfBinaryTree.TreeNode b = new neetcode.DepthOfBinaryTree.TreeNode(5, new neetcode.DepthOfBinaryTree.TreeNode(7), new neetcode.DepthOfBinaryTree.TreeNode(8));
//        neetcode.DepthOfBinaryTree.TreeNode root = new neetcode.DepthOfBinaryTree.TreeNode(1, a, b);
//        System.out.println("Should be 3: " + neetcode.DepthOfBinaryTree.maxDepth(root));
    }
}