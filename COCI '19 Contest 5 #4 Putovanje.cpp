/*
 https://dmoj.ca/problem/coci19c5p4
 Tree LCA + difference array on tree
 from A -> B, split it into A -> LCA -> B, we add 1 to every edge on this path
 We can efficiently add 1 to the edges using a difference array on nodes and do a prefix sum
 on the tree starting from the bottom
*/

#include<bits/stdc++.h>
#define int long long
using namespace std;

const int MAXN = 2e5+5;
vector<tuple<int, int, int>> graph[MAXN];
int depth[MAXN], first[MAXN], diff[MAXN];
vector<int> euler;
pair<int, int> st[2*MAXN][18];
int total = 0;
int N;

void dfs(int u, int prev) {
    first[u] = euler.size();
    euler.push_back(u);
    for(auto [v, c1, c2] : graph[u]) {
        if(v != prev) {
            depth[v] = depth[u] + 1;
            dfs(v, u);
            euler.push_back(u);
        }
    }
}

int lca(int u, int v) {
    int left = min(first[u], first[v]);
    int right = max(first[u], first[v]);
    int k = log2(right - left + 1);
    return min(st[left][k], st[right - (1 << k) + 1][k]).second;
}

int solve(int cur, int prev) {
    int c_sum = 0;
    for(auto [adj, c1, c2] : graph[cur]) {
        if(adj == prev) continue;
        int sub = solve(adj, cur);
        c_sum += sub;
        total += min(c2, c1 * sub);
    }
    return c_sum + diff[cur];
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for(int i = 0; i < N - 1; i++) {
        int a, b, c1, c2;
        cin >> a >> b >> c1 >> c2;
        graph[a].push_back({b, c1, c2});
        graph[b].push_back({a, c1, c2});
    }

    dfs(1, -1);
    int M = euler.size();
    int layers = log2(M) + 1;
    for(int i = 1; i <= M; i++) {
        st[i][0] = {depth[euler[i]], euler[i]};
    }
    for(int k = 1; k < layers; k++) {
        for(int i = 1; i <= M - (1 << k) + 1; i++) {
            st[i][k] = min(st[i][k - 1], st[i + (1 << (k - 1))][k - 1]);
        }
    }

    for(int i = 1; i < N; i++) {
        int ancestor = lca(i, i + 1);
        diff[ancestor] -= 2;
        diff[i] += 1;
        diff[i + 1] += 1;
    }

    solve(1, -1);
    cout << total << "\n";
    return 0;
}
