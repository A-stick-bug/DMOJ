/*
 https://dmoj.ca/problem/cheerio1s3
 long double is needed because even double is not precise enough for this question (what a troll)

 Find number of trend lines by starting at each point and keeping track of the highest and lowest slope up to point j
 If the current slope is greater than highest or less than smallest,
 all points between i and j are either above or below the line (or on the line)
 O(n^2)
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }

    sort(points.begin(), points.end());

    int total = 0;
    for (int i = 0; i < n - 1; i++) {
        long double highest = numeric_limits<double>::lowest();
        long double lowest = numeric_limits<double>::max();

        for (int j = i + 1; j < n; j++) {
            long double slope = static_cast<long double>(points[j].second - points[i].second) / (points[j].first - points[i].first);
            if (slope >= highest || slope <= lowest) {
                total += 1;
            }
            highest = max(highest, slope);  // update highest and lowest slope
            lowest = min(lowest, slope);
        }
    }
    cout << total << endl;
    return 0;
}
