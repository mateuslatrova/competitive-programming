#include <bits/stdc++.h>

using namespace std;

const int maxv = 1000000;

int is_prime(int n)
{
    if (n <= 1)
        return 0;
    
    if (n == 2 || n == 3)
        return 1;
    
    if (n % 2 == 0 || n % 3 == 0)
        return 0;
    
    for (int i = 5; i * i <= n; i = i + 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return 0;
 
    return 1;
}

void add_divs(int x, map<int, int>&divs){
    int i = 2;
    while(i * i <= x){
        if (!is_prime(i)) {
            i++;
            continue;
        }

        while (x % i == 0){
            divs[i]++;
            x /= i;
        }
        i++;
    }
    if(x > 1) divs[x]++;
}


int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> nums;
        set<int> set_nums;
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            nums.push_back(a);
            set_nums.insert(a);
        }

        // edge case:
        if (set_nums.size() == 1) {
            cout << "YES" << endl;
            continue;
        }

        map<int, int> divs;

        for (int num: nums) {
            add_divs(num, divs);   
        }

        bool ok = true;

        for (auto pair : divs) {
            if (pair.second % n != 0) {
                cout << "NO" << endl;
                ok = false;
                break;
            }
        }

        if (ok)
            cout << "YES" << endl;

    }

    return 0;
}
