// https://dmoj.ca/problem/dpc
// Simple DP
// for each day, for each activity, we take the maximum of the previous day's that is a different activity
// use the input array as dp array because we are doing +=

#include <bits/stdc++.h>

using namespace std;

int dp[100001][3];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int a = 0; a < 3; a++) {
            cin >> dp[i][a];
        }
    }

    for (int i = 1; i < N; i++) {  // maximum of previous day that is different activity
        dp[i][0] += max(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] += max(dp[i - 1][0], dp[i - 1][2]);
        dp[i][2] += max(dp[i - 1][0], dp[i - 1][1]);
    }

    // get maximum element in dp[N-1]
    cout << *max_element(dp[N - 1], dp[N - 1] + 3) << "\n";
    return 0;
}


