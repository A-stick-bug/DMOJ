#include <bits/stdc++.h>
#define int long long
using namespace std;

class FenwickTree {
public:
    vector<int> bit;
    int n;

    FenwickTree(int n) {
        this->n = n + 1;
        bit.assign(n + 1, 0);
    }

    int sum(int r) {
        int ret = 0;
        for (; r >= 1; r -= (r & -r))
            ret += bit[r];
        return ret;
    }

    void add(int idx, int delta) {
        for (; idx < n; idx += (idx & -idx))
            bit[idx] += delta;
    }
};

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, P;
    cin >> N;
    vector<int> arr(N);
    for (int i = 0; i < N; i++)
        cin >> arr[i];
    cin >> P;

    for (int i = 0; i < N; i++)
        arr[i] -= P;

    vector<int> ss = {0};
    partial_sum(arr.begin(), arr.end(), back_inserter(ss));
    sort(ss.begin(), ss.end());
    ss.erase(unique(ss.begin(), ss.end()), ss.end());

    FenwickTree bit(ss.size());
    bit.add(lower_bound(ss.begin(), ss.end(), 0) - ss.begin() + 1, 1);

    int total = 0;
    int cur_sum = 0;
    for (int cur : arr) {
        cur_sum += cur;
        int idx = lower_bound(ss.begin(), ss.end(), cur_sum) - ss.begin() + 1;
        total += bit.sum(idx);
        bit.add(idx, 1);
    }

    cout << total << "\n";
    return 0;
}
