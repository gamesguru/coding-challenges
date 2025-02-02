#include <stack>
#include <iostream>
#include <assert.h>
using namespace std;

class Solution {
public:
    bool isValid(const string &s) {
        stack<char> sta;
        const int n = s.size() - 1;

        for (int i = 0; i <= n; i++) {
            const char c = s[i];

            if (c == '(' or c == '[' or c == '{') {
                sta.push(c);
            } else {
                // Check if stack is empty, i.e., we have a closing bracket but no opening
                if (sta.size() == 0)
                    return false;

                // Get top element
                char prev = sta.top();
                sta.pop();

                // Check if parenthesis is unmatched
                if (
                    prev == '(' and c != ')' or
                    prev == '[' and c != ']' or
                    prev == '{' and c != '}'
                )
                    return false;
            }
        }

        // Check if everything got popped off, i.e., every opening bracket had a matching closing bracket
        if (sta.size() > 0)
            return false;

        return true;
    }
};


int main() {
    // Test cases
    constexpr int n = 6;
    const string _inputs[n] = {
        // My test cases
        "[",
        "[[]",
        // NeetCode test cases
        "[]",
        "([{}])",
        "[(])",
        "]"
    };
    const bool _expecteds[n] = {
        // My test cases
        false,
        false,
        // NeetCode test cases
        true,
        true,
        false,
        false
    };

    // Run test cases
    auto *solution = new Solution;
    for (int i = 0; i < n; i++) {
        const string _input = _inputs[i];
        const bool _expected = _expecteds[i];

        cout << _input << "\n";
        bool actual = solution->isValid(_input);
        cout << "assert {expected} == {actual}" << "\n";
        cout << "assert " << _expected << " == " << actual << "\n";
        cout << endl;

        assert(_expected == actual);
    }

    return 0;
}
