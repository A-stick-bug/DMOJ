/*
https://dmoj.ca/problem/cheerio1s4

DP with transition optimization
Observation:
- if we are at an element containing X, we either go to the closest X+1 on the left or on the right
  - eg. [1,2,2,3] from 1, notice that going to the first or second 2 makes no difference
- we can store the indices that each element appear in and use binary search to find closest left/right

TC: O(nlogn)
*/

#include <bits/stdc++.h>
#define int long long
using namespace std;

const int INF = 1000000000000;
vector<int> locs[500005];
int cache[500005];

int solve(int idx, int arr[], int N, int M) {
    if (cache[idx] != -1) {
        return cache[idx];
    }
    if (arr[idx] == M) {  // finished
        return 0;
    }
    int nxt = arr[idx] + 1;
    int mid = lower_bound(locs[nxt].begin(), locs[nxt].end(), idx) - locs[nxt].begin();
    int right = (mid == locs[nxt].size()) ? INF : locs[nxt][mid];  // find X+1 on the right
    int left = (mid == 0) ? INF : locs[nxt][mid - 1];  // find X+1 on the left

    int ans = INF;  // take best answer from valid transitions
    if (0 <= left && left < N) {
        ans = min(ans, solve(left, arr, N, M) + abs(idx - left));
    }
    if (0 <= right && right < N) {
        ans = min(ans, solve(right, arr, N, M) + abs(idx - right));
    }
    cache[idx] = ans;
    return cache[idx];
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    int arr[N];
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        locs[arr[i]].push_back(i);  // locs[X] contains indices of X in order
    }
    fill(cache, cache+N, -1);
    int start = locs[1][0];
    cout << start + solve(start, arr, N, M) + 1 << "\n";  // add distance to go to first box

    return 0;
}
