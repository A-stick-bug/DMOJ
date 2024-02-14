// binary search

#include <bits/stdc++.h>
using namespace std;

bool works(int x, vector<int>& arr1, vector<int>& arr2, int N, int M) {
    int i = 0, j = 0, cnt = 0;
    while (i < N && j < M) {
        if (abs(arr1[i] - arr2[j]) > x) {
            if (arr1[i] > arr2[j]) {
                j += 1;
            } else {
                i += 1;
            }
        } else {
            i += 1;
            j += 1;
            cnt += 1;
        }
    }
    return cnt == min(N, M);
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> arr1(N), arr2(M);
    for (int i = 0; i < N; i++) cin >> arr1[i];
    for (int i = 0; i < M; i++) cin >> arr2[i];
    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());

    int low = 0, high = 1000000000;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (works(mid, arr1, arr2, N, M)) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << low << endl;
    return 0;
}