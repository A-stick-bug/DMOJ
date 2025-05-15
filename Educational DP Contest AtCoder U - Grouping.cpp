/*
 https://dmoj.ca/problem/dpu
 - Bitmask DP with submask iteration
 - The O3 optimization pragma is extremely important here

 TC: O(n * 3^n), calculated using binomial theorem
 note: can theoretically be optimized to O(3^n) using smart submask iteration

*/

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> arr(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> arr[i][j];

    int n_exp = 1 << n;
    vector<int> value(n_exp);  // precompute values gained from all groupings
    for (int mask = 0; mask < n_exp; mask++) {
        int res = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if ((mask & (1 << i)) && (mask & (1 << j)))
                    res += arr[i][j];
        value[mask] = res;
    }

    int inf = 1LL << 60;
    vector<int> dp(n_exp, -inf);
    dp[n_exp - 1] = 0;  // base case
    for (int taken = n_exp - 2; taken >= 0; taken--) {  // for each state, try each added grouping
        vector<int> available;
        for (int i = 0; i < n; i++)
            if (!(taken & (1 << i)))
                available.push_back(i);
        int m = available.size();
        int best = 0;
        for (int submask = 1; submask < (1 << m); submask++) {  // iterate subset of available bits
            int nxt_mask = 0;
            for (int i = 0; i < m; i++)
                if (submask & (1 << i))
                    nxt_mask |= (1 << available[i]);
            int new_taken = taken | nxt_mask;
            best = max(best, value[nxt_mask] + dp[new_taken]);
        }
        dp[taken] = best;
    }
    cout << dp[0] << "\n";
    return 0;
}
