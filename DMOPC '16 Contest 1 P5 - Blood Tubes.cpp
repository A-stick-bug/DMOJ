/*
https://dmoj.ca/problem/dmopc16c1p5

Inversion counting using Fenwick Tree
Also using a greedy algorithm

For each blood tube, put at the front or at the back, depending on which one creates fewer inversions
Doing this for every blood tube will give the fewest number of inversions at the end
(not sure why greedy works here, but it does, proof by AC 👍)
*/

#include <bits/stdc++.h>

using namespace std;

class FenwickTree {
public:
    vector<int> bit;
    int N;

    explicit FenwickTree(int n) {
        N = n;
        bit = vector<int>(N + 1, 0);
    }

    void update(int i, int diff) {
        while (i <= N) {
            bit[i] += diff;
            i += i & (-i);
        }
    }

    int query(int i) {
        int total = 0;
        while (i > 0) {
            total += bit[i];
            i -= i & (-i);
        }
        return total;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; ++i)
        cin >> arr[i];

    FenwickTree bit(N + 1);

    vector<int> freq(N, 0);
    for (int num: arr)
        freq[num - 1]++;

    long long inversions = 0;
    for (int num: arr) {
        int start = bit.query(num);
        int end = bit.query(N) - bit.query(num);  // bit.query(N) is how the total number of elements in bit
        bit.update(num, 1);
        inversions += min(start, end);
    }

    cout << inversions << "\n";

    return 0;
}