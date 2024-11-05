// https://dmoj.ca/problem/dmpg19s3
// stack to keep track of element count multipliers

#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int _;
    cin >> _;

    vector<string> arr;
    string token;
    while (cin >> token) {
        arr.push_back(token);
    }

    int n = arr.size();
    map<string, long long> cnt;
    vector<long long> multiplier = {1};

    for (int i = n - 1; i >= 0; --i) {
        if (isdigit(arr[i][0])) {
            if (i > 0 && arr[i - 1] == ")") {  // start of new multiplier
                multiplier.push_back(multiplier.back() * stoll(arr[i]) % MOD);
            } else {  // single element
                cnt[arr[i - 1]] = (cnt[arr[i - 1]] + stoll(arr[i]) * multiplier.back() % MOD) % MOD;
            }
        } else if (arr[i] == "(") {  // end of multiplier
            multiplier.pop_back();
        }
    }

    for (auto [key, value]: cnt) {
        cout << key << " " << value % MOD << "\n";
    }
    return 0;
}