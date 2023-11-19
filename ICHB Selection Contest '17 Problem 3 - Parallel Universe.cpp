// https://dmoj.ca/problem/ichb2017p3
// template segment tree, use unsigned int instead of int to prevent overflow
// function is AND (&)

#include <bits/stdc++.h>
#define int unsigned int
using namespace std;

int AND(int a, int b) {  // functions for the segment tree
    return a & b;
}

class SegTree {
    vector<int> seg;
    function<int(int, int)> f;
    int N;
    int default_val;

public:
    SegTree(vector<int> &arr, function<int(int, int)> f, int default_val) : f(f), default_val(default_val) {
        int layers = ceil(log2(arr.size()));
        N = 1 << layers;
        seg.resize(N << 1, default_val);
        for (size_t i = 0; i < arr.size(); ++i)
            seg[i + N] = arr[i];
        for (int i = N - 1; i > 0; --i)
            seg[i] = f(seg[i << 1], seg[(i << 1) | 1]);
    }

    void update(int i, int val) {
        for (seg[i += N] = val; i > 1; i >>= 1)
            seg[i >> 1] = f(seg[i], seg[i ^ 1]);
    }

    int query(int l, int r) {
        int resl = default_val, resr = default_val;
        for (l += N, r += N; l <= r; l >>= 1, r >>= 1) {
            if (l & 1) resl = f(resl, seg[l++]);
            if (!(r & 1)) resr = f(seg[r--], resr);
        }
        return f(resl, resr);
    }
};

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, Q;
    cin >> N >> Q;
    vector<int> arr(N);
    for (int i = 0; i < N; ++i)
        cin >> arr[i];

    SegTree and_tree(arr, AND, 4294967295);

    while (Q--) {
        char q;
        int a, b, val;
        cin >> q;

        if (q == 'U') {  // update elements
            cin >> a >> b;
            and_tree.update(a - 1, b);
        } else {
            cin >> a >> b >> val;
            cout << AND(val, and_tree.query(a - 1, b - 1)) << '\n';  // min query
        }
    }
    return 0;
}
