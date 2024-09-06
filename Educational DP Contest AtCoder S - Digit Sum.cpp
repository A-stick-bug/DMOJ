/*
 * https://dmoj.ca/problem/dps
 * Simple Digit DP
 * states: [touch r?][current number % D][index]
 * value: numbers with the current prefix that equal 0 (mod D)
 *
 * TC: O(log10(K) * D)
 */

#include <bits/stdc++.h>

#define int long long
using namespace std;

const int MOD = 1e9 + 7, MN = 10001, MD = 101;
int D, N;
string K;
int dp[2][MD][MN];

int solve(bool touch_r, int mod_d, int idx) {
    if (idx >= K.size())  // finished constructing
        return mod_d == 0;
    if (dp[touch_r][mod_d][idx] != -1)  // cache
        return dp[touch_r][mod_d][idx];

    int ans = 0;
    int K_digit = K[idx] - '0';
    int high = touch_r ? K_digit : 9;  // make sure number is <=K

    for (int digit = 0; digit <= high; digit++) {
        bool new_t_r = touch_r && (digit == K_digit);  // still a prefix of K?
        ans += solve(new_t_r, (mod_d + digit) % D, idx + 1);
    }
    ans %= MOD;
    return dp[touch_r][mod_d][idx] = ans;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> K >> D;
    memset(dp, -1, sizeof(dp));

    int ans = (solve(true, 0, 0) - 1 + MOD) % MOD;  // 0 doesn't count
    cout << ans << "\n";

    return 0;
}
