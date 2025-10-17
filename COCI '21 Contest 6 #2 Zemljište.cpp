#include <bits/stdc++.h>
#define int long long
using namespace std;

const int MAXN = 505;
int N, M, A, B;
int grid[MAXN][MAXN];
int psa[MAXN][MAXN];

int query(int r1, int c1, int r2, int c2) {
    return psa[r2][c2] - psa[r2][c1 - 1] - psa[r1 - 1][c2] + psa[r1 - 1][c1 - 1];
}

signed main() {
    cin >> N >> M >> A >> B;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> grid[i][j];
            psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + grid[i][j];
        }
    }

    int best = 100000000000;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            for (int r = i; r <= N; r++) {
                int low = j, high = M;
                while (low <= high) {
                    int mid = (low + high) / 2;
                    if (query(i, j, r, mid) >= B) {
                        high = mid - 1;
                    } else {
                        low = mid + 1;
                    }
                }

                for (int m = max(1LL, low - 1); m <= min(M, low + 1); m++) {
                    int q = query(i, j, r, m);
                    best = min(best, abs(A - q) + abs(B - q));
                }
            }
        }
    }

    cout << best << "\n";
    return 0;
}