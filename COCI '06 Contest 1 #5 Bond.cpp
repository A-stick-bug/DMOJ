/*
 https://dmoj.ca/problem/coci06c1p5
 similar to https://dmoj.ca/problem/dpo

 Note: each person can only be arranged 1 mission
 We can use bitmask DP to keep track of already taken missions
 and store the maximum probability in each state
 dp[i][state]: currently on i-th person, state represents the missions already taken

 TC: O(2^n * n^2)
 note: you could remove a N factor by grouping numbers by (# of set bits)
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    int prob[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> prob[i][j];
        }
    }

    int MN = 1 << N;
    vector<double> prev(MN, 100);  // previous dp states
    vector<double> dp(MN, 0);


    for (int i = 0; i < N; i++){
        for (int state = 0; state < MN; state++){
            if (__builtin_popcount(state) != i + 1)  // number of taken tasks doesn't match
                continue;
            for (int bit = 0; bit < N; bit++){  // transition states
                if (state & (1 << bit))
                    dp[state] = max(dp[state], prev[state - (1 << bit)] * prob[i][bit] / 100);
            }
        }
        swap(dp, prev);
        fill(dp.begin(), dp.end(), 0);
    }
    cout << setprecision(9) << prev[MN - 1] << "\n";
    return 0;
}
