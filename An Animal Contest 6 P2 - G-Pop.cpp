// AI translation of python code since Python is too slow

#include <bits/stdc++.h>
using namespace std;

// Fenwick Tree (Binary Indexed Tree) with order statistics (select)
// This structure supports update(i, diff), prefix sum query and select(k)
// (i.e. find the smallest index with prefix sum >= k).
struct OrderStatisticsTree {
    int n;
    vector<int> tree;

    // Constructor: build from an initial array (0-indexed) of length n.
    OrderStatisticsTree(const vector<int>& arr) {
        n = arr.size();
        tree.assign(n + 1, 0);
        for (int i = 1; i <= n; i++){
            tree[i] = arr[i - 1];
        }
        // Build the tree in O(n)
        for (int i = 1; i <= n; i++){
            int j = i + (i & -i);
            if(j <= n)
                tree[j] += tree[i];
        }
    }

    // Point update: add diff to index i (1-indexed)
    void update(int i, int diff) {
        for (; i <= n; i += i & -i)
            tree[i] += diff;
    }

    // Prefix sum query: returns sum of indices [1, i]
    int p_query(int i) {
        int res = 0;
        for(; i; i -= i & -i)
            res += tree[i];
        return res;
    }

    // Range query: returns sum in [l, r]
    int query(int l, int r) {
        return p_query(r) - p_query(l - 1);
    }

    // select(k): returns the smallest index i (1-indexed) with prefix sum >= k.
    int select(int k) {
        int idx = 0;
        int bit = 1;
        while(bit <= n) bit <<= 1;
        bit >>= 1;
        for(; bit; bit >>= 1){
            if(idx + bit <= n && tree[idx + bit] < k) {
                k -= tree[idx + bit];
                idx += bit;
            }
        }
        return idx + 1;
    }
};

// Structure for events.
struct Event {
    int time;
    int prev;
    int t; // 1 means start event, -1 means end event.
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector<pair<int,int>> queries(Q);
    for (int i = 0; i < Q; i++){
        int l, r;
        cin >> l >> r;
        queries[i] = {l, r};
    }

    // Build events: for each query (l, r) add a start event at time l and an end event at time r+1.
    vector<Event> events;
    events.reserve(2 * Q);
    for(auto &pr : queries){
        int l = pr.first, r = pr.second;
        events.push_back({l, l, 1});
        events.push_back({r + 1, l, -1});
    }
    // Sort events lexicographically by (time, prev, t)
    sort(events.begin(), events.end(), [](const Event &a, const Event &b){
        if(a.time != b.time) return a.time < b.time;
        if(a.prev != b.prev) return a.prev < b.prev;
        return a.t < b.t;
    });

    // res[0..N]: we use indices 1..N for our answer (res[0] is the "previous" element for i==1)
    vector<int> res(N + 1, 1);  // initialize all with 1

    // "cur" tree: tracks available numbers.
    vector<int> curArr(N, 1);  // numbers 1..N are initially available (frequency 1)
    OrderStatisticsTree cur(curArr);

    // "restrict" tree: tracks active restrictions; initially, all are 0.
    vector<int> restrictArr(N, 0);
    OrderStatisticsTree restrictTree(restrictArr);

    int idx = 0;
    int eventsSize = events.size();
    // Process positions i from 1 to N.
    for (int i = 1; i <= N; i++){
        // Process all events happening at time i.
        while(idx < eventsSize && events[idx].time == i){
            Event e = events[idx++];
            if(e.t == 1) {
                // Start restriction: update restrict tree at current time (which equals l).
                restrictTree.update(i, 1);
            } else {
                // End restriction event.
                // If the smallest active restriction’s starting time equals e.prev:
                if(restrictTree.select(1) == e.prev) {
                    int end_r;
                    if(restrictTree.p_query(N) > 1) {
                        int second = restrictTree.select(2);
                        end_r = min(i, second);
                    } else {
                        end_r = i;
                    }
                    int start_j = restrictTree.select(1); // should equal e.prev.
                    // For j from start_j to end_r-1, if the number chosen at j is not in cur,
                    // then add it back.
                    for (int j = start_j; j < end_r; j++){
                        if(cur.query(res[j], res[j]) == 0)
                            cur.update(res[j], 1);
                    }
                }
                // Remove the restriction associated with e.prev.
                restrictTree.update(e.prev, -1);
            }
        }

        int choice;
        // Decide on the choice: if the previously chosen number (res[i-1]) is still available, reuse it;
        // otherwise, choose the smallest available number from cur.
        if(cur.query(res[i - 1], res[i - 1]) != 0)
            choice = res[i - 1];
        else
            choice = cur.select(1);

        // If there is any active restriction then mark the chosen number as used.
        if(restrictTree.p_query(N) > 0)
            cur.update(choice, -1);

        res[i] = choice;
    }

    cout << *max_element(res.begin(), res.end()) << "\n";
    for (int i = 1; i <= N; i++){
        cout << res[i] << (i == N ? "\n" : " ");
    }

    return 0;
}
