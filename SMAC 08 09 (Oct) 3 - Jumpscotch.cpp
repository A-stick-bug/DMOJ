// https://dmoj.ca/problem/smac08c1p3
// Harder version of https://dmoj.ca/problem/dpb
//
// Calculate dp[i] by getting the minimum of previous D elements + arr[i]
// Because D can be large, we need a data structure to query the minimum element quickly
// A monotonic queue is perfect for doing this

#include <bits/stdc++.h>

using namespace std;

const int MN = 1000000;
int arr[MN], dp[MN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, D;
    cin >> N >> D;
    for (int i = 0; i < N; i++) {  // take input
        cin >> arr[i];
    }

    deque<int> q;  // q[0] will have the minimum element
    q.push_back(0);  // base cases
    dp[0] = arr[0];

    for (int i = 1; i < N; i++) {
        dp[i] = dp[q[0]] + arr[i];  // use queue to get minimum element

        while (!q.empty() && dp[i] <= dp[q[q.size() - 1]])  // strictly increasing queue for min
            q.pop_back();
        q.push_back(i);

        if (q[0] <= i - D)  // minimum element exits window
            q.pop_front();
    }

    cout << dp[N - 1] << "\n";
    return 0;
}