// https://dmoj.ca/problem/nccc8s2
// - Count number of subsequences of a string with all unique characters
// - For each character as we either include it in a subsequence or we don't
// - We have X+1 ways of choosing which specific occurrence of the character
//   we include (or don't include at all), where X is the number of occurrences

import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        String s = readLine();
        int n = s.length();
        long MOD = (int) 1e9 + 7;

        int[] freq = new int[26];
        for (int i = 0; i < n; i++){
            freq[s.charAt(i) - 'a']++;
        }

        Long total = 1L;
        for (int i = 0; i < 26; i++){
            total = (total * (freq[i] + 1)) % MOD;
        }
        System.out.println(total);
    }
    static String next () throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine().trim());
        return st.nextToken();
    }
    static long readLong () throws IOException {
        return Long.parseLong(next());
    }
    static int readInt () throws IOException {
        return Integer.parseInt(next());
    }
    static double readDouble () throws IOException {
        return Double.parseDouble(next());
    }
    static char readCharacter () throws IOException {
        return next().charAt(0);
    }
    static String readLine () throws IOException {
        return br.readLine().trim();
    }
}
