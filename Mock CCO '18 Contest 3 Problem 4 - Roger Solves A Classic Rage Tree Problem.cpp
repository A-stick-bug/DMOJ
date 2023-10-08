// https://dmoj.ca/problem/ncco3d2p1
// 1-indexed arrays and queries
//
// Template sparse table:
// query (max - min) in a range, build 2 sparse tables

#include <bits/stdc++.h>

using namespace std;

const int MM = 50005, layers = 16;
int N, Q, arr[MM];
int min_table[layers][MM], max_table[layers][MM];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> Q;
    for (int i = 1; i <= N; i++) cin >> arr[i];

    for (int i = 1; i <= N; i++) {  // fill sparse tables with base case
        min_table[0][i] = arr[i];
        max_table[0][i] = arr[i];
    }

    // create min and max sparse table
    for (int k = 1; k <= log2(N); k++)
        for (int i = 1; i + (1 << k) - 1 <= N; i++)
            min_table[k][i] = min(min_table[k - 1][i], min_table[k - 1][i + (1 << (k - 1))]);
    for (int k = 1; k <= log2(N); k++)
        for (int i = 1; i + (1 << k) - 1 <= N; i++)
            max_table[k][i] = max(max_table[k - 1][i], max_table[k - 1][i + (1 << (k - 1))]);

    // process queries
    int L, R;
    for (int i = 0; i < Q; i++) {
        cin >> L >> R;
        int k = log2(R - L + 1);  // greatest power of 2 less than or equal to k
        cout << max(max_table[k][L], max_table[k][R - (1 << k) + 1]) -
                min(min_table[k][L], min_table[k][R - (1 << k) + 1]) << "\n";
    }
}
