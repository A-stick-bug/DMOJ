// https://dmoj.ca/problem/bsfast
// find index of first element strictly less than K
// traverse down the seg tree in log(n) to do this
// first check if we can go down the left path because it is earlier

#include <bits/stdc++.h>
using namespace std;

const int INF = 1 << 30;

int minf(int a, int b){
    return min(a,b);
}

struct SegTree {
    vector<int> seg;
    int N;
    function<int(int, int)> f;
    int default_val;

    SegTree(vector<int>& arr, function<int(int, int)> f, int default_val) : f(f), default_val(default_val) {
        int layers = ceil(log2(arr.size()));
        N = 1 << layers;
        seg.resize(1 << (layers + 1), default_val);
        for (int i = 0; i < arr.size(); i++) {
            seg[N + i] = arr[i];
        }
        for (int i = N - 1; i > 0; i--) {
            seg[i] = f(seg[i * 2], seg[i * 2 + 1]);
        }
    }

    void update(int i, int val) {
        i += N;
        seg[i] = val;
        while (i > 1) {
            i /= 2;
            seg[i] = f(seg[i * 2], seg[i * 2 + 1]);
        }
    }

    int query(int i, int l, int r, int cur_l, int cur_r, int k) {
        if (cur_r < l || r < cur_l || seg[i] >= k) {
            return -1;
        }
        if (cur_l == cur_r) {
            return cur_l;
        }
        int mid = (cur_l + cur_r) / 2;
        int left = query(i * 2, l, r, cur_l, mid, k);
        if (left != -1) {
            return left;
        }
        return query(i * 2 + 1, l, r, mid + 1, cur_r, k);
    }

    int query_range(int l, int r, int k) {
        return query(1, l, r, 0, N - 1, k);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    cin >> N >> Q;
    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    SegTree seg(arr,  minf, INF);

    int ans = 0;
    for (int _ = 0; _ < Q; _++) {
        int type;
        cin >> type;
        if (type == 1) {
            int i, val;
            cin >> i >> val;
            i = (i ^ ans) - 1;
            val ^= ans;
            seg.update(i, val);
        } else {
            int l, r, k;
            cin >> l >> r >> k;
            l = (l ^ ans) - 1;
            r = (r ^ ans) - 1;
            k ^= ans;
            ans = seg.query_range(l, r, k) + 1;
            cout << ans << "\n";
        }
    }

    return 0;
}
