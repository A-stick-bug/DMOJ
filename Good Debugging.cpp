#include <bits/stdc++.h>
using namespace std;

class LazySegTree {
private:
    vector<int> seg, lazy;
    int size;
    int f(int x, int y) { return x + y; }
    int default_val = 0;

public:
    LazySegTree(int N) {
        int layers = ceil(log2(N));
        size = 1 << layers;
        seg.assign(2 * size, default_val);
        lazy.assign(2 * size, default_val);
        for (int i = 0; i < N; i++){
            seg[i+size]= 1;
        }
        for (int i = size-1; i > 0; i--){
            seg[i]=seg[i*2]+seg[i*2+1];
        }
    }

    void push_down(int i, int segment_size) {
        if (lazy[i] % 2 == 0) return;
        lazy[2*i] += lazy[i];
        lazy[2*i + 1] += lazy[i];
        seg[2*i] = segment_size - seg[2*i];
        seg[2*i + 1] = segment_size - seg[2*i + 1];
        lazy[i] = default_val;
    }

    void update(int i, int l, int r, int cur_l, int cur_r, int diff) {
        if (cur_r < l || r < cur_l) return;
        int mid = (cur_l + cur_r) / 2;
        if (l <= cur_l && cur_r <= r) {
            lazy[i] += diff;
            seg[i] = (cur_r - cur_l + 1) - seg[i];
            return;
        }
        push_down(i, cur_r - mid);
        update(2*i, l, r, cur_l, mid, diff);
        update(2*i + 1, l, r, mid + 1, cur_r, diff);
        seg[i] = f(seg[2*i], seg[2*i + 1]);
    }

    int query(int i, int l, int r, int cur_l, int cur_r, int broken) {
        if (seg[i] < broken) return -1;
        if (cur_l == cur_r) return cur_l;
        int mid = (cur_l + cur_r) / 2;
        push_down(i, cur_r - mid);
        int left = query(2*i, l, r, cur_l, mid, broken);
        if (left != -1) return left;
        return query(2*i + 1, l, r, mid + 1, cur_r, broken - seg[2*i]);
    }

    int query_range(int l, int r, int broken) {
        return query(1, l, r, 0, size - 1, broken);
    }

    void update_range(int l, int r, int diff) {
        update(1, l, r, 0, size - 1, diff);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, L;
    cin >> N >> M >> L;

    LazySegTree seg(N);

    for (int i = 0; i < M; i++) {
        int l, r;
        cin >> l >> r;
        seg.update_range(l - 1, r - 1, 1);
        int broke = seg.query_range(0, N - 1, L);
        if (broke == -1) {
            cout << "AC?" << "\n";
        } else {
            cout << broke + 1 << "\n";
        }
    }

    return 0;
}
