// https://dmoj.ca/problem/coci07c3p6
// Segment tree with lazy propagation
// - For each segment, we keep track of the occurrences of each digit
// - To update (and push down), we shift the digits 1 to the right, mod 10
// - To answer queries, we can get the sum of the digits using hte frequencies

#include <bits/stdc++.h>
using namespace std;

vector<int> shift(vector<int> arr, int amt) {
    amt = amt % 10;
    vector<int> result(arr.size());
    copy(arr.end() - amt, arr.end(), result.begin());
    copy(arr.begin(), arr.end() - amt, result.begin() + amt);
    return result;
}

vector<int> combine(vector<int> a1, vector<int> a2) {
    vector<int> result(a1.size());
    for (int i = 0; i < a1.size(); ++i) {
        result[i] = a1[i] + a2[i];
    }
    return result;
}

class LazySegTree {
public:
    vector<vector<int>> seg;
    vector<int> lazy;
    int size;
    vector<int> default_value;

    LazySegTree(vector<int> arr, vector<int> default_value) : default_value(default_value) {
        int layers = ceil(log2(arr.size()));
        size = 1 << layers;
        seg.resize(2 * size, default_value);
        lazy.resize(2 * size, 0);

        for (int i = 0; i < arr.size(); ++i) {
            seg[size + i][arr[i]] += 1;
        }
        for (int i = size - 1; i > 0; --i) {
            seg[i] = combine(seg[2 * i], seg[2 * i + 1]);
        }
    }

    void push_down(int i, int segment_size) {
        if (lazy[i] == 0) {
            return;
        }
        lazy[2 * i] += lazy[i];
        lazy[2 * i + 1] += lazy[i];
        seg[2 * i] = shift(seg[2 * i], lazy[i]);
        seg[2 * i + 1] = shift(seg[2 * i + 1], lazy[i]);
        lazy[i] = 0;
    }

    void update(int i, int l, int r, int cur_l, int cur_r, int diff) {
        if (cur_r < l || r < cur_l) {
            return;
        }
        int mid = (cur_l + cur_r) / 2;
        if (l <= cur_l && cur_r <= r) {
            lazy[i] += diff;
            seg[i] = shift(seg[i], diff);
            return;
        }
        push_down(i, cur_r - mid);
        update(2 * i, l, r, cur_l, mid, diff);
        update(2 * i + 1, l, r, mid + 1, cur_r, diff);
        seg[i] = combine(seg[2 * i], seg[2 * i + 1]);
    }

    vector<int> query(int i, int l, int r, int cur_l, int cur_r) {
        if (cur_r < l || r < cur_l) {
            return default_value;
        }
        if (l <= cur_l && cur_r <= r) {
            return seg[i];
        }
        int mid = (cur_l + cur_r) / 2;
        push_down(i, cur_r - mid);
        return combine(query(2 * i, l, r, cur_l, mid),
                       query(2 * i + 1, l, r, mid + 1, cur_r));
    }

    vector<int> query_range(int l, int r) {
        return query(1, l, r, 0, size - 1);
    }

    void update_range(int l, int r, int diff) {
        update(1, l, r, 0, size - 1, diff);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    cin >> N >> Q;
    vector<int> arr(N);
    for (int i = 0; i < N; ++i) {
        char digit;
        cin >> digit;
        arr[i] = digit - '0';
    }

    LazySegTree seg(arr, vector<int>(10, 0));

    for (int i = 0; i < Q; ++i) {
        int l, r;
        cin >> l >> r;
        l--; r--;  // convert to 0-indexing
        vector<int> freq = seg.query_range(l, r);
        int sum = 0;
        for (int i = 0; i < 10; ++i) {
            sum += freq[i] * i;
        }
        cout << sum << "\n";
        seg.update_range(l, r, 1);
    }

    return 0;
}
