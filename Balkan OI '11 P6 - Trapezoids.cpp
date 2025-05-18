// https://dmoj.ca/problem/bkoi11p6
// A bunch of data structures
// Segment tree + line sweep by earlier starting point, with heap and coordinate compression
// The idea is extremely similar to https://dmoj.ca/problem/aac1p6
// Heap and line sweep deals with the top 2 points, seg tree deals with the bottom 2

#include <bits/stdc++.h>
using namespace std;

static const int MOD = 30013;
using pii = pair<int,int>;

pii comb(const pii &l, const pii &r) {
    if (l.first == r.first)  // combine frequencies
        return { l.first, (l.second + r.second) % MOD };
    return max(l, r);
}

struct SegTree {
    int size;
    vector<pii> seg;
    SegTree(int n) {
        size = 1;
        while (size < n) size <<= 1;
        seg.assign(2 * size, {0, 0});
    }
    void update(int i, const pii &v) {
        i += size;
        seg[i] = v;
        for (i >>= 1; i > 0; i >>= 1) {
            seg[i] = comb(seg[i<<1], seg[i<<1|1]);
        }
    }
    pii query(int l0, int r0) {
        pii resL{0,0}, resR{0,0};
        for (int l = l0 + size, r = r0 + size + 1; l < r; l >>= 1, r >>= 1) {
            if (l & 1) { resL = comb(resL, seg[l++]); }
            if (r & 1) { resR = comb(seg[--r], resR); }
        }
        return comb(resL, resR);
    }
};

struct Item {  // for the heap
    int b, c, d;
    int val, freq;
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<array<int, 4>> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i][0] >> A[i][1] >> A[i][2] >> A[i][3];
    }
    sort(A.begin(), A.end(), [](auto &x, auto &y){ return x[0] < y[0]; });  // by A

    vector<int> coords;  // coordinate compression
    coords.reserve(2 * n);
    for (auto &t : A) {
        auto [a,b,c,d] = t;
        coords.push_back(c);
        coords.push_back(d);
    }
    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());
    int m = coords.size();

    unordered_map<int,int> compress;
    compress.reserve(m);
    for (int i = 0; i < m; i++) {
        compress[coords[i]] = i;
    }

    SegTree seg(m + 2);

    // min-heap by b
    auto cmp = [](auto &x, auto &y){ return x.b > y.b; };
    priority_queue<Item, vector<Item>, decltype(cmp)> pending(cmp);

    // process intervals
    for (auto [a, b, c, d] : A) {
        while (!pending.empty() && pending.top().b < a) {  // line sweep, add trapezoids ending before `a`
            auto [pb, pc, pd, pv, pf] = pending.top();
            pending.pop();
            seg.update(compress[pd], {pv, pf});
        }
        // query best up to c
        int ci = compress[c];
        auto [val, freq] = seg.query(0, ci);
        val += 1;
        freq = max(1, freq);
        pending.push({b, c, d, val, freq});
    }

    // clear up remaining trapezoids
    while (!pending.empty()) {
        auto [pb, pc, pd, pv, pf] = pending.top();
        pending.pop();
        seg.update(compress[pd], {pv, max(1, pf)});
    }

    auto [ans, freq] = seg.query(0, m+1);
    cout << ans << " " << freq << "\n";
    return 0;
}