#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;

    vector<int> answers;

    while (t--) {
        int n;
        cin >> n;

        vector<int> a;
        for (int i = 0; i < n; i++) {
            int b;
            cin >> b;
            a.push_back(b);
        }

        vector<int> dp(n, n+1);
        dp[n-1] = 1;

        for (int i = n-2; i >= 0; i--) {
            int f_opt = dp[i+1]+1;
            
            int s_opt = 0;
            if (i+a[i]+1 > n)
                s_opt = n+1;
            else if (i+a[i]+1 == n)
                s_opt = 0;
            else
                s_opt = dp[i+a[i]+1];
            
            dp[i] = min(f_opt, s_opt);
        }

        answers.push_back(dp[0]);
    }

    for (auto x: answers)
        cout << x << endl;

    return 0;
}
