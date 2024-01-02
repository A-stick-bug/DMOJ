// C++ translation that passes

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<vector<int>> grid(N, vector<int>(M));
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++)
            cin >> grid[i][j];

    int r, c;
    cin >> r >> c;

    vector<deque<int>> maxs(N);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < c; j++) {
            while(!maxs[i].empty() && grid[i][maxs[i].back()] <= grid[i][j])
                maxs[i].pop_back();
            maxs[i].push_back(j);
        }
    }

    vector<vector<int>> total_res;
    for(int j = c-1; j < M; j++) {
        if(j >= c) {
            for(int i = 0; i < N; i++) {
                if(maxs[i].front() == j - c)
                    maxs[i].pop_front();
                while(!maxs[i].empty() && grid[i][maxs[i].back()] <= grid[i][j])
                    maxs[i].pop_back();
                maxs[i].push_back(j);
            }
        }

        vector<int> max_vals(N);
        for(int i = 0; i < N; i++)
            max_vals[i] = grid[i][maxs[i].front()];

        deque<int> q;
        vector<int> res(N - r + 1);
        for(int i = 0; i < N; i++) {
            int left = i - r + 1;
            while(!q.empty() && max_vals[q.back()] <= max_vals[i])
                q.pop_back();
            q.push_back(i);

            if(left >= 0) {
                res[left] = max_vals[q.front()];
                if(q.front() == left)
                    q.pop_front();
            }
        }

        total_res.push_back(res);
    }

    for(int i = 0; i < total_res[0].size(); i++) {
        for(int j = 0; j < total_res.size(); j++)
            cout << total_res[j][i] << " ";
        cout << "\n";
    }

    return 0;
}
