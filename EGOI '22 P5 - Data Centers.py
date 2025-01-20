# TLE IN PYTHON, CHECK C++ CODE BELOW
# https://dmoj.ca/problem/egoi22p5
# - Given Q operations of removing x from the k biggest numbers, what is the resulting
#   array after these operations
#
# TC: O(NS)
# note that a log factor will TLE so we use a linear merge instead of sort

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

for _ in range(Q):
    x, k = map(int, input().split())  # remove x from top k

    for i in range(k):
        arr[i] -= x

    # now we have 2 descending runs, we cna merge them in O(n)
    # instead of sorting in O(nlogn)
    a1 = arr[:k]
    a2 = arr[k:]

    arr = []
    while a1 and a2:
        if a1[-1] < a2[-1]:
            arr.append(a1.pop())
        else:
            arr.append(a2.pop())
    while a1:
        arr.append(a1.pop())
    while a2:
        arr.append(a2.pop())
    arr.reverse()

print(" ".join(map(str, arr)))

"""
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr.rbegin(), arr.rend());

    while (Q--) {
        int x, k;
        cin >> x >> k;

        for (int i = 0; i < k; i++) {
            arr[i] -= x;
        }

        vector<int> a1(arr.begin(), arr.begin() + k);
        vector<int> a2(arr.begin() + k, arr.end());
        vector<int> merged;

        int i = 0, j = 0;
        while (i < a1.size() && j < a2.size()) {
            if (a1[i] > a2[j]) {
                merged.push_back(a1[i++]);
            } else {
                merged.push_back(a2[j++]);
            }
        }
        while (i < a1.size()) {
            merged.push_back(a1[i++]);
        }
        while (j < a2.size()) {
            merged.push_back(a2[j++]);
        }

        arr = move(merged);
    }

    for (int i = 0; i < N; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";

    return 0;
}
"""
