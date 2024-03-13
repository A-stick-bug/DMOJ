// https://dmoj.ca/problem/gooda
// python code has explanation and stuff
// note that case 6 is massive and overflows int (but we can't use long long for everything or else MLE)

#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<int> scc, low_link, node_id, fun;
vector<ll> cache, scc_fun;
vector<vector<int>> graph, compressed;
vector<bool> in_path;
stack<int> path;
int t = 0, comp = 1, N, M, start, _end;

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
            scc_fun[comp] += fun[path.top()];
            scc[path.top()] = comp;
            path.pop();
        }
        in_path[cur] = false;
        scc_fun[comp] += fun[cur];
        scc[path.top()] = comp;
        path.pop();
        comp++;
    }
}

pair<vector<int>, vector<ll>> get_scc() {
    for (int i = 1; i <= N; i++) {
        if (node_id[i] == -1) {
            dfs(i);
        }
    }
    return make_pair(scc, scc_fun);
}

ll solve(ll cur) {
    if (cache[cur] != -1) {
        return cache[cur];
    }
    if (cur == scc[_end]) {
        return scc_fun[scc[_end]];
    }
    ll best = 0;
    for (int adj : compressed[cur]) {
        best = max(best, solve(adj) + (ll)scc_fun[cur]);
    }
    cache[cur] = best;
    return cache[cur];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> start >> _end;
    fun.resize(N + 1, -1);
    for (int i = 1; i <= N; i++) {
        cin >> fun[i];
    }

    graph.resize(N + 1);
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
    }

    scc.resize(N + 1, -1);
    scc_fun.resize(N + 1, 0);
    low_link.resize(N + 1, -1);
    node_id.resize(N + 1, -1);
    in_path.resize(N + 1, false);
    tie(scc, scc_fun) = get_scc();

    compressed.resize(comp);
    for (int i = 1; i <= N; i++) {
        for (int adj : graph[i]) {
            if (scc[i] != scc[adj]) {
                compressed[scc[i]].push_back(scc[adj]);
            }
        }
    }

    for (auto &adj : compressed) {
        unordered_set<int> s(adj.begin(), adj.end());
        adj.assign(s.begin(), s.end());
    }

    cache.resize(N + 1, -1);
    cout << solve(scc[start]) << "\n";

    return 0;
}
