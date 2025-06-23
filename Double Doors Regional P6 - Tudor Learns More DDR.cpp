// https://dmoj.ca/problem/ddrp6
// direct translation of Python code, check that version for explanation

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

int encode(const string &s) {
    int res = 0;
    int pow4[3] = {1, 4, 16};
    for (int i = 0; i < (int)s.size(); i++) {
        res += (s[i] - '0') * pow4[i];
    }
    return res;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    if (n < 10){  // precompute small values to avoid edge cases
        int precomp[] = {-1, 4, 16, 64, 248, 968, 3776, 14728, 57448, 224080, 874040};
        cout << precomp[n] << "\n";
        return 0;
    }
    n -= 3;

    vector<string> states = {
        "000", "001", "002", "003", "010", "011", "012", "013", "020", "021", "022", "023", "030", "031", "032", "033",
        "100", "101", "102", "103", "110", "111", "112", "113", "120", "121", "122", "123", "130", "131", "132", "133",
        "200", "201", "202", "203", "210", "211", "212", "213", "220", "221", "222", "223", "230", "231", "232", "233",
        "300", "301", "302", "303", "310", "311", "312", "313", "320", "321", "322", "323", "330", "331", "332", "333"
    };

    matrix mat(64, vector<int>(64, 0));
    for (const string &cur : states) {
        for (char added : string("0123")) {
            string nxt = cur + added;
            if (string("0123012,0321032").find(nxt) != string::npos) {
                continue;
            }
            nxt = nxt.substr(nxt.size() - 3);
            mat[encode(cur)][encode(nxt)] += 1;
        }
    }

    matrix transition = matrix_exp(mat, n);
    matrix start(64, vector<int>(64, 0));
    for (const string &cur : states) {
        start[encode(cur)][0] += 1;
    }

    matrix res = multiply(transition, start);
    int ans = 0;
    for (const auto &row : res) {
        for (int v : row) {
            ans = (ans + v) % MOD;
        }
    }
    cout << ans << "\n";

    return 0;
}