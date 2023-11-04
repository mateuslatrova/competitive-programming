#include <bits/stdc++.h>

using namespace std;

bool all_equal(vector<int> v) {
    set<int> s;
    for (int x: v)
        s.insert(x);
    return s.size() == 1;
} 

void break_biggest_t(vector<int> &v) {
    
    auto maxElement = max_element(v.begin(), v.end());
    auto minElement = min_element(v.begin(), v.end());

    int fh = *minElement;
    int sh = *maxElement - *minElement;
    
    *maxElement = fh;
    v.push_back(sh);
}

int main() {

    int t;
    cin >> t;

    while (t--) {

        vector<int> tls;

        for (int i = 0; i < 3; i++) {
            int a;
            cin >> a;
            tls.push_back(a);
        }

        int max_ops = 3;

        if (all_equal(tls)) {
            cout << "YES" << endl;
            continue;
        }

        int i = 0;
        for (i = 0; i < max_ops; i++) {
            break_biggest_t(tls);

            if (all_equal(tls)) {
                cout << "YES" << endl;
                break;
            }
        }

        if (i == 3) 
            cout << "NO" << endl;
    }

    return 0;
}