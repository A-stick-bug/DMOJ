// https://dmoj.ca/problem/dmopc20c1p4
// Matrix exponentiation
//
// - Represent the current number of crabs of each age as a vector
// - Represent the transition from day n to day n+1 as a matrix
// - Use fast matrix exponentiation to compute result after N days
//
// TC: O(T^3 * log(N))

#include <bits/stdc++.h>
#define int long long
#define matrix vector<vector<int>>

using namespace std;

const int MOD = 1e9 + 7;

matrix multiply(const matrix& m2, const matrix& m1) {
    int n = m1.size();
    matrix res(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int tot = 0;
            for (int k = 0; k < n; k++) {
                tot += m1[k][j] * m2[i][k];  // j -> k -> i
                tot %= MOD;
            }
            res[i][j] = tot;
        }
    }
    return res;
}

matrix matrix_exp(matrix base, int p) {
    int n = base.size();
    matrix res(n, vector<int>(n));  // identity matrix
    for (int i = 0; i < n; i++)
        res[i][i] = 1;
    while (p > 0) {
        if (p % 2 == 1)
            res = multiply(base, res);
        base = multiply(base, base);
        p /= 2;
    }
    return res;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, mul, T, C;
    cin >> N >> mul >> T >> C;

    matrix A(T + 1, vector<int>(T + 1));  // day n -> day n+1, as a matrix
    for (int i = 1; i <= T; i++)
        A[i][i - 1] = 1;  // increase 'age' by 1
    A[0][T] = mul;  // adult (age=T) each create `mul` of age=0
    A[T][T] = 1;  // adults stay adults

    matrix A_n = matrix_exp(A, N - 1);

    int big = A_n[T][T];
    int small = 0;
    for (int i = 0; i < T; i++) {
        small += A_n[i][T];
        small %= MOD;
    }

    cout << C * (2 * big + small) % MOD << "\n";
    return 0;
}