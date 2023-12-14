// https://dmoj.ca/problem/lazy
// Min lazy segment tree with both set element to val and update by difference
// - update by diff stack on top of each other and many updates can be done at once using lazy propagation
// - update to val overrides all previous updates
//
// (Lesson learned: when you get stuck, come back to it later)

#include <bits/stdc++.h>

using ll = long long;
using namespace std;

const ll inf = 9223372036854775807;

class LazySegTree {
    vector<ll> seg, lazy, lazy2;  // lazy 1 does difference update, lazy 2 does value update
    ll size;
    ll default_val = inf;

    ll f(ll x, ll y) { return min(x, y); }

    inline void push_down(ll i, ll segment_size) {
        if (lazy2[i] != 0) {  // push down value
            lazy2[i * 2] = lazy2[i];
            lazy2[i * 2 + 1] = lazy2[i];
            seg[i * 2] = lazy2[i];
            seg[i * 2 + 1] = lazy2[i];
            lazy[i * 2] = 0;  // override previous updates by difference
            lazy[i * 2 + 1] = 0;
            lazy2[i] = 0;
        }
        if (lazy[i] != 0) {  // push down the difference normally
            lazy[i * 2] += lazy[i];
            lazy[i * 2 + 1] += lazy[i];
            seg[i * 2] += lazy[i];
            seg[i * 2 + 1] += lazy[i];
            lazy[i] = 0;
        }
    }

public:
    LazySegTree(vector<int> &arr) {
        ll N = arr.size();
        size = pow(2, ceil(log2(N)));
        seg.assign(2 * size, default_val);
        lazy.assign(2 * size, 0);
        lazy2.assign(2 * size, 0);

        for (ll i = 0; i < N; i++)
            seg[size + i] = arr[i];
        for (ll i = size - 1; i > 0; i--)
            seg[i] = f(seg[i * 2], seg[i * 2 + 1]);
    }

    void update(int i, int l, int r, int cur_l, int cur_r, int diff, bool operation) {
        if (cur_r < l || r < cur_l)
            return;
        ll mid = (cur_l + cur_r) / 2;
        if (l <= cur_l && cur_r <= r) {
            if (operation == 0) {  // update by difference
                lazy[i] += diff;
                seg[i] += diff;
            } else {
                lazy2[i] = diff;  // update to value
                seg[i] = diff;
                lazy[i] = 0;   // override previous updates by difference
            }
            return;
        }
        push_down(i, cur_r - mid);
        update(i * 2, l, r, cur_l, mid, diff, operation);
        update(i * 2 + 1, l, r, mid + 1, cur_r, diff, operation);
        seg[i] = f(seg[i * 2], seg[i * 2 + 1]);
    }

    ll query(int i, int l, int r, int cur_l, int cur_r) {
        if (cur_r < l || r < cur_l)
            return default_val;
        if (l <= cur_l && cur_r <= r)
            return seg[i];

        ll mid = (cur_l + cur_r) / 2;
        push_down(i, cur_r - mid);
        return f(query(i * 2, l, r, cur_l, mid),
                 query(i * 2 + 1, l, r, mid + 1, cur_r));
    }

    ll query_range(int l, int r) {
        return query(1, l, r, 0, size - 1);
    }

    void update_range(int l, int r, int diff, bool operation) {
        update(1, l, r, 0, size - 1, diff, operation);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    vector<int> arr(N);
    for (int i = 0; i < N; i++)
        cin >> arr[i];
    LazySegTree seg(arr);

    int q, l, r, val;
    while (Q--) {
        cin >> q >> l >> r;
        l--;
        r--;
        if (q == 1) {
            cin >> val;
            seg.update_range(l, r, val, false);  // update by difference
        } else if (q == 2) {
            cin >> val;
            seg.update_range(l, r, val, true);  // update to val
        } else {
            cout << seg.query_range(l, r) << "\n";  // query min
        }
    }
    return 0;
}
