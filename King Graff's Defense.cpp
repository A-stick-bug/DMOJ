/*
 MLE, 15/28, whoever set the memory limit this low is actually trolling

 https://dmoj.ca/problem/graffdefense

 Note: this is just bi-connected components, but I didn't know that when I did this problem

 - let a component be a part of the graph with no bridges inside
 - first find all bridges and remove them from the graph
 - now, any connected nodes in the graph will be part of the same component

 - there are NC2 ways to put the 2 soldiers
 - for each component, add XC2 to the valid positions, where X is the # of nodes in that component
 - answer will be (# of valid positions)/(numbers of ways to put 2 soldiers)
*/

#include<bits/stdc++.h>
using namespace std;

vector<int> adj[1000005];
int low[1000005], disc[1000005], tim;
set<pair<int, int>> bridge;

void dfs(int u, int par) {
    disc[u] = low[u] = ++tim;
    for(int v : adj[u]) {
        if(v == par) continue;
        if(!disc[v]) {
            dfs(v, u);
            low[u] = min(low[u], low[v]);
            if(low[v] > disc[u]) {
                bridge.insert({min(u, v), max(u, v)});
            }
        } else {
            low[u] = min(low[u], disc[v]);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;
    vector<pair<int, int>> edges;
    for(int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        if(u == v) continue;
        edges.push_back({min(u, v), max(u, v)});
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    dfs(1, -1);

    for(auto e : edges) {
        if(bridge.count(e)) {
            adj[e.first].erase(find(adj[e.first].begin(), adj[e.first].end(), e.second));
            adj[e.second].erase(find(adj[e.second].begin(), adj[e.second].end(), e.first));
        }
    }

    vector<int> comp;
    bool vis[1000005] = {0};
    for(int i = 1; i <= n; i++) {
        if(vis[i]) continue;
        int cnt = 0;
        queue<int> q;
        q.push(i);
        vis[i] = true;
        while(!q.empty()) {
            int u = q.front();
            q.pop();
            cnt++;
            for(int v : adj[u]) {
                if(vis[v]) continue;
                vis[v] = true;
                q.push(v);
            }
        }
        comp.push_back(cnt);
    }

    long long valid = 0;
    for(int c : comp) {
        valid += 1LL * c * (c - 1) / 2;
    }
    long long total = 1LL * n * (n - 1) / 2;
    cout << fixed << setprecision(5) << 1 - (double)valid / total << "\n";

    return 0;
}
