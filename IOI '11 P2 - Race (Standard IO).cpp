// check Python code for explanations

#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 5;
const int inf = 1 << 30;
vector<pair<int, int>> graph[N];
int best = inf;
int _size[N], K;
bool cut[N];

void get_sizes(int cur, int prev) {
    _size[cur] = 1;
    for(auto &it : graph[cur]) {
        int adj = it.first;
        if(adj == prev || cut[adj]) continue;
        get_sizes(adj, cur);
        _size[cur] += _size[adj];
    }
}

int get_centroid(int cur, int prev, int comp_size) {
    for(auto &it : graph[cur]) {
        int adj = it.first;
        if(!cut[adj] && adj != prev && _size[adj] > comp_size / 2)
            return get_centroid(adj, cur, comp_size);
    }
    return cur;
}

vector<pair<int, int>> get_paths(int start, int prev) {
    vector<pair<int, int>> paths;
    stack<tuple<int, int, int, int>> stk;
    stk.push({start, prev, 0, 0});
    while(!stk.empty()) {
        auto [cur, prev, tot, le] = stk.top(); stk.pop();
        paths.push_back({tot, le});
        for(auto &it : graph[cur]) {
            int adj = it.first, val = it.second;
            if(adj == prev || cut[adj]) continue;
            stk.push({adj, cur, tot + val, le + 1});
        }
    }
    return paths;
}

void solve(int node) {
    get_sizes(node, -1);
    int centroid = get_centroid(node, -1, _size[node]);
    unordered_map<int, int> match = {{0, 0}};
    for(auto &it : graph[centroid]) {
        int adj = it.first, val = it.second;
        if(cut[adj]) continue;
        vector<pair<int, int>> adj_paths;
        for(auto &path : get_paths(adj, centroid))
            adj_paths.push_back({path.first + val, path.second + 1});
        for(auto &path : adj_paths) {
            int tot = path.first, le = path.second;
            if(match.count(K - tot)) best = min(best, match[K - tot] + le);
        }
        for(auto &path : adj_paths) {
            int tot = path.first, le = path.second;
            if(match.count(tot)) match[tot] = min(match[tot], le);
            else match[tot] = le;
        }
    }
    cut[centroid] = true;
    for(auto &it : graph[centroid])
        if(!cut[it.first]) solve(it.first);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N >> K;
    for(int i = 1; i < N; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }
    solve(0);
    cout << (best == inf ? -1 : best) << "\n";
    return 0;
}