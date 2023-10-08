// https://dmoj.ca/problem/tsoc16c1p4
// find number of islands with monkeys using dfs:
//   - check every cell: if there is a monkey in that cell, mark every cell in that island as visited
//   - use walls to mark visited cells

#include <bits/stdc++.h>

using namespace std;

const int ROWS = 35, COLS = 50;
char graph[ROWS][COLS];
int N, M;
int dir[4][2] = {{0,  1},
                 {1,  0},
                 {-1, 0},
                 {0,  -1}};

// flood fill
void fill(int r, int c) {
    int new_r, new_c;
    graph[r][c] = '#';  // mark as visited
    stack<pair<int, int>> st;
    st.emplace(r, c);

    while (!st.empty()) {
        auto [row, col] = st.top();
        st.pop();
        for (auto [dr, dc]: dir) {
            new_r = row + dr;
            new_c = col + dc;
            if (graph[new_r][new_c] != '#') {
                graph[new_r][new_c] = '#';
                st.emplace(new_r, new_c);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> graph[i][j];

    int total = 0;
    for (int i = 1; i < N - 1; i++) {  // all cells on an edge are walls
        for (int j = 1; j < M - 1; j++) {
            if (graph[i][j] == 'M') {
                total += 1;
                fill(i, j);
            }
        }
    }
    cout << total << "\n";
    return 0;
}
