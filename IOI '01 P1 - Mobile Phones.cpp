/*
https://dmoj.ca/problem/ioi01p1

2D Fenwick tree with basic query and update operations
- queries are 0-indexed, change to 1-indexing

*/

#include <bits/stdc++.h>
using namespace std;

class BIT_2D {
    int ROWS, COLS;
    vector<vector<int>> bit;

public:
    BIT_2D(int r, int c) : ROWS(r), COLS(c), bit(r + 1, vector<int>(c + 1)) {}

    void update(int r, int c, int diff) {
        for (; r <= ROWS; r += r & -r)
            for (int col = c; col <= COLS; col += col & -col)
                bit[r][col] += diff;
    }

    int query(int r, int c) {
        int total = 0;
        for (; r > 0; r -= r & -r)
            for (int col = c; col > 0; col -= col & -col)
                total += bit[r][col];
        return total;
    }

    int query_range(int r1, int c1, int r2, int c2) {
        return query(r2, c2) - query(r1 - 1, c2) - query(r2, c1 - 1) + query(r1 - 1, c1 - 1);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int _, N;
    cin >> _ >> N;
    BIT_2D bit(N, N);

    while (true) {
        int q;
        cin >> q;
        if (q == 3)
            break;

        if (q == 1) {  // update operation
            int r, c, diff;
            cin >> r >> c >> diff;
            bit.update(r + 1, c + 1, diff);
        } else if (q == 2) {
            int r1, c1, r2, c2;
            cin >> r1 >> c1 >> r2 >> c2;
            cout << bit.query_range(r1 + 1, c1 + 1, r2 + 1, c2 + 1) << "\n";
        }
    }

    return 0;
}
