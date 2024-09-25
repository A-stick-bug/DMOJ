// https://dmoj.ca/problem/bsspc22c1p8
// use a segment tree with lazy propagation and keep track of each color's count

#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1048576;
int seg[MAXN * 2][3];
int lazy[MAXN * 2];

void shiftAmount(int arr[3], int amt) {
    amt = amt % 3;
    int tmp[3];
    for (int i = 0; i < 3; i++) {
        tmp[i] = arr[i];
    }
    for (int i = 0; i < 3; i++) {
        arr[i] = tmp[(i - amt + 3) % 3];
    }
}

void combine(int a1[3], int a2[3], int res[3]) {
    for (int i = 0; i < 3; i++) {
        res[i] = a1[i] + a2[i];
    }
}

inline void push_down(int i) {
    if (lazy[i] == 0) return;
    lazy[i * 2] += lazy[i];
    lazy[i * 2 + 1] += lazy[i];
    shiftAmount(seg[i * 2], lazy[i]);
    shiftAmount(seg[i * 2 + 1], lazy[i]);
    lazy[i] = 0;
}

// update [l, r] by diff
void update(int i, int l, int r, int cur_l, int cur_r, int diff) {
    if (cur_r < l || r < cur_l) return;  // No overlap
    if (l <= cur_l && cur_r <= r) {  // Full overlap
        lazy[i] += diff;
        shiftAmount(seg[i], diff);
        return;
    }
    int mid = (cur_l + cur_r) / 2;
    push_down(i);
    update(i * 2, l, r, cur_l, mid, diff);
    update(i * 2 + 1, l, r, mid + 1, cur_r, diff);
    combine(seg[i * 2], seg[i * 2 + 1], seg[i]);
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    string arrStr, targetStr;
    cin >> arrStr >> targetStr;

    if (arrStr == targetStr){
        cout << 0 << "\n";
        return 0;
    }

    for (int i = 0; i < N; i++) {
        int arrValue = arrStr[i] == 'R' ? 0 : (arrStr[i] == 'G' ? 1 : 2);
        int targetValue = targetStr[i] == 'R' ? 0 : (targetStr[i] == 'G' ? 1 : 2);
        int diff = (targetValue - arrValue + 3) % 3;
        seg[MAXN + i][diff] += 1;
    }

    for (int i = MAXN - 1; i >= 1; i--) {
        combine(seg[i * 2], seg[i * 2 + 1], seg[i]);
    }

    int Q;
    cin >> Q;

    for (int i = 1; i <= Q; i++) {
        int l, r;
        cin >> l >> r;
        l--; r--;

        update(1, l, r, 0, MAXN - 1, 2);

        // cout << seg[1][0] << " " << seg[1][1] << " " << seg[1][2] << "\n";

        if (seg[1][0] == N) {
            cout << i << "\n";
            return 0;
        }
    }

    cout << -1 << "\n";
    return 0;
}
