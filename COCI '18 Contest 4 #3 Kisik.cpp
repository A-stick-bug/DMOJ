/*
https://dmoj.ca/problem/coci18c4p3
Greedy, optimized with data structures

Take the min of the following:
- For every possible height, we take the min width and multiply them

Note: this solution is bad, you should be using priority queue
*/

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

#define int long long
#define pii pair<int, int>
typedef tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long inf = 1LL << 60;
    int N, K;
    cin >> N >> K;

    vector<pair<int, int>> arr(N);
    for(int i = 0; i < N; i++)
        cin >> arr[i].first >> arr[i].second;

    sort(arr.begin(), arr.end());
    long long width = 0;  // width of K thinnest items
    for(int i = 0; i < K; i++)
        width += arr[i].first;

    vector<pair<int, int>> by_h(arr);  // sort by height for greedy
    sort(by_h.rbegin(), by_h.rend(), [](pii a, pii b) {
        return a.second < b.second;
    });

    arr.push_back({inf, inf});  // padding to prevent index error
    long long best = inf;
    ordered_set os;  // make an SortedList by width
    for(auto &p : arr)
        os.insert(p);

    for(int i = 0; i <= N - K; i++) {
        auto it = os.lower_bound(by_h[i]);
        int idx = os.order_of_key(*it);

        if(idx >= K)  // include the tallest in the width
            best = min(best, (width - (*os.find_by_order(K - 1)).first + by_h[i].first) * by_h[i].second);
        else {  // tallest is already in the width, replace it after
            best = min(best, width * by_h[i].second);
            width -= by_h[i].first;
            width += (*os.find_by_order(K)).first;
        }
        os.erase(it);
    }
    cout << best << "\n";
    return 0;
}
