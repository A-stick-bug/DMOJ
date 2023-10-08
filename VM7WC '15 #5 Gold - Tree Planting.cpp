// https://dmoj.ca/problem/vmss7wc15c5p3
// Using multiple Fenwick Trees on the (/) diagonal (NOT 2D bit)
// to get the (/) diagonal, we can use row+col

#include <bits/stdc++.h>

using namespace std;

const int MM = 4001, MOD = 1000000007;
int bit[MM][MM];  // each row is a separate BIT for the (row+col) diagonal, column is just normal 1D BIT

void update(int pos, int val, int diagonal) {
    for (int i = pos; i < MM; i += i & -i)
        bit[diagonal][i] += val;
}

int query(int pos, int diagonal) {
    int sum = 0;
    for (int i = pos; i > 0; i -= i & -i)
        sum += bit[diagonal][i];
    return sum;
}

int N;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    int t, row, col, x, d;
    int total = 0;
    for (int i = 0; i < N; i++) {
        cin >> t >> row >> col >> x;
        d = row + col;  // get the diagonal

        if (t == 1) {  // type 1: plant trees
            update(row, x, d);
        } else {  // type 2: query diagonal
            total = (total + query(row, d) - query(row - x - 1, d)) % MOD;
        }
    }
    cout << total << "\n";
    return 0;
}
