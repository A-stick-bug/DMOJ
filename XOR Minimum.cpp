// check python code for explanation

#include <bits/stdc++.h>
using namespace std;

const int MN = 32;
int N, Q, x, arr[100005], flipped[MN];
struct TrieNode {
    TrieNode* child[2];
    int val;
    TrieNode() : child{nullptr, nullptr}, val(-1) {}
};

TrieNode* trie = new TrieNode();

void insert_num(int idx) {
    TrieNode* cur = trie;
    for (int bit = MN - 1; bit >= 0; --bit) {
        bool i = arr[idx] & (1 << bit);
        if (!cur->child[i])
            cur->child[i] = new TrieNode();
        cur = cur->child[i];
    }
    cur->val = idx;
}

int get_min() {
    TrieNode* cur = trie;
    for (int bit = MN - 1; bit >= 0; --bit) {
        if (cur->child[flipped[bit]])
            cur = cur->child[flipped[bit]];
        else
            cur = cur->child[flipped[bit] ^ 1];
    }
    return cur->val;
}

int main() {
    cin >> N >> Q;
    for (int i = 0; i < N; ++i)
        cin >> arr[i];
    for (int i = N - 1; i >= 0; --i)
        insert_num(i);

    while (Q--) {
        cin >> x;
        for (int bit = 0; bit < MN; ++bit)
            if (x & (1 << bit))
                flipped[bit] ^= 1;
        cout << get_min() << "\n";
    }
    return 0;
}
