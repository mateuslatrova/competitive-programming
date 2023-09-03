#include <bits/stdc++.h>

using namespace std;

int main() {

    int t;
    cin >> t;

    while (t--) {

        int n; cin >> n;
        int b[n];
        for (int i = 0 ; i < n; i++) {
            cin >> b[i]; 
        }

        vector<int> a = {b[0]};

        for (int i = 1; i < n; i++) {
            int x = min(b[i], b[i-1]);
            while (x > b[i] | x >= b[i-1])
                x -= 1;

            if (x >= 1) 
                a.push_back(x);

            a.push_back(b[i]);
        }

        int last = b[n-1];
        if (last > 1)
            a.push_back(last-1);


        int m = a.size();
        cout << m << endl;
        
        for (int i = 0; i < m; i++) {
            cout << a[i];
            if (i != m-1)
                cout << " ";
        } 
        cout << endl;
    }

    return 0;
}