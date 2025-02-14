#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, X;
    cin >> N >> X;

    long long mx = (N - 1) * (N - 2) / 2;

    if (mx < X) {
        cout << -1 << "\n";
        return 0;
    }

    vector<long long> excluded, included;
    long long to_remove = mx - X;
    for (long long i = 1; i < N - 1; i++) {
        long long stored_water = (N - 1) - i;
        if (to_remove >= stored_water) {
            excluded.push_back(i);
            to_remove -= stored_water;
        } else {
            included.push_back(i);
        }
    }

    // output
    vector<long long> res;
    for (auto x: excluded)
        res.push_back(x);
    res.push_back(N);
    for (auto x: included)
        res.push_back(x);
    res.push_back(N - 1);
    for (size_t i = 0; i < res.size(); i++) {
        cout << res[i] << (i + 1 == res.size() ? "\n" : " ");
    }
    return 0;
}
