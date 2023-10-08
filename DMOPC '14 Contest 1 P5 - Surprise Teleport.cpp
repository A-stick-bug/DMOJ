// https://dmoj.ca/problem/dmopc14c1p5
// 2 BFS, one considering teleporters and one without considering teleporters

#include <bits/stdc++.h>

using namespace std;

const int MM = 1000;
char graph[MM][MM];
bool tp[MM][MM], vis[MM][MM], vis2[MM][MM];

int dir[4][2] = {{0,  1},
                 {1,  0},
                 {-1, 0},
                 {0,  -1}};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    // create graph
    int R, C, sr, sc, er, ec;
    cin >> R >> C >> sr >> sc >> er >> ec;
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            cin >> graph[i][j];
    vis[sr][sc] = true;
    vis2[sr][sc] = true;

    // place teleporters
    int TPS, r, c;
    cin >> TPS;
    for (int i = 0; i < TPS; i++) {
        cin >> r >> c;
        tp[r][c] = true;
    }

    // find distance without using teleport
    int new_r, new_c, no_tp;
    queue<tuple<int, int, int>> q;
    q.push({sr, sc, 0});
    while (!q.empty()) {
        auto [row, col, dist] = q.front();
        q.pop();
        if (row == er && col == ec) {  // reached end without teleport
            no_tp = dist;
            break;
        }
        for (auto [dr, dc]: dir) {
            new_r = row + dr;
            new_c = col + dc;
            if (0 <= new_r && new_r < R && 0 <= new_c && new_c < C && !vis[new_r][new_c] && graph[new_r][new_c] != 'X'){
                vis[new_r][new_c] = true;
                q.push({new_r, new_c, dist + 1});
            }
        }
    }

    // find distance using teleport
    queue<tuple<int, int, int>> q2;
    q2.push({sr, sc, 0});
    while (!q2.empty()) {
        auto [row, col, dist] = q2.front();
        q2.pop();
        if ((row == er && col == ec) || tp[row][col]) {  // reached end or a teleport point
            cout << no_tp - dist << "\n";
            break;
        }
        for (auto [dr, dc]: dir) {
            new_r = row + dr;
            new_c = col + dc;
            if (0 <= new_r && new_r < R && 0 <= new_c && new_c < C && !vis2[new_r][new_c] && graph[new_r][new_c] != 'X'){
                vis2[new_r][new_c] = true;
                q2.push({new_r, new_c, dist + 1});
            }
        }
    }

    return 0;
}