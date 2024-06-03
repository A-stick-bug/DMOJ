/*
https://dmoj.ca/problem/bship
Easier version (sum instead of min) of https://dmoj.ca/problem/coci23c1p3

Notice that a 2D psa takes 2000*2000*4/1000000 = 16mb of memory which instantly MLEs
Instead, we can use a 2D sliding window
We store sum(grid[row][i:i+K]) for each row and we can shift each of these windows in O(1)
To get answer, we can do a sliding window sum on these row sums for all valid values i

TC: O(MN)
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

	int R, C, K;
	cin >> R >> C >> K;

	vector<vector<bool>> grid(R, vector<bool>(C));
    for (int i = 0; i < R; i++){
        for (int j = 0; j < C; j++){
            char cell;
            cin >> cell;
            grid[i][j] = cell == 'X';
        }
    }

    vector<int> row(C, 0);  // initialize sliding window sum on each row
    for (int i = 0; i < R; i++){
        row[i] = accumulate(grid[i].begin(), grid[i].begin() + K, 0);
    }

    long long total = 0;
    for (int j = 0; j + K - 1 < C; j++){
        // take sum of rows (area of squares)
        int row_sum = accumulate(row.begin(), row.begin() + K, 0);
        for (int i = 0; i + K - 1 < R; i++){
            total += row_sum;
            row_sum += row[i + K];  // update sliding window
            row_sum -= row[i];
        }

        // update row sums (area of slices on each row)
        for (int i = 0; i < R; i++){
            row[i] += grid[i][j + K];
            row[i] -= grid[i][j];
        }
    }
    cout << setprecision(12) << (double) total / ((R - K + 1) * (C - K + 1)) << "\n";
}
