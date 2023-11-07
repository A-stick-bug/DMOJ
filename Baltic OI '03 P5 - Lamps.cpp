/*
https://dmoj.ca/problem/btoi03p5
cellular automaton rule 102
use binary lifting to jump by powers of 2
O(N*log(M))
*/

#include <bits/stdc++.h>

using namespace std;

const int MN = 10e6;
bitset<MN> state, temp;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, iterations;
    cin >> N >> iterations;

    for (int i = 0, val; i < N; i++) {  // create starting state
        cin >> val;
        if (val == 1)
            state.set(i);
    }

    int p2;
    while (iterations > 0) {
        p2 = pow(2, floor(log2(iterations)));  // largest power of 2 less than iterations
        for (int i = 0; i < N; i++) {
            temp[i] = state[i] ^ state[(i + p2) % N];  // do the binary lifting trick
        }
        swap(temp, state);
        iterations -= p2;
    }

    for (int i = 0; i < N; i++) {
        if (state.test(i))
            cout << "1" << "\n";
        else
            cout << "0" << "\n";
    }
    return 0;
}
