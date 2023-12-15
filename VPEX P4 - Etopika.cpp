#include<bits/stdc++.h>
using namespace std;

const int MAXN = 1e5 + 5;
const int LOG = 20;
int depth[MAXN], first[MAXN], dist[MAXN];
pair<int, int> st[2*MAXN][LOG];
vector<pair<int, int>> graph[MAXN];
vector<int> euler;

void dfs(int u, int prev) {
    first[u] = euler.size();
    euler.push_back(u);
    for(auto &it : graph[u]) {
        if(it.first != prev) {
            depth[it.first] = depth[u] + 1;
            dist[it.first] = dist[u] + it.second;
            dfs(it.first, u);
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

int distance(int u, int v) {
    return dist[u] + dist[v] - 2 * dist[lca(u, v)];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, D;
    cin >> N >> D;

    for(int i = 0; i < N - 1; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        a--; b--;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    dfs(0, -1);
    int M = euler.size();
    for(int i = 0; i < M; i++)
        st[i][0] = {depth[euler[i]], euler[i]};
    for(int k = 1; k <= LOG; k++)
        for(int i = 0; i + (1 << k) <= M; i++)
            st[i][k] = min(st[i][k - 1], st[i + (1 << (k - 1))][k - 1]);

    long long prev1 = 0, prev2 = 0, total1 = 0, total2 = 0;
    for(int i = 0; i < D; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        int mid = distance(a, b);

        // use temporary variable and swap
        long long t1 = min(total1 + distance(prev1, b), total2 + distance(prev2, b)) + mid;
        total2 = min(total1 + distance(prev1, a), total2 + distance(prev2, a)) + mid;
        total1 = t1;

        prev1 = a;
        prev2 = b;
    }
    cout << min(total1, total2) << "\n";
    return 0;
}
