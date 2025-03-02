/*
 * https://dmoj.ca/problem/year2016p7
 * Precomputation trick with no updates
 * - Compute the maximum possible `r` for each index `l`
 *   - This can be done with a sliding window + multiset
 * - For each query, use a sparse table to find the maximum length interval
 *
 * TC: O(nlogn + qlogn)
 */

#include <bits/stdc++.h>

using namespace std;

const int LOG = 18;
const int MN = 100001;
array<int, 3> st[LOG][MN];

void build_st(const vector<array<int, 3>> &arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++)  // base layer
        st[0][i] = arr[i];
    for (int h = 1; h < LOG; h++)
        for (int i = 0; i < n - (1 << h) + 1; i++)
            st[h][i] = min(st[h - 1][i], st[h - 1][i + (1 << (h - 1))]);  // combine function goes here
}

array<int, 3> query(int l, int r) {
    int h = __lg(r - l + 1);
    return min(st[h][l], st[h][r - (1 << h) + 1]);  // combine function goes here
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<int> arr(N);
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    // right[i] will be the maximum possible r starting at i
    vector<int> right(N);
    multiset<int> window;
    int j = -1; // rightmost so far

    for (int i = 0; i < N; i++) {  // sliding window
        while (j + 1 < N) {
            j++;
            window.insert(arr[j]);

            if (*--window.end() - *window.begin() > K) {  // revert
                window.erase(window.find(arr[j]));
                j--;
                break;
            }
        }
        right[i] = j;

        // move i forwards, remove old value
        window.erase(window.find(arr[i]));
    }

    // (-length, left, right), negative length to get max
    vector<array<int, 3>> ranges;
    for (int i = 0; i < N; i++)
        ranges.push_back({-(right[i] - i + 1), i, right[i]});
    build_st(ranges);

    int Q;
    cin >> Q;
    while (Q--) {
        int l, r;
        cin >> l >> r;
        l--;
        r--;

        // find first index where ranges[i].right > r
        int rightmost = r + 1;
        int low = l;
        int high = r;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (ranges[mid][2] > r) {
                rightmost = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        if (ranges[l][2] >= r) {  // entire range works
            cout << l + 1 << " " << r + 1 << "\n";
            continue;
        }

        auto [le, ans_l, ans_r] = query(l, rightmost - 1);
        le *= -1;  // revert to positive

        if (le >= r - rightmost + 1)
            cout << ans_l + 1 << " " << ans_r + 1 << "\n";
        else  // a suffix interval (bounded by r) is more optimal
            cout << rightmost + 1 << " " << r + 1 << "\n";
    }

    return 0;
}
