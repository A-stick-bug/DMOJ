// https://dmoj.ca/problem/dpb
// similar to Frog 1, except now, we can get to the current stone from more than 2 previous stones
// same logic, take the minimum cost to get here from all possible previous stones

#include <bits/stdc++.h>

using namespace std;

int arr[100001], dp[100001];
int INF = 2147483647;

int main() {
    int N, K;
    cin >> N >> K;

    for (int i = 0; i < N; i++) cin >> arr[i];

    int lowest;
    for (int i = 1; i < N; i++) {
        lowest = INF;
        for (int j = i - 1; j >= 0 && j >= i - K; j--) {  // get minimum of all possible previous stones
            lowest = min(lowest, dp[j] + abs(arr[i] - arr[j]));
        }
        dp[i] = lowest;
    }

    cout << dp[N - 1] << "\n";
    return 0;
}

