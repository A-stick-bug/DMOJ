#include<bits/stdc++.h>

using namespace std;

const long long INF = 1e9+7;
const long long MAXN = 1e5+5;

struct Node {
    long long total, prefix, suffix, inside;
};

Node seg[4*MAXN];
long long arr[MAXN];

Node combine(Node left, Node right) {
    Node res;
    res.total = left.total + right.total;
    res.prefix = max(left.prefix, left.total + right.prefix);
    res.suffix = max(right.suffix, right.total + left.suffix);
    res.inside = max({left.inside, right.inside, left.suffix + right.prefix});
    return res;
}

void build(long long v, long long tl, long long tr) {
    if(tl == tr) {
        seg[v] = {arr[tl], arr[tl], arr[tl], arr[tl]};
    } else {
        long long tm = (tl + tr) / 2;
        build(v*2, tl, tm);
        build(v*2+1, tm+1, tr);
        seg[v] = combine(seg[v*2], seg[v*2+1]);
    }
}

void update(long long v, long long tl, long long tr, long long pos, long long val) {
    if(tl == tr) {
        seg[v] = {val, val, val, val};
    } else {
        long long tm = (tl + tr) / 2;
        if(pos <= tm)
            update(v*2, tl, tm, pos, val);
        else
            update(v*2+1, tm+1, tr, pos, val);
        seg[v] = combine(seg[v*2], seg[v*2+1]);
    }
}

Node query(long long v, long long tl, long long tr, long long l, long long r) {
    if(l > r)
        return {-INF, -INF, -INF, -INF};
    if(l == tl && r == tr)
        return seg[v];
    long long tm = (tl + tr) / 2;
    return combine(query(v*2, tl, tm, l, min(r, tm)),
                   query(v*2+1, tm+1, tr, max(l, tm+1), r));
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, Q;
    cin >> N >> Q;
    for(long long i = 0; i < N; i++)
        cin >> arr[i];
    build(1, 0, N-1);
    while(Q--) {
        char type;
        cin >> type;
        if(type == 'S') {
            long long i, v;
            cin >> i >> v;
            i--;
            update(1, 0, N-1, i, v);
        } else {
            long long l, r;
            cin >> l >> r;
            l--; r--;
            cout << query(1, 0, N-1, l, r).inside << "\n";
        }
    }

    return 0;
}
