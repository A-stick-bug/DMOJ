// https://dmoj.ca/problem/dpd
// template knapsack dp problem
// need to use long long to prevent overflow

#include <bits/stdc++.h>

using namespace std;

const int N_MAX = 101, W_MAX = 100001;
int N, W, val[N_MAX], weight[N_MAX] ;
long long dp[N_MAX][W_MAX];

long long solve(int i, int capacity) {
    if (i < 0) {  // base case
        return 0;
    }
    if (dp[i][capacity] != -1) {  // use previously calculated values
        return dp[i][capacity];
    }

    long long take = 0;
    if (capacity >= weight[i]) {  // we have enough space to take this item
        take = val[i] + solve(i - 1, capacity - weight[i]);
    }
    dp[i][capacity] = max(take, solve(i - 1, capacity));  // memoize, either take or don't take
    return dp[i][capacity];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> W;
    int w, v;
    for (int i = 0; i < N; i++) {  // take input
        cin >> w >> v;
        weight[i] = w;
        val[i] = v;
    }

    for (int i = 0; i <= N; i++) 
        for (int j = 0; j <= W; j++)
            dp[i][j] = -1;

    cout << solve(N - 1, W) << "\n";
    return 0;
}