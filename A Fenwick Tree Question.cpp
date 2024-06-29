// https://dmoj.ca/problem/olyrim2
// Key observation: handle each bit of a number separately and multiply by respective
//                  power of 2 when summing to get answer
// Make Fenwick trees for every bit (32 total)
//
// Example: 0 1 0 0 1
// OR of all pairs = pair a 1 with anything else to get 1 -> (# of 1)*(length-1) - (duplicates)
// AND = only get 1 by pairing up two 1s -> NC2 -> (# of 1)*(# of 1 minus 1)/2
// XOR = get 1 by pairing up 0 with 1 -> ones*zeros -> (# of 1)*(length - (# of 1))
//
// note: array is 0-indexed and BIT is 1-indexed

#include <bits/stdc++.h>

#define ll long long

using namespace std;

const int MN = 32;

class FenwickTree {
public:
    vector<int> bit;
    int N;

    FenwickTree(int n) {
        N = n;
        bit = vector<int>(N + 1, 0);
    }

    FenwickTree(vector<int> &nums) {
        N = nums.size();
        bit.resize(N + 1);
        for (int i = 0; i < N; i++) {
            bit[i + 1] = nums[i];
        }
        for (int i = 1; i <= N; i++) {
            int j = i + (i & -i);
            if (j <= N) {
                bit[j] += bit[i];
            }
        }
    }

    void update(int i, int diff) {
        for (; i < bit.size(); i += i & -i) {
            bit[i] += diff;
        }
    }

    int query(int i) {
        int total = 0;
        for (; i > 0; i -= i & -i) {
            total += bit[i];
        }
        return total;
    }

    int query(int l, int r) {
        return query(r) - query(l - 1);
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    cin >> N >> Q;

    // create arrays for each bit position
    vector<vector<int>> arrs(MN, vector<int>(N, 0));
    for (int i = 0, num; i < N; i++) {
        cin >> num;
        for (int bit = 0; bit < MN; bit++) {
            if (num & (1 << bit))
                arrs[bit][i] = 1;
        }
    }
    vector<FenwickTree> bits(MN, FenwickTree(0));
    for (int i = 0; i < MN; i++) {
        bits[i] = FenwickTree(arrs[i]);
    }

    for (int _ = 0; _ < Q; _++) {
        int t, a, b;
        cin >> t >> a >> b;
        if (t == 1) {  // update all bits at this position
            for (int bit = 0; bit < MN; bit++) {
                if (arrs[bit][a - 1])  // check if we need to flip bit 1 -> 0
                    bits[bit].update(a, -(((1 << bit) & b) == 0));
                else
                    bits[bit].update(a, ((1 << bit) & b) != 0);
                arrs[bit][a - 1] = (b & (1 << bit)) != 0;  // update original array
            }
            continue;
        }

        ll total = 0;
        for (int bit = 0; bit < MN; bit++) {
            if (t == 2) {  // OR
                int ones = bits[bit].query(a, b);
                int le = b - a + 1;
                total += (1LL * ones * (le - 1) - 1LL * (ones) * (ones - 1) / 2) * (1 << bit);
            }
            else if (t == 3) {  // AND
                int ones = bits[bit].query(a, b);
                total += (1LL * (ones) * (ones - 1) / 2) * (1 << bit);
            }
            else {  // XOR
                int ones = bits[bit].query(a, b);
                int zeros = (b - a + 1) - ones;
                total += (1LL * ones * zeros) * (1 << bit);
            }
        }

        cout << total << "\n";
    }
    return 0;
}

/*
Example case:
first 4 queries: [0 1 0 0 1] -> [1 0 1 0 0]

5 7
0 1 0 0 1
1 1 1
1 2 0
1 5 0
1 3 1
2 1 5
3 1 5
4 1 5

7
1
6
*/
