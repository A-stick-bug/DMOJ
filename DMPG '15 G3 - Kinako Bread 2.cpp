// https://dmoj.ca/problem/dmpg15g3
// direct translation of Python code, check that one for explanation

#include <bits/stdc++.h>

using namespace std;

const int MAXN = 200005;

struct FenwickTree {
    vector<int> bit;
    int n;

    FenwickTree(int size) {
        n = size;
        bit.assign(n + 1, 0);
    }

    void update(int i, int diff) {
        while (i <= n) {
            bit[i] += diff;
            i += i & -i;
        }
    }

    int query(int i) {
        int total = 0;
        while (i > 0) {
            total += bit[i];
            i -= i & -i;
        }
        return total;
    }

    int query_range(int left, int right) {
        return query(right) - query(left - 1);
    }
};

int N, LX, RX, LY, RY;
vector<pair<int, int>> arr;
vector<vector<int>> graph;
vector<int> sz;
vector<bool> cut;
FenwickTree bit(MAXN);
long long total = 0;

void get_sizes(int cur, int prev) {
    sz[cur] = 1;
    for (int adj : graph[cur]) {
        if (adj == prev || cut[adj]) continue;
        get_sizes(adj, cur);
        sz[cur] += sz[adj];
    }
}

int get_centroid(int cur, int prev, int comp_size) {
    for (int adj : graph[cur]) {
        if (!cut[adj] && adj != prev && sz[adj] > comp_size / 2) {
            return get_centroid(adj, cur, comp_size);
        }
    }
    return cur;
}

vector<pair<int, int>> get_paths(int cur, int prev) {
    vector<pair<int, int>> paths;
    vector<tuple<int, int, int, int>> stack;
    stack.emplace_back(arr[cur].first, arr[cur].second, cur, prev);

    while (!stack.empty()) {
        auto [x, y, node, parent] = stack.back();
        stack.pop_back();
        paths.emplace_back(x, y);
        for (int adj : graph[node]) {
            if (!cut[adj] && adj != parent) {
                stack.emplace_back(x + arr[adj].first, y + arr[adj].second, adj, node);
            }
        }
    }

    return paths;
}

long long match_pairs(vector<pair<int, int>> &paths, int lx, int rx, int ly, int ry) {
    sort(paths.begin(), paths.end());

    auto helper = [&](int rx) {
        if (rx < 0) return 0LL;
        int l = -1;
        long long t = 0;
        for (int r = paths.size() - 1; r >= 0; --r) {
            while (l + 1 < r && paths[r].first + paths[l + 1].first <= rx) {
                ++l;
                bit.update(paths[l].second + 1, 1);
            }
            if (l >= r) {
                bit.update(paths[l].second + 1, -1);
                --l;
            }
            t += bit.query_range(ly - paths[r].second + 1, ry - paths[r].second + 1);
        }
        for (int i = 0; i <= l; ++i) {
            bit.update(paths[i].second + 1, -1);
        }
        return t;
    };

    return helper(rx) - helper(lx - 1);
}

void solve(int root) {
    get_sizes(root, -1);
    int centroid = get_centroid(root, -1, sz[root]);
    int cx = arr[centroid].first, cy = arr[centroid].second;

    vector<pair<int, int>> all_paths = {{0, 0}};
    for (int adj : graph[centroid]) {
        if (cut[adj]) continue;
        vector<pair<int, int>> paths = get_paths(adj, centroid);
        total -= match_pairs(paths, LX - cx, RX - cx, LY - cy, RY - cy);
        all_paths.insert(all_paths.end(), paths.begin(), paths.end());
    }

    total += match_pairs(all_paths, LX - cx, RX - cx, LY - cy, RY - cy);

    cut[centroid] = true;
    for (int adj : graph[centroid]) {
        if (!cut[adj]) solve(adj);
    }
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> LX >> RX >> LY >> RY;
    arr.resize(N + 1);
    graph.resize(N + 1);
    sz.resize(N + 1);
    cut.assign(N + 1, false);

    for (int i = 1; i <= N; ++i) {
        char c;
        cin >> c;
        arr[i] = (c == 'K') ? make_pair(1, 0) : make_pair(0, 1);
    }

    for (int i = 0; i < N - 1; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    solve(1);

    for (int i = 1; i <= N; ++i) {
        if (LX <= arr[i].first && arr[i].first <= RX && LY <= arr[i].second && arr[i].second <= RY) {
            ++total;
        }
    }

    cout << total << "\n";
    return 0;
}
