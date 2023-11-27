// https://dmoj.ca/problem/stp2
// boring and slow segment tree method
// check the python code for a much better and faster solution

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class SegTree {
private:
    int default_val;
    vector<int> seg;
    vector<int> first;
    int layers;
    int N;

public:
    SegTree(vector<int>& arr) {
        default_val = 1 << 30;
        layers = ceil(log2(arr.size()));
        N = 1 << layers;
        seg.resize(2 * N, default_val);
        first.resize(2 * N);
        for (int i = 0; i < arr.size(); i++) {
            seg[N + i] = arr[i];
        }
        for (int i = 0; i < first.size(); i++){
            first[i] = i;
        }
        for (int i = N - 1; i >= 1; i--) {
            if (seg[i * 2] <= seg[i * 2 + 1]) {
                seg[i] = seg[i * 2];
                first[i] = first[i * 2];
            }
            else {
                seg[i] = seg[i * 2 + 1];
                first[i] = first[i * 2 + 1];
            }
        }
    }

    void update(int i, int val) {
        i += 1 << layers;
        seg[i] = val;
        while (i > 1) {
            i /= 2;
            if (seg[i * 2] <= seg[i * 2 + 1]) {
                seg[i] = seg[i * 2];
                first[i] = first[i * 2];
            }
            else {
                seg[i] = seg[i * 2 + 1];
                first[i] = first[i * 2 + 1];
            }
        }
    }

    pair<int, int> query(int i, int l, int r, int tl, int tr) {
        if (l > r) {
            return make_pair(default_val, 0);
        }
        if (l == tl && r == tr) {
            return make_pair(seg[i], first[i]);
        }
        int tm = (tl + tr) / 2;
        pair<int, int> left = query(i * 2, l, min(r, tm), tl, tm);
        pair<int, int> right = query(i * 2 + 1, max(l, tm + 1), r, tm + 1, tr);
        if (left.first <= right.first) {
            return left;
        }
        else {
            return right;
        }
    }

    pair<int, int> query_range(int l, int r) {
        pair<int, int> res = query(1, l, r, 0, N - 1);
        return make_pair(res.first, res.second - N +1);
    }
};

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    SegTree seg(arr);
    for (int i = 0; i < Q; i++) {
        char q;
        int a, b;
        cin >> q >> a >> b;
        if (q == 'U') {
            seg.update(a - 1, b);
        }
        else {
            pair<int, int> result = seg.query_range(a - 1, b - 1);
            cout << result.first << " " << result.second << endl;
        }
    }
    return 0;
}
