/*
 https://dmoj.ca/problem/stnbd4
 - Mo's algorithm (sqrt decomp on queries)
 - Maintain a Fenwick Tree of the frequency of elements on the current range
   to update inversion count in log(n)

 TC: O(N*sqrt(N)*log(N)), assuming N=Q
*/

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <bits/stdc++.h>
#define ll long long

using namespace std;

class FenwickTree {
public:
    vector<int> bit;
    int n;

    FenwickTree(int n) : n(n) {
        bit.assign(n + 1, 0);
    }

    void update(int index, int delta) {
        for (; index <= n; index += index & -index)
            bit[index] += delta;
    }

    int query(int index) {
        int sum = 0;
        for (; index > 0; index -= index & -index)
            sum += bit[index];
        return sum;
    }

    int query_range(int left, int right) {
        return query(right) - query(left - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    const int SQRT = 900; // group size
    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; ++i)
        cin >> arr[i];

    // coordinate compression
    vector<int> ordered(arr);
    sort(ordered.begin(), ordered.end());
    ordered.erase(unique(ordered.begin(), ordered.end()), ordered.end());

    unordered_map<int, int> compress;
    for (int i = 0; i < ordered.size(); ++i)
        compress[ordered[i]] = i + 1;

    for (int i = 0; i < N; ++i)
        arr[i] = compress[arr[i]];

    int Q;
    cin >> Q;

    vector<array<int, 3>> queries(Q);
    vector<ll> ans(Q, -1);

    for (int i = 0; i < Q; ++i) {
        cin >> queries[i][0] >> queries[i][1];
        queries[i][2] = i;
    }

    int M = compress.size();
    FenwickTree bit(M);
    ll inversions = 0;

    sort(queries.begin(), queries.end()); // sort and group by left
    int prev_r = 0, prev_l = 1;

    for (int i = 0; i < Q; i += SQRT) {
        vector<array<int, 3>> group(queries.begin() + i, queries.begin() + min(i + SQRT, Q));

        if (i & 1) {  // ascending/descending optimization
            sort(group.begin(), group.end(), [](const array<int, 3>& a, const array<int, 3>& b) {
                return a[1] > b[1]; // sort by right, descending for odd groups
            });
        } else {
            sort(group.begin(), group.end(), [](const array<int, 3>& a, const array<int, 3>& b) {
                return a[1] < b[1]; // sort by right, ascending for even groups
            });
        }

        for (auto [l, r, idx] : group) {
            l -= 1; r -= 1;

            while (prev_r < r) { // extend right
                ++prev_r;
                bit.update(arr[prev_r], 1);
                inversions += bit.query_range(arr[prev_r] + 1, M);
            }

            while (prev_r > r) { // shrink right
                bit.update(arr[prev_r], -1);
                inversions -= bit.query_range(arr[prev_r] + 1, M);
                --prev_r;
            }

            while (prev_l < l) { // shrink left
                bit.update(arr[prev_l], -1);
                inversions -= bit.query(arr[prev_l] - 1);
                ++prev_l;
            }

            while (prev_l > l) { // extend left
                --prev_l;
                bit.update(arr[prev_l], 1);
                inversions += bit.query(arr[prev_l] - 1);
            }
            ans[idx] = inversions;
        }
    }

    for (int i = 0; i < Q; ++i)
        cout << ans[i] << "\n";

    return 0;
}