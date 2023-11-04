#include <bits/stdc++.h>

using namespace std;

bool is_substring(string x, string s) {
    if (x.find(s) != string::npos)
        return true;
    else
        return false;
}

int main() {

    int t;
    cin >> t;

    vector<int> answers;
    while (t--) {

        int n, m;
        string x, s;

        cin >> n >> m;
        cin >> x >> s;

        int ops = 0;

        while (x.size() < s.size()) {
            x += x;
            ops++;
        }

        if (is_substring(x, s))
            cout << ops << endl;
        else {
            x += x;
            ops++;
            if (is_substring(x, s))
                cout << ops << endl;
            else
                cout << -1 << endl;
        }
    }

    return 0;
}