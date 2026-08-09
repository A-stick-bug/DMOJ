#include <bits/stdc++.h>

using namespace std;

// O(n * log^2(n))
vector<int> suffix_array(const string& s) {
    int n = s.length();

    vector<int> perm(n);
    iota(perm.begin(), perm.end(), 0);
    sort(perm.begin(), perm.end(), [&](int a, int b) {
        return s[a] < s[b];
    });

    vector<int> rank(n, 0);
    for (int i = 1; i < n; ++i) {
        rank[perm[i]] = rank[perm[i - 1]] + (s[perm[i]] != s[perm[i - 1]] ? 1 : 0);
    }

    for (int p2 = 1; p2 < n; p2 *= 2) {
        auto get_pair = [&](int i) -> pair<int, int> {
            return {rank[i], i + p2 < n ? rank[i + p2] : -1};
        };

        sort(perm.begin(), perm.end(), [&](int a, int b) {
            return get_pair(a) < get_pair(b);
        });

        vector<int> new_rank(n, 0);
        for (int i = 1; i < n; ++i) {
            int prev = perm[i - 1];
            int cur = perm[i];
            new_rank[cur] = new_rank[prev] + (get_pair(cur) != get_pair(prev) ? 1 : 0);
        }

        rank = move(new_rank);
        if (rank[perm.back()] == n - 1) {
            break;
        }
    }

    return perm;
}

int main() {
    string s;
    cin >> s;
    int n = s.size();
    int k;
    cin >> k;

    vector<int> sa = suffix_array(s);
    for (int i = 0; i < n; i++) {
        if (n - sa[i] >= k) {
            cout << s.substr(sa[i], k) << "\n";
            break;
        }
    }

    return 0;
}
