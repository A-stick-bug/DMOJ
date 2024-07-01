// https://dmoj.ca/problem/oly21practice9
// requires stupid constant time optimizations, check python code for explanations

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <bits/stdc++.h>
using namespace std;

const int MN = 2001;
int R, C;
int arr[MN][MN];
int largest;

bool works(int arr[MN][MN], int diff) {
    int marked[MN][MN] = {0};
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (largest - arr[i][j] > diff) {
                marked[i + 1][j + 1] = 1;
            }
        }
    }

    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            marked[i][j] += marked[i - 1][j] + marked[i][j - 1] - marked[i - 1][j - 1];
        }
    }

    int marked_cnt = 0;
    for (int i = 1; i <= R; i++) {
        for (int j = 1; j <= C; j++) {
            if (marked[i][j] != 0) {
                marked_cnt++;
            }
        }
    }

    if (marked_cnt == 0) {
        return true;
    }

    int small = INT_MAX, big = INT_MIN;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (marked[i + 1][j + 1]) {
                small = min(small, arr[i][j]);
                big = max(big, arr[i][j]);
            }
        }
    }
    return big - small <= diff;
}

bool check(int diff) {
    int cop[MN][MN];
    memcpy(cop, arr, sizeof(arr));
    if (works(cop, diff)) return true;
    reverse(cop, cop + R);
    if (works(cop, diff)) return true;
    for (int i = 0; i < R; i++)
        reverse(cop[i], cop[i] + C);
    if (works(cop, diff)) return true;
    reverse(cop, cop + R);
    if (works(cop, diff)) return true;
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> arr[i][j];
        }
    }

    largest = -1;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            largest = max(largest, arr[i][j]);
        }
    }

    int low = 0, high = 1e9;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (check(mid)) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << low << endl;

    return 0;
}
