#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {
    }

    explicit ListNode(const int x) : val(x), next(nullptr) {
    }

    ListNode(const int x, ListNode *next) : val(x), next(next) {
    }
};

class Solution {
public:
    static ListNode *reverseList(ListNode *head) {
        return nullptr;
    }
};

int main() {
    // auto *solution = new Solution();
    Solution::reverseList();
    return 0;
}
