// https://dmoj.ca/problem/subway
// Q: count the number of longest paths in a tree
// A: all paths tree DP
//
// TC: O(nlogn), extra logn from sorting paths

#include<bits/stdc++.h>
using namespace std;

vector<int> graph[50005];
int path_cnt[50005];  // number of paths with length i (only accurate for longest)


int match_longest(vector<pair<int, int>> paths, int longest) {
    // count of number of ways of joining 2 paths to form the longest possible
    int total = 0;
    map<int, int> match;
    for(auto p : paths) {
        int length = p.first, cnt = p.second;
        if(match.count(longest - length))
            total += cnt * match[longest - length];
        match[length] += cnt;
    }
    return total;
}

pair<int, int> solve(int cur, int prev) {
    if(graph[cur].size() == 1 && cur != 1)  // leaf node: path of length 0 occurs once
        return make_pair(0, 1);

    // paths starting at the current node and ending below
    // (path length, number of ways of creating this path)
    vector<pair<int, int>> paths;
    for(auto adj : graph[cur]) {
        if(adj == prev)
            continue;
        pair<int, int> p = solve(adj, cur);
        paths.push_back(make_pair(p.first + 1, p.second));
    }

    sort(paths.begin(), paths.end());  // sort by length
    int longest = 0, cnt = 0;
    if(paths.size() >= 2) {
        longest = paths.back().first + (paths.end() - 2)->first;  // join 2 longest paths
        cnt = match_longest(paths, longest);
        path_cnt[longest] += cnt;
    }

    // longest path starting at cur and ending below
    cnt = 0;
    longest = paths.back().first;
    for(auto p : paths)
        if(p.first == longest)
            cnt += p.second;
    path_cnt[longest] += cnt;  // it is possible that the longest path isn't formed by joining 2 nodes
    return make_pair(longest, cnt);
}

int main() {
    int n;
    cin >> n;
    for(int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    solve(1, -1);
    for(int i = n - 1; i >= 0; i--) {
        if(path_cnt[i] != 0) {
            cout << path_cnt[i] << endl;
            break;
        }
    }

    return 0;
}
