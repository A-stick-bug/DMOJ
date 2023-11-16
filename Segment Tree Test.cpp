// https://dmoj.ca/problem/ds3
// Segment tree for min and gcd queries
// Sqrt decomposition for frequency queries (number of elements equal to x in a range)

#include <bits/stdc++.h>

using namespace std;

int minFunc(int a, int b) {
    return min(a, b);
}

int gcdFunc(int a, int b) {
    return __gcd(a, b);
}


class SegTree {
    vector<int> seg;
    function<int(int, int)> f;
    int default_val, N;

public:
    SegTree(vector<int> &arr, function<int(int, int)> f, int default_val) : f(f), default_val(default_val) {
        int layers = ceil(log2(arr.size()));
        N = 1 << layers;
        seg.resize(N << 1, default_val);
        for (size_t i = 0; i < arr.size(); ++i)
            seg[i + N] = arr[i];
        for (int i = N - 1; i > 0; --i)
            seg[i] = f(seg[i << 1], seg[(i << 1) | 1]);
    }

    void update(int i, int val) {
        for (seg[i += N] = val; i > 1; i >>= 1)
            seg[i >> 1] = f(seg[i], seg[i ^ 1]);
    }

    int query(int l, int r) {
        int resl = default_val, resr = default_val;
        for (l += N, r += N; l <= r; l >>= 1, r >>= 1) {
            if (l & 1) resl = f(resl, seg[l++]);
            if (!(r & 1)) resr = f(seg[r--], resr);
        }
        return f(resl, resr);
    }
};

class Freq {
    vector<int> nums;
    vector<unordered_map<int, int>> blocks;
    int width;

public:
    Freq(vector<int> &nums) : nums(nums) {
        width = sqrt(nums.size());
        int block_count = (nums.size() / width) + 1;
        blocks.resize(block_count);
        for (size_t i = 0; i < nums.size(); ++i)
            blocks[i / width][nums[i]]++;
    }

    void update(int i, int val) {
        blocks[i / width][nums[i]]--;
        nums[i] = val;
        blocks[i / width][val]++;
    }

    int get_count(int i, int j, int x) {
        int first = (i / width) + 1;
        int last = (j / width) - 1;
        int count = 0;
        if (first > last) {
            for (int a = i; a <= j; a++) {  // frequency of x from i to j
                count += nums[a] == x;
            }
        } else {
            for (int k = first; k <= last; ++k)  // inside blocks
                count += blocks[k][x];
            for (int a = i; a < first * width; a++) {  // frequency of x before blocks
                count += nums[a] == x;
            }
            for (int a = (last + 1) * width; a <= j; a++) {  // frequency of x after blocks
                count += nums[a] == x;
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, Q;
    cin >> N >> Q;
    vector<int> arr(N);
    for (int i = 0; i < N; ++i)
        cin >> arr[i];

    SegTree min_tree(arr, minFunc, INT_MAX);
    SegTree gcd_tree(arr, gcdFunc, 0);
    Freq freq(arr);

    while (Q--) {
        char q;
        int a, b;
        cin >> q >> a >> b;

        if (q == 'C') {
            min_tree.update(a - 1, b);
            gcd_tree.update(a - 1, b);
            freq.update(a, b);
        } else if (q == 'M') {
            cout << min_tree.query(a - 1, b - 1) << '\n';
        } else if (q == 'G') {
            cout << gcd_tree.query(a - 1, b - 1) << '\n';
        } else {
            int val = gcd_tree.query(a - 1, b - 1);
            cout << freq.get_count(a - 1, b - 1, val) << '\n';
        }
    }
    return 0;
}
