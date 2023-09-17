#include <bits/stdc++.h>

using namespace std;

int main()
{

    int t;
    cin >> t;

    // max value of k so that ou can travel from room 1 to romm k and
    // return to room 1 safely

    while (t--)
    {
        int n;
        cin >> n;

        vector<int> d = {0}, s = {0};

        for (int i = 0; i < n; i++)
        {
            int x, y;
            cin >> x >> y;
            d.push_back(x), s.push_back(y);
        }

        int maximum = 300;

        for (int i = 1; i <= n; i++)
        {
            int ith_trap = d[i];
            int ith_trap_limit = ith_trap + (int) ceil((s[i]-2) / 2.0);

            if (ith_trap_limit < maximum)
                maximum = ith_trap_limit;
        }

        cout << maximum << endl;
    }

    return 0;
}