/*
 https://dmoj.ca/problem/gfssoc2s5

 Using tarjan's algorithm for SCC, compress SCC into a single node

 Observations:
 - provinces are just strongly connected components (SCCs), once you get there, you might as well
   borrow everything in this province
 - we can just turn each SCC into a single node with the sum of money you can borrow
 - now we get a DAG, and we can use graph DP

 Note that we use 1-indexing for everything
*/

#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int N, M;
vector<int> scc, scc_money, low_link, node_id, money;
vector<bool> in_path;
vector<vector<int>> graph, graph2;
vector<pair<int, int>> cache[2];
int t = 0, comp = 1;
stack<int> path;

void dfs(int cur) {
    node_id[cur] = low_link[cur] = t++;
    path.push(cur);
    in_path[cur] = true;

    for (int adj : graph[cur]) {
        if (node_id[adj] == -1) {
            dfs(adj);
            low_link[cur] = min(low_link[cur], low_link[adj]);
        } else if (in_path[adj]) {
            low_link[cur] = min(low_link[cur], node_id[adj]);
        }
    }

    if (node_id[cur] == low_link[cur]) {
        while (path.top() != cur) {
            in_path[path.top()] = false;
            scc_money[comp] += money[path.top()];
            scc[path.top()] = comp;
            path.pop();
        }
        in_path[cur] = false;
        scc_money[comp] += money[cur];
        scc[path.top()] = comp;
        path.pop();
        comp++;
    }
}

pair<int, int> solve(int cur, bool take) {
    if (cur == scc[N]) {
        return {take * scc_money[cur], 1};
    }
    if (cache[take][cur] != make_pair(-1, -1)) {
        return cache[take][cur];
    }

    int best = 0, ways = 1;
    for (int adj : graph2[cur]) {
        if (take) {
            pair<int, int> res = solve(adj, false);
            res.first += scc_money[cur];
            if (res.first == best) {
                ways = (ways + res.second) % MOD;
            } else if (res.first > best) {
                best = res.first;
                ways = res.second % MOD;
            }
        }
        pair<int, int> res = solve(adj, true);
        if (res.first == best) {
            ways = (ways + res.second) % MOD;
        } else if (res.first > best) {
            best = res.first;
            ways = res.second % MOD;
        }
    }

    cache[take][cur] = {best, ways};
    return cache[take][cur];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    scc = money = low_link = node_id = vector<int>(N + 1, -1);
    scc_money = vector<int>(N + 1, 0);
    in_path = vector<bool>(N + 1, false);
    graph = graph2 = vector<vector<int>>(N + 1);
    cache[0] = cache[1] = vector<pair<int, int>>(N + 1, {-1, -1});

    for (int i = 1; i <= N; i++) {
        cin >> money[i];
    }

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
    }

    for (int i = 1; i <= N; i++) {
        if (node_id[i] == -1) {
            dfs(i);
        }
    }

    graph2 = vector<vector<int>>(comp);
    for (int i = 1; i <= N; i++) {
        for (int adj : graph[i]) {
            if (scc[i] != scc[adj]) {
                graph2[scc[i]].push_back(scc[adj]);
            }
        }
    }

    for (auto &adj : graph2) {
        sort(adj.begin(), adj.end());
        adj.erase(unique(adj.begin(), adj.end()), adj.end());
    }

    pair<int, int> res = solve(scc[1], true);
    cout << res.first << " " << res.second << "\n";

    return 0;
}
