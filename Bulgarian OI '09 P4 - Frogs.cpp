// https://dmoj.ca/problem/bgoi09p4
// Generalized algorithm, this works for online queries as well
// To save memory, we only use primitive data types
//
// Cube root lifting with O(n) memory
//
// TC: O(N^{4/3})
// SC: O(N)

#include <stdio.h>

#define MN 1000001


void print(int n) {  // io templates, credit: humanthe2nd
    char s[10];
    int i=0;
    while(n>0){
        s[i++]=(n%10)+'0';
        n/=10;
    }
    while (--i >= 0) {
        putchar(s[i]);
    }
    putchar(' ');
}

int N;
int arr[MN];
int nxt[MN];

int storage[MN];  // literally the only extra storage we can use
int top = -1;  // index of top element when storage is being used as a stack

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
        nxt[i] = -1;
    }

    // standard monotonic stack, next greater element
    for (int i = 0; i < N; i++) {
        while (top >= 0 && arr[storage[top]] < arr[i]) {
            nxt[storage[top]] = i;
            top--;
        }
        storage[++top] = i;
    }

    // before this point, storage is used as a stack
    // now, it will be used as a binary lifting table

    // runtime of this part is O(N * JUMP_CNT)
    int JUMP_CNT = 100;
    for (int i = 0; i < N; i++) {
        int cur = i;
        for (int cnt = 0; cur != -1 && cnt < JUMP_CNT; cnt++)
            cur = nxt[cur];
        storage[i] = cur;
    }

    int SKIP = 25;  // only precompute every this many nodes to save memory
    int JUMP_CNT2 = JUMP_CNT * JUMP_CNT;

    // runtime of this part is O(N * JUMP_CNT / SKIP)
    int bigjump[MN / SKIP + 1];
    for (int i = 0; i < N; i++) {
        if (i % SKIP == 0) {
            int cur = i;
            for (int cnt = 0; cur != -1 && cnt < JUMP_CNT; cnt++)
                cur = storage[cur];
            bigjump[i / SKIP] = cur;
        }
    }

    for (int i = 0; i < N; i++) {  // queries
        int k;
        scanf("%d", &k);

        // k-th ancestor of i
        int cur = i;
        while (k > 0 && cur != -1) {
            if (k >= JUMP_CNT2 && cur % SKIP == 0) {  // try big jump
                cur = bigjump[cur / SKIP];
                k -= JUMP_CNT2;
            } else if  (k >= JUMP_CNT) {  // try small jump
                cur = storage[cur];
                k -= JUMP_CNT;
            } else {
                cur = nxt[cur];
                k--;
            }
        }
        if (cur == -1) {  // -1
            putchar('-');
            putchar('1');
            putchar(' ');
        }
        else
            print(arr[cur]);
    }

    return 0;
}
