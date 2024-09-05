/*
https://dmoj.ca/problem/year2018p4

Intro to Digit DP
Keeping track of only R and using f(R) - f(L-1)

States in digit dp:
- [main state]: eg. digit sum, value % M, etc.
- [digit index]: which digit of the number we are currently at
- [under limit?]: if true, it means that we can put anything we want for the next digit
                  else, we can only put a number <= the i-th digit of `X`

Note that the number of distinct digit sums is at most 9*log10(MAX) ~ 162
dp state: [digit sum][digit index][under limit?]: numbers with this property
*/

#include <bits/stdc++.h>
#define int long long

using namespace std;

const int MN = 170;
int dp[MN][20][2];
string num;

int solve(int goal_sum, int d_sum, int idx, bool anything) {
    if (idx >= num.size()) {
        return d_sum == goal_sum;
    }
    if (dp[d_sum][idx][anything] != -1) {
        return dp[d_sum][idx][anything];
    }
    int total = 0;
    for (int next_digit = 0; next_digit < 10; ++next_digit) {
        if (anything) {
            total += solve(goal_sum, d_sum + next_digit, idx + 1, true);
        } else {
            int num_digit = num[idx] - '0';
            if (next_digit > num_digit) {
                continue;
            } else if (next_digit == num_digit) {
                total += solve(goal_sum, d_sum + next_digit, idx + 1, false);
            } else {
                total += solve(goal_sum, d_sum + next_digit, idx + 1, true);
            }
        }
    }
    return dp[d_sum][idx][anything] = total;
}

signed main() {
    int L, R;
    cin >> L >> R;
    int d_sums = 0;
    for (int i = 0; i < MN; ++i) {
        memset(dp, -1, sizeof(dp));
        num = to_string(R);
        int countR = solve(i, 0, 0, false);
        memset(dp, -1, sizeof(dp));  // reset dp
        num = to_string(L - 1);
        int countL = solve(i, 0, 0, false);
        if (countR - countL > 0) {
            d_sums += 1;
        }
    }
    cout << d_sums << "\n";
    return 0;
}
