// https://dmoj.ca/problem/coci07c3p5
// Digit DP, keeping track of both L, R
//
// Only iterate over valid states and states leading to valid ones
// states: [index of digit][current sum][touch L?][touch R?]: count
// touch L: whether the current number is a prefix of A
//
// note: `cur_num` always contains the smallest number satisfying the
//       current state since we iterate the digits 1-9 (it is NOT a state)

#include <bits/stdc++.h>

#define int long long

using namespace std;

const int MN = 16;  // max digits
const int MS = 136;  // max digit sum
int dp[MN][MS][2][2];

int sum_goal, A, B;
string str_A, str_B;
int mi = 1LL << 60;

void reset_dp() {
    for (int i = 0; i < MN; i++) {
        for (int j = 0; j < MS; j++) {
            dp[i][j][0][0] = -1;
            dp[i][j][1][0] = -1;
            dp[i][j][0][1] = -1;
            dp[i][j][1][1] = -1;
        }
    }
}

int solve(int idx, int sum, bool touch_l, bool touch_r, int cur_num) {
    if (idx >= str_B.size()) {  // out of digits
        if (sum == sum_goal) {  // found valid sum
            mi = min(mi, cur_num);
            return 1;
        }
        return 0;
    }
    if (dp[idx][sum][touch_l][touch_r] != -1) {  // cache
        return dp[idx][sum][touch_l][touch_r];
    }

    int ans = 0;
    int A_digit = str_A[idx] - '0';
    int B_digit = str_B[idx] - '0';
    int low = touch_l ? A_digit : 0;
    int high = touch_r ? B_digit : 9;

    for (int digit = low; digit <= high; digit++) {
        bool new_t_l = touch_l && (digit == A_digit);  // check if we are still touching l and r
        bool new_t_r = touch_r && (digit == B_digit);
        ans += solve(idx + 1, sum + digit, new_t_l, new_t_r, cur_num * 10 + digit);
    }
    return dp[idx][sum][touch_l][touch_r] = ans;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> A >> B >> sum_goal;
    str_A = to_string(A);
    str_B = to_string(B);
    str_A = string(str_B.size() - str_A.size(), '0') + str_A;  // leading zeros

    reset_dp();
    int ans = solve(0, 0, true, true, 0);

    cout << ans << "\n" << mi << "\n";

    return 0;
}
