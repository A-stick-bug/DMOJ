// https://dmoj.ca/problem/dmpg18s5
// sqrt decomposition
// init: for each number, add its divisors to the corresponding block
// update: remove divisors of old number and add new
// query: divisors in blocks + number of divisible numbers outside of blocks

#include <bits/stdc++.h>
using namespace std;

vector<int> divisors(int n) {
    vector<int> divisors;
    for (int i = 1; i * i <= n; ++i) {
        if (n % i == 0) {
            divisors.push_back(i);
            if (i * i != n) {
                divisors.push_back(n / i);
            }
        }
    }
    return divisors;
}

vector<int> nums;
vector<vector<int>> blocks;
int width = 450;
int sqrtn;

void update(int i, int val) {
    int block = i / width;
    for (int div : divisors(nums[i])) {
        blocks[block][div]--;
    }
    nums[i] = val;
    for (int div : divisors(val)) {
        blocks[block][div]++;
    }
}

int query(int i, int j, int d) {
    int first = (i / width) + 1;
    int last = (j / width) - 1;
    int total = 0;

    if (first > last) {
        for (int v = i; v <= j; ++v) {
            total += nums[v] % d == 0;
        }
        return total;
    }

    for (int v = i; v < first * width; ++v) {
        total += nums[v] % d == 0;
    }
    for (int b = first; b <= last; ++b) {
        total += blocks[b][d];
    }
    for (int v = (last + 1) * width; v <= j; ++v) {
        total += nums[v] % d == 0;
    }
    return total;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    cin >> N >> Q;
    nums.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }

    sqrtn = (nums.size() / width) + 1;
    blocks = vector<vector<int>>(sqrtn, vector<int>(200001, 0));

    for (int i = 0; i < N; ++i) {
        for (int div : divisors(nums[i])) {
            blocks[i / width][div]++;
        }
    }

    for (int _ = 0; _ < Q; ++_) {
        int type;
        cin >> type;
        if (type == 1) {
            int i, j, d;
            cin >> i >> j >> d;
            cout << query(i - 1, j - 1, d) << "\n";
        } else {
            int i, val;
            cin >> i >> val;
            update(i - 1, val);
        }
    }
    return 0;
}
