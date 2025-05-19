// https://dmoj.ca/problem/scb24p4
// Brute force with bitmask
// Notice how fast C++ is at these bit operations
// TC: O(2^2m)

#include <bits/stdc++.h>

using namespace std;

const int M_EXP = 1 << 12;
int cnt[M_EXP];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K;

    for (int i = 0; i < N; i++) {  // store frequency of each bitmask
        string binary_str;
        cin >> binary_str;
        cnt[stoi(binary_str, nullptr, 2)]++;
    }

    int best = 0;
    for (int ans = 0; ans < M_EXP; ans++) {  // try all possible answer keys
        int cur = 0;
        for (int mask = 0; mask < M_EXP; mask++) {  // match answer key with all responses
            if (__builtin_popcount(ans ^ mask) <= M - K) {  // check if person passed
                cur += cnt[mask];
            }
        }
        best = max(best, cur);
    }

    cout << best << "\n";

    return 0;
}