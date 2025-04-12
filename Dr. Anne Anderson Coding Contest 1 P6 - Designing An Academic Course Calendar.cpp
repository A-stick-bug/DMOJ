// https://dmoj.ca/problem/daacc1p6
// graph DP + topo sort
// note: the graph DP part was probably unnecessary and can be simplified...
// first check which course are needed, then topo sort to order them

#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> rev_graph;
vector<int> dp;

void solve(int cur) {
    if (dp[cur] != -1) return;
    if (rev_graph[cur].empty()) dp[cur] = 0;
    for (int adj: rev_graph[cur]) {
        solve(adj);
        dp[cur] = max(dp[cur], dp[adj] + 1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;

    vector<int> must_list;
    vector<bool> must(N + 1, 0);
    for (int i = 0; i < K; i++) {
        int a;
        cin >> a;
        must_list.push_back(a);
        must[a] = true;
    }

    vector<int> indeg(N + 1, 0);
    vector<vector<int>> graph(N + 1, vector<int>());
    rev_graph.resize(N + 1, vector<int>());

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        rev_graph[b].push_back(a);
        indeg[b]++;
    }
    // END INPUT

    dp.resize(N + 1, -1);
    for (int need: must_list)
        solve(need);

    queue<pair<int, int>> q;
    for (int i = 1; i <= N; i++)
        if (dp[i] == 0)
            q.push({0, i});

    vector<vector<int>> depth(N + 1, vector<int>());

    while (!q.empty()) {
        auto [d, cur] = q.front();
        q.pop();

        if (dp[cur] != -1)
            depth[d].push_back(cur);
        for (int adj: graph[cur]) {
            indeg[adj]--;
            if (indeg[adj] == 0)
                q.push({d + 1, adj});
        }

    }

    int days = *max_element(dp.begin(), dp.end()) + 1;

    cout << days << "\n";
    for (int d = 0; d < days; d++) {
        sort(depth[d].begin(), depth[d].end());
        for (int i = 0; i < depth[d].size(); i++)
            cout << depth[d][i] << " \n"[i == depth[d].size() - 1];
    }

    return 0;
}