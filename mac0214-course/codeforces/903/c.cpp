#include <bits/stdc++.h>

using namespace std;

int main() {

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<string> m;

        for (int i = 0; i < n; i++) {
            string a;
            cin >> a;
            m.push_back(a);
        }

        int last_idx = n-1;
        int ops = 0;

        for (int i = 0; i < n/2; i++) {
            for (int j = 0; j < n/2; j++) {
                
                char up_left = m[i][j];
                char up_right = m[j][last_idx-i];
                char down_left = m[last_idx-j][i];
                char down_right = m[last_idx-i][last_idx-j];
                
                vector<char> v = {up_left, up_right, down_left, down_right};

                char maxElement = *max_element(v.begin(), v.end());

                for (char c: v) {
                    ops += (int) (maxElement - c);
                }

                m[i][j] = maxElement;
                m[j][last_idx-i] = maxElement;
                m[last_idx-j][i] = maxElement;
                m[last_idx-i][last_idx-j] = maxElement;
            }
        }

        cout << ops << endl;
    }

    return 0;
}