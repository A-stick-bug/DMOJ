/*
 https://dmoj.ca/problem/2dperm
 typical annoying ad hoc question

 Using offline queries (definitely not intended solution)
 Note: the intended solution uses a difference array (and doesn't have that extra log factor from sorting)

 TC: O(MN*log(MN) + Qlog(Q))
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N, M, Q;
    cin >> N >> M >> Q;
    int area = N * M;
    vector<int> table;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            table.push_back(i * j);
        }
    }
    sort(table.begin(), table.end());

    vector<pair<int, int>> queries(Q);
    for (int i = 0; i < Q; i++) {
        cin >> queries[i].first;
        queries[i].second = i;
    }
    sort(queries.rbegin(), queries.rend());

    vector<int> ans(Q);
    int i = 0, j = area - 1;
    for (auto [num, idx] : queries) {
        while (i + 1 < area && table[i + 1] + num - 1 <= area) {
            i++;
        }
        while (j - 1 >= 0 && table[j - 1] > num) {
            j--;
        }

        ans[idx] = i - (area - j) + 1;
        if (num == area) {
            ans[idx] = 1;
        }
    }

    for (int i = 0; i < Q; i++) {
        cout << ans[i] << "\n";
    }

    return 0;
}
