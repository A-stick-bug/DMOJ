#include <bits/stdc++.h>
#define int long long
using namespace std;

class SqrtDecomp {
    vector<int> a, b, c;
    int len, block_count;

public:
    SqrtDecomp(vector<int>& input) {
        len = sqrt(input.size());
        this->a = input;
        this->a.resize(input.size() + len, 0);
        block_count = (input.size() / len) + 1;
        b.resize(block_count, 0);
        c.resize(block_count, 0);  // an additional c[block] is added when querying elements in block
        for (int i = 0; i < block_count; ++i) {  // compute block sums
            b[i] = accumulate(a.begin() + i * len, a.begin() + (i + 1) * len, 0);
        }
    }
    void update(int l, int r, int diff) {
        int c_l = (l / len) + 1;
        int c_r = (r / len) - 1;
        if (c_l > c_r) {  // doesn't cover any blocks
            for (int i = l; i <= r; ++i) {
                a[i] += diff;
                b[i / len] += diff;
            }
            return;
        }

        for (int i = c_l; i <= c_r; ++i) {  // update blocks
            c[i] += diff;
            b[i] += diff * len;
        }
        for (int i = l; i < c_l * len; ++i) {  // update individual cells
            a[i] += diff;
            b[c_l - 1] += diff;
        }
        for (int i = (c_r + 1) * len; i <= r; ++i) {
            a[i] += diff;
            b[c_r + 1] += diff;
        }
    }

    int query(int l, int r) {
        int c_l = (l / len) + 1;
        int c_r = (r / len) - 1;
        int sum = 0;

        if (c_l > c_r) {  // doesn't cover any blocks
            for (int i = l; i <= r; ++i) {
                sum += a[i] + c[i / len];
            }
            return sum;
        }

        for (int i = c_l; i <= c_r; ++i) {  // add value from blocks
            sum += b[i];
        }
        for (int i = l; i < c_l * len; ++i) {  // add value from individual cells
            sum += a[i] + c[c_l - 1];
        }
        for (int i = (c_r + 1) * len; i <= r; ++i) {
            sum += a[i] + c[c_r + 1];
        }
        return sum;
    }
};

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N, Q;
    cin >> M >> N >> Q;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
    }
    SqrtDecomp sq(a);

    for (int i = 0; i < Q; ++i) {
        int type;
        cin >> type;
        if (type == 1) {  // range update
            int l, r, x;
            cin >> l >> r >> x;
            sq.update(l - 1, r - 1, x);
        } else {
            int l, r;
            cin >> l >> r;
            cout << sq.query(l - 1, r - 1) % M << "\n";
        }
    }

    return 0;
}
