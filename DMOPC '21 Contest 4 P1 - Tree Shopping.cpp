// the point splits the triangle into 3 pieces
// the sum of those pieces will equal the area of the triangle only if the point is inside the triangle

#include <bits/stdc++.h>
#define int long long

using namespace std;

int area(int x1, int y1, int x2, int y2, int x3, int y3) {
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)));
}

bool isInside(int x1, int y1, int x2, int y2, int x3, int y3, int x, int y) {
    int A = area(x1, y1, x2, y2, x3, y3);
    int A1 = area(x, y, x2, y2, x3, y3);
    int A2 = area(x1, y1, x, y, x3, y3);
    int A3 = area(x1, y1, x2, y2, x, y);
    return A == A1 + A2 + A3;
}

signed main() {
    int N, P;
    cin >> N >> P;
    vector<vector<int>> tri(N, vector<int>(6));
    for(int i = 0; i < N; i++)
        for(int j = 0; j < 6; j++)
            cin >> tri[i][j];
    for(int i = 0; i < P; i++) {
        int x, y;
        cin >> x >> y;
        int sum = 0;
        for(int j = 0; j < N; j++)
            sum += isInside(tri[j][0], tri[j][1], tri[j][2], tri[j][3], tri[j][4], tri[j][5], x, y);
        cout << sum << endl;
    }
    return 0;
}
