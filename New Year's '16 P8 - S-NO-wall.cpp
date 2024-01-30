/*
https://dmoj.ca/problem/year2016p8
longest contiguous segment with range updates, we also need to keep track of the indices of the longest
segment so we can remove it during type 2 queries

at each node we store:
- left most node covered by segment
- right most node covered by segment
- length of prefix ones
- length of suffix ones
- indices of [l, r] for the longest contiguous segment inside the current node

IMPORTANT:
- there doesn't exist a default that works for all empty segments since each segment have their own [L, R]
  therefore, we must create a default even for nodes that don't exist
- (in_l = 0) and (in_r = -1) for default segments as it represents a length 0 maximum segment

*/

#include <bits/stdc++.h>

#define pi pair<int, int>

using namespace std;


struct Node {
    int L, R, best_l, best_r, in_l, in_r;
};

Node combine(Node left, Node right) {
    int best_r = right.best_r;
    if (right.in_r == right.R && right.in_l == right.L) {
        best_r = (right.R - right.L + 1) + left.best_r;
    }

    int best_l = left.best_l;
    if (left.in_r == left.R && left.in_l == left.L) {
        best_l = (left.R - left.L + 1) + right.best_l;
    }

    // take l,r with largest range
    pi max_pair = max({make_pair(left.in_l, left.in_r),
                       make_pair(left.R - left.best_r + 1, right.L + right.best_l - 1),
                       make_pair(right.in_l, right.in_r)},
                      [&](pi a, pi b) { return (a.second - a.first) < (b.second - b.first); });

    Node res = {left.L, right.R, best_l, best_r, max_pair.first, max_pair.second};
    return res;
}

class LazySegTree {
    int size;
    vector<Node> seg;
    vector<int> lazy;

public:
    LazySegTree(int N) {
        int layers = ceil(log2(N));
        size = 1 << layers;
        seg.resize(2 * size);
        for (int i = 0; i < size; i++) {
            seg[size + i] = {i, i, 0, 0, 0, -1};
        }
        for (int i = size - 1; i > 0; i--) {
            seg[i] = combine(seg[i * 2], seg[i * 2 + 1]);
        }
        lazy.assign(2 * size, -1);
    }

    void push_down(int i, int L, int R) {
        if (lazy[i] == -1) {
            return;
        }
        lazy[i * 2] = lazy[i];
        lazy[i * 2 + 1] = lazy[i];
        int mid = (L + R) / 2;
        if (lazy[i] == 1) {  // everything on
            seg[i * 2] = {L, mid, mid - L + 1, mid - L + 1, L, mid};
            seg[i * 2 + 1] = {mid + 1, R, R - mid, R - mid, mid + 1, R};
        } else if (lazy[i] == 0) {  // everything off
            seg[i * 2] = {L, mid, 0, 0, 0, -1};
            seg[i * 2 + 1] = {mid + 1, R, 0, 0, 0, -1};
        }
        lazy[i] = -1;
    }

    void update(int i, int l, int r, int cur_l, int cur_r, int val) {
        if (cur_r < l || r < cur_l) {
            return;
        }
        int mid = (cur_l + cur_r) / 2;
        if (l <= cur_l && cur_r <= r) {
            lazy[i] = val;
            if (lazy[i] == 1) {  // everything on
                seg[i] = {cur_l, cur_r, cur_r - cur_l + 1, cur_r - cur_l + 1, cur_l, cur_r};
            } else if (lazy[i] == 0) {  // everything off
                seg[i] = {cur_l, cur_r, 0, 0, 0, -1};
            }
            return;
        }
        push_down(i, cur_l, cur_r);
        update(i * 2, l, r, cur_l, mid, val);
        update(i * 2 + 1, l, r, mid + 1, cur_r, val);
        seg[i] = combine(seg[i * 2], seg[i * 2 + 1]);
    }

    Node query(int i, int l, int r, int cur_l, int cur_r) {
        if (cur_r < l || r < cur_l) {
            return {cur_l, cur_r, 0, 0, 0, -1};
        }
        if (l <= cur_l && cur_r <= r) {
            return seg[i];
        }
        int mid = (cur_l + cur_r) / 2;
        push_down(i, cur_l, cur_r);
        return combine(query(i * 2, l, r, cur_l, mid), query(i * 2 + 1, l, r, mid + 1, cur_r));
    }

    Node query_range(int l, int r) {
        return query(1, l, r, 0, size - 1);
    }

    void update_range(int l, int r, int val) {
        update(1, l, r, 0, size - 1, val);
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    LazySegTree seg(N + 1);

    for (int i = 0; i < Q; i++) {
        int type;
        cin >> type;

        if (type == 0) {  // turn off
            int l, r;
            cin >> l >> r;
            seg.update_range(l, r, 0);
            Node ans = seg.query_range(1, N);
            cout << ans.in_r - ans.in_l + 1 << "\n";
        } else if (type == 1) {  // turn on
            int l, r;
            cin >> l >> r;
            seg.update_range(l, r, 1);
            Node ans = seg.query_range(1, N);
            cout << ans.in_r - ans.in_l + 1 << "\n";
        } else {  // get longest and remove it
            Node ans = seg.query_range(1, N);
            seg.update_range(ans.in_l, ans.in_r, 0);
        }
    }
    return 0;
}
