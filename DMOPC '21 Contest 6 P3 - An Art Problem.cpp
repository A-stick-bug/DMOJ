// https://dmoj.ca/problem/dmopc21c6p3
// BFS flood fill, multiple starting points
// sort to start by filling with the smaller numbers

#include <bits/stdc++.h>

using namespace std;

bool sort3rd(const tuple<int, int, int, int> &a,
              const tuple<int, int, int, int> &b) {
    return (get<2>(a) < get<2>(b));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int ROWS, COLS, K;
    cin >> ROWS >> COLS >> K;

    vector<vector<int>> graph(ROWS, vector<int>(COLS));
    for (int i = 0; i < ROWS; ++i)
        for (int j = 0; j < COLS; ++j)
            cin >> graph[i][j];

    array<pair<int, int>, 4> dir = {{{0, 1}, {1, 0}, {-1, 0}, {0, -1}}};

    vector<tuple<int, int, int, int>> q;
    for (int i = 0; i < ROWS; ++i)
        for (int j = 0; j < COLS; ++j)
            if (graph[i][j])
                q.emplace_back(i, j, graph[i][j], 1);

    sort(q.begin(), q.end(), sort3rd);  // sort by color, smaller colors have priority

    deque<tuple<int, int, int, int>> dq(q.begin(), q.end());
    while (!dq.empty()) {
        auto [row, col, color, time] = dq.front();
        dq.pop_front();
        if (time > K)
            break;
        for (auto [dr, dc]: dir) {
            int new_r = row + dr;
            int new_c = col + dc;
            if (0 <= new_r && new_r < ROWS && 0 <= new_c && new_c < COLS && !graph[new_r][new_c]) {
                graph[new_r][new_c] = color;
                dq.emplace_back(new_r, new_c, color, time + 1);
            }
        }
    }

    for (auto &row: graph) {
        for (auto &cell: row)
            cout << cell << ' ';
        cout << '\n';
    }

    return 0;
}
