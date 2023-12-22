/*
 * https://dmoj.ca/problem/dmopc19c6p4
 *
 * Sqrt decomp with map optimizations:
 * - use map instead of unordered map
 * - don't create useless keys when getting count from blocks
 * - remove keys with value 0 when updating
 */

#pragma GCC optimize("O3")

#include <bits/stdc++.h>

using namespace std;

class Freq {  // sqrt decomp
    vector<int> nums;
    vector<map<int, int>> blocks;
    int width;

public:
    Freq(vector<int> &arr) {
        nums = arr;
        width = sqrt(arr.size());
        int block_count = (arr.size() / width) + 1;
        blocks.resize(block_count);
        for (size_t i = 0; i < arr.size(); ++i)
            blocks[i / width][arr[i]]++;
    }

    void update(int i, int diff) {
        int prev = nums[i];
        if (blocks[i / width][nums[i]] == 1)  // potential speedup: remove useless keys
            blocks[i / width].erase(nums[i]);
        else
            blocks[i / width][nums[i]]--;
        nums[i] = prev + diff;
        blocks[i / width][prev + diff]++;  // add updated element
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
            // only get the count if the number exists to not create useless keys
            for (int k = first; k <= last; ++k)
                if (blocks[k].find(x) != blocks[k].end())
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
    vector<int> arr(N, 0);  // everyone is originally at 0
    Freq freq(arr);

    int q, i, l, r, val;
    while (Q--) {
        cin >> q;
        if (q == 1) {  // increase by 1
            cin >> i;
            freq.update(i - 1, 1);

        } else if (q == 2) {  // decrease by 1
            cin >> i;
            freq.update(i - 1, -1);

        } else {  // get number of elements equal to val in a range
            cin >> l >> r >> val;
            cout << freq.get_count(l - 1, r - 1, val) << '\n';  // frequency query
        }
    }
    return 0;
}
