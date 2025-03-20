// https://dmoj.ca/problem/acc3p4
// Lazy segment tree with custom function
// Geometric solution using rectangles and triangles
// Note: this can probably be simplified using some math tricks

#include <bits/stdc++.h>

#define int long long

using namespace std;

const int MN = 1048576;  // ~ceil(log2(n))
int seg[MN * 2];
int lazy[MN * 2];  // regular lazy tag
int tri[MN * 2];  // number of triangles on this segment

// omitted build function since all start at 0
// omitted default value since default is 0

inline void push_down(int idx, int le) {
    if (lazy[idx] == 0 and tri[idx] == 0)
        return;
    le /= 2;  // down a layer -> half the size

    // rectangle
    lazy[idx * 2] += lazy[idx];
    lazy[idx * 2 + 1] += lazy[idx];
    seg[idx * 2] += le * lazy[idx];
    seg[idx * 2 + 1] += le * lazy[idx];
    lazy[idx] = 0;

    // triangle
    tri[idx * 2] += tri[idx];
    seg[idx * 2] += tri[idx] * le * (le + 1) / 2;
    tri[idx * 2 + 1] += tri[idx];
    seg[idx * 2 + 1] += tri[idx] * le * (le + 1) / 2;
    lazy[idx * 2 + 1] += tri[idx] * le;
    seg[idx * 2 + 1] += tri[idx] * le * le;
    tri[idx] = 0;
}

void update(int l, int r, int val, int idx, int cur_l, int cur_r) {
    if (cur_r < l or r < cur_l)
        return;
    if (l <= cur_l and cur_r <= r) {  // lazy update
        int le = cur_r - cur_l + 1;
        lazy[idx] += val * (cur_l - l);  // rectangle
        seg[idx] += le * val * (cur_l - l);
        tri[idx] += val;  // triangle
        seg[idx] += val * le * (le + 1) / 2;
        return;
    }
    push_down(idx, cur_r - cur_l + 1);
    int mid = (cur_l + cur_r) / 2;
    update(l, r, val, idx * 2, cur_l, mid);
    update(l, r, val, idx * 2 + 1, mid + 1, cur_r);
    seg[idx] = seg[idx * 2] + seg[idx * 2 + 1];
}

int query(int l, int r, int idx, int cur_l, int cur_r) {
    if (cur_r < l or r < cur_l)
        return 0;
    if (l <= cur_l and cur_r <= r)
        return seg[idx];

    push_down(idx, cur_r - cur_l + 1);
    int mid = (cur_l + cur_r) / 2;
    return query(l, r, idx * 2, cur_l, mid) + query(l, r, idx * 2 + 1, mid + 1, cur_r);
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    while (Q--) {
        int t, l, r, v;
        cin >> t;
        if (t == 1) {
            cin >> l >> r >> v;
            l--; r--;
            update(l, r, v, 1, 0, MN - 1);
        } else {
            cin >> l >> r;
            l--; r--;
            cout << query(l, r, 1, 0, MN - 1) << "\n";
        }
    }
    return 0;
}