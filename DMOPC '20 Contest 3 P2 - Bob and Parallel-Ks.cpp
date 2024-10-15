/*
 https://dmoj.ca/problem/dmopc20c3p2
 Check all adjacent beats one by one
 Just use unordered_map for everything

 - If your code TLEs, try using .reserve(number of element that will be in the map)

 runtimes:
 - unordered_map: 1.9s
 - unordered_map with .reserve(): 1.4s
 - gp_hash_table: 1.7s
 */

#include <bits/stdc++.h>

using namespace std;

int M, N, K;

int solve(vector<int> &a1, vector<int> &a2) {
    unordered_map<int, vector<int>> diff;
    diff.reserve(M);
    for (int i = 0; i < M; i++)  // parallel-K can only be formed if the difference is the same
        diff[a1[i] - a2[i]].push_back(a1[i]);

    int match = 0;
    for (auto [_, group]: diff) {
        unordered_set<int> freq(group.begin(), group.end());
        for (int i: group)  // check how many pairs of interval `K` we have
            match += freq.find(i + K) != freq.end();
    }
    return match;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> M >> N >> K;
    vector<vector<int>> arr(N);
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            int note;
            cin >> note;
            arr[j].push_back(note);
        }
    }

    int total = 0;
    for (int i = 0; i < N - 1; i++) {
        total += solve(arr[i], arr[i + 1]);
    }
    cout << total << '\n';
    return 0;
}
