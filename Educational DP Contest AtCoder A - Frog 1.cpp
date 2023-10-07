// https://dmoj.ca/problem/dpa
// template DP problem, get the current cost using previous costs

#include <bits/stdc++.h>

using namespace std;

int arr[100001], dp[100001];

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) cin >> arr[i];

    dp[0] = 0;  // base cases
    dp[1] = abs(arr[1] - arr[0]);

    int jump1, jump2;
    for (int i = 2; i < N; i++) {
        jump1 = dp[i - 1] + abs(arr[i] - arr[i - 1]);
        jump2 = dp[i - 2] + abs(arr[i] - arr[i - 2]);
        dp[i] = min(jump1, jump2);  // take the minimum of jumping from 2 cells before or 1 cell before
    }

    cout << dp[N - 1] << "\n";
    return 0;
}
