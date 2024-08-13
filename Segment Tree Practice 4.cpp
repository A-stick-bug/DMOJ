/*
 https://dmoj.ca/problem/stp4
 Template Mo's algorithm
 Basically put the queries in a certain order such that you can
 go from 1 query to another in amortized sqrt(N) time

 TC: O(NsqrtN), assuming N=Q
 note: there's probably a more efficient method that I didn't think of
*/

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <bits/stdc++.h>

using namespace std;

const int SQRT = 1250;  // group size

int N, Q;
vector<int> arr;
vector<array<int, 3>> queries;
vector<int> ans;
vector<int> freq;
int once = 0;

inline void add_element(int val) {
    if (freq[val] == 0) {  // 0 -> 1
        once++;
    } else if (freq[val] == 1) {  // 1 -> 2
        once--;
    }
    freq[val]++;
}

inline void remove_element(int val) {
    if (freq[val] == 1) {  // 1 -> 0
        once--;
    } else if (freq[val] == 2) {  // 2 -> 1
        once++;
    }
    freq[val]--;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> Q;
    arr.resize(N + 1);
    queries.resize(Q);
    ans.resize(Q, -1);
    freq.resize(N + 1, 0);

    for (int i = 1; i <= N; ++i) {
        cin >> arr[i];
    }

    for (int i = 0; i < Q; ++i) {
        int l, r;
        cin >> l >> r;
        queries[i] = {l, r, i};
    }

    sort(queries.begin(), queries.end());  // sort and group by left
    int prev_r = 0;
    int prev_l = 1;

    for (int i = 0; i < Q; i += SQRT) {
        vector<array<int, 3>> group(queries.begin() + i, queries.begin() + min(i + SQRT, Q));
        if (i % 2 == 0) {  // ascending/descending optimization
            sort(group.begin(), group.end(),  [](array<int,3> &a, array<int,3> &b){
                return a[1] < b[1];
            });  // sort individual group by right
        } else {
            sort(group.begin(), group.end(),  [](array<int,3> &a, array<int,3> &b){
                return a[1] > b[1];
            });
        }

        for (const auto& q : group) {
            int l = q[0], r = q[1], idx = q[2];
            while (prev_r < r) {
                prev_r++;
                add_element(arr[prev_r]);
            }
            while (prev_r > r) {
                remove_element(arr[prev_r]);
                prev_r--;
            }
            while (prev_l < l) {
                remove_element(arr[prev_l]);
                prev_l++;
            }
            while (prev_l > l) {
                prev_l--;
                add_element(arr[prev_l]);
            }

            ans[idx] = once;
        }
    }

    for (int i = 0; i < Q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
