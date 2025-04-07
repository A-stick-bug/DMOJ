// https://dmoj.ca/problem/coci16c4p3
// almost same as https://leetcode.com/problems/tallest-billboard
// brute force memoization
// check Python version for smarter code

#include <bits/stdc++.h>
using namespace std;

const int MM = 200002;
const int offset = 100001;
const int MN = 501;
const int inf = 1 << 30;

int dp[501][MM];
int arr[MN];
int N;

int solve(int idx, int cur) {
    if (idx == N) {
        if (cur == 0) return 0;  // valid split
        else return -inf;
    }
    if (dp[idx][cur + offset] != -1)  // cache
        return dp[idx][cur + offset];

    int res = max({solve(idx + 1, cur),
                   solve(idx + 1, cur + arr[idx]) + arr[idx],
                   solve(idx + 1, cur - arr[idx]) + arr[idx]});
    return dp[idx][cur + offset] = res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    int total = 0;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        total += arr[i];
    }

    memset(dp, -1, sizeof(dp));
    int both = solve(0, 0) / 2;

    int diff = total - both * 2;
    cout << both + diff << "\n";

    return 0;
}
