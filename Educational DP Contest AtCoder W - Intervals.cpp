// https://dmoj.ca/problem/dpw
// See original python version for commentary

#include <bits/stdc++.h>
#define ll long long
using namespace std;

struct Node {
    // fields go here, don't forget default values
    ll val = -(1LL << 60);
};

struct combine {
    Node operator()(const Node& l, const Node& r) {
        return Node{max(l.val, r.val)};
    }
};

template <typename Node, typename Lazy, typename Func>
class LazySegTree {
    int size;  // number of leaves allocated
    vector<Node> seg;
    vector<Lazy> lazy;
    Func combine;

    void push_down(int i) {  // custom function: must be changed every time according to Lazy
        if (lazy[i] == 0) return;
        lazy[2 * i] += lazy[i];
        seg[2 * i].val += lazy[i];
        lazy[2 * i + 1] += lazy[i];
        seg[2 * i + 1].val += lazy[i];
        lazy[i] = 0;
    }

    void update(int l, int r, Node val, int idx, int cur_l, int cur_r) {
        if (cur_r < l || cur_l > r) return;
        if (l <= cur_l && cur_r <= r) {
            seg[idx].val += val.val;
            lazy[idx] += val.val;
            return;
        }
        push_down(idx);
        int mid = (cur_l + cur_r) / 2;
        update(l, r, val, idx * 2, cur_l, mid);
        update(l, r, val, idx * 2 + 1, mid + 1, cur_r);
        seg[idx] = combine(seg[idx * 2], seg[idx * 2 + 1]);
    }

    Node query(int l, int r, int idx, int cur_l, int cur_r) {
        if (cur_r < l || cur_l > r) return Node{};
        if (l <= cur_l && cur_r <= r) return seg[idx];
        push_down(idx);
        int mid = (cur_l + cur_r) / 2;
        return combine(query(l, r, idx * 2, cur_l, mid),
                       query(l, r, idx * 2 + 1, mid + 1, cur_r));
    }

public:
    LazySegTree(int n) {
        size = 1;
        while (size < n)
            size *= 2;
        seg.resize(2 * size);
        lazy.resize(2 * size);
    }

    LazySegTree(const vector<Node>& arr): LazySegTree{arr.size()} {
        for (int i = 0; i < arr.size(); i++) {
            seg[i + size] = arr[i];
        }
        for (int i = size - 1; i > 0; i--) {
            seg[i] = combine(seg[2 * i], seg[2 * i + 1]);
        }
    }

    void update(int l, int r, Node val) {
        update(l, r, val, 1, 0, size - 1);
    }

    Node query(int l, int r) {
        return query(l, r, 1, 0, size - 1);
    }
};
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<array<int, 3>> events;
    for (int i = 0; i < M; i++) {
        int l, r, amt;
        cin >> l >> r >> amt;
        events.push_back({l, amt, -1});
        events.push_back({r + 1, -amt, l});
    }
    sort(events.begin(), events.end());

    vector<ll> dp(N + 1, 0);
    LazySegTree<Node, ll, combine> seg(vector<Node>(N + 1, Node{0}));

    int idx = 0;
    for (int i = 1; i <= N; i++) {
        while (idx < events.size() && events[idx][0] <= i) {
            int amt = events[idx][1];
            if (events[idx][2] == -1) {
                seg.update(0, i - 1, Node{amt});
            } else {
                int l = events[idx][2];
                seg.update(0, l - 1, Node{amt});
            }
            idx++;
        }

        dp[i] = seg.query(0, i - 1).val;
        seg.update(i, i, Node{dp[i]});
    }

    cout << *max_element(dp.begin(), dp.end()) << "\n";
}
