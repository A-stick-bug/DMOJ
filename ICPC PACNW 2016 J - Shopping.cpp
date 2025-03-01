/*
https://dmoj.ca/problem/pacnw16j

Observations:
- for each i in [l,r] we do cur %= arr[i]
- at most log(10^18) ~ 60 of these operations actually reduce the number
  since each time the number is at least halved

Implement a structure that can do "find earliest element <= `x` starting from `l`"
- Binary search + rmq sparse table -> total of 60*log(N) per query
- Turns out to have a really good constant factor, passing in under 0.4 seconds
 */

#include <bits/stdc++.h>
#define int long long

using namespace std;

const int LOG = 19;
const int MN = 200001;
int st[LOG][MN];

void build_st(const vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++)  // base layer
        st[0][i] = arr[i];
    for (int h = 1; h < LOG; h++)
        for (int i = 0; i < n - (1 << h) + 1; i++)
            st[h][i] = min(st[h - 1][i], st[h - 1][i + (1 << (h - 1))]);  // combine function goes here
}

int query(int l, int r){
    int h = __lg(r - l + 1);
    return min(st[h][l], st[h][r - (1 << h) + 1]);  // combine function goes here
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    vector<int> arr(N);
    for (int i = 0; i < N; i++){
        cin >> arr[i];
    }

    build_st(arr);

    while (Q--) {
        int val, l, r;
        cin >> val >> l >> r;
        l--; r--;

        int idx = l;
        while (idx <= r and val > 0) {
            val %= arr[idx];

            // search for earliest index `i` where `arr[i] <= val`
            int nxt_idx = N;
            int low = idx, high = N;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (query(idx, mid) <= val) {
                    nxt_idx = mid;
                    high = mid - 1;
                }
                else {
                    low = mid + 1;
                }
            }

            idx = nxt_idx;  // move to earliest smaller index
        }
        cout << val << "\n";
    }

    return 0;
}
