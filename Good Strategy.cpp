/*
 * https://dmoj.ca/problem/goodc
 * My first time using the c++ set (it's actually really useful)
 * NOTE: the set has questions in DECREASING order by difficulty
 *
 * Not too familiar with custom comparators, so to prioritize the number of people that solved the question over
 * the question's number, we just add a large number for each person that solved it (this is also makes sure all
 * values are unique)
 */

#include <bits/stdc++.h>

#define ll long long
using namespace std;

const ll SOLVED = 10000000;
int N, M;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;  // N problems, M minutes (number of queries)

    ll difficulty[N + 1];  // store the difficulty of problems (bigger is EASIER)
    set<pair<ll, int>> ordered;

    for (int i = 1; i <= N; i++) {  // create default state
        difficulty[i] = N - i;  // N-1 because the easier questions come first and the set is harder to easier
        ordered.emplace(N - i, i);  // also store the question number for when we query the easiest and hardest
    }

    int operation, problem, small, big;
    ll diff;
    while (M--) {
        cin >> operation >> problem;

        if (operation == 1) {  // team 1 solved the problem, ignore this problem from now on
            diff = difficulty[problem];
            ordered.erase({diff, problem});
        } else {  // problem difficulty decreased
            diff = difficulty[problem];
            if (ordered.find({diff, problem}) != ordered.end()) {  // check if we haven't solved this yet
                ordered.erase({diff, problem});  // update difficulty
                difficulty[problem] += SOLVED;
                ordered.insert({diff + SOLVED, problem});
            }
        }

        if (ordered.empty()) {  // already solved everything
            cout << "Make noise" << "\n";
            continue;
        }

        // find min and max
        small = ordered.begin()->second;
        big = ordered.rbegin()->second;
        cout << big << ' ' << small << "\n";
    }
    return 0;
}
