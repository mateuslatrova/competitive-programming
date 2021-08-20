// Problem: https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#include <bits/stdc++.h>

using namespace std;

// Complete the freqQuery function below.
vector<int> freqQuery(vector<vector<int>> queries) {
    vector<int> ans;
    map<int,int> numToFreq; // maps integer to frequency.
    map<int,set<int>> freqToNums; // maps integer to frequency.
    int n = queries.size();

    for (int i = 0; i < n; i++) {
        int command = queries[i][0];
        int elem = queries[i][1];

        switch(command) {
            case 1:
                if (numToFreq.find(elem) != numToFreq.end()) {
                    freqToNums[numToFreq[elem]].erase(elem);
                    numToFreq[elem]++;
                    freqToNums[numToFreq[elem]].insert(elem);
                } else {
                    numToFreq.insert(make_pair(elem,1));
                    freqToNums[1].insert(elem);
                }
                break;
            case 2:
                if (numToFreq.find(elem) != numToFreq.end()){
                    freqToNums[numToFreq[elem]].erase(elem);
                    numToFreq[elem]--;
                    if (numToFreq[elem] == 0) {
                        numToFreq.erase(elem);
                    } else freqToNums[numToFreq[elem]].insert(elem);
                }
                break;
            case 3:
                if (freqToNums[elem].size() != 0) ans.push_back(1);
                else ans.push_back(0);
                break;
        }
    }

    return ans;
}

// Testing:
int main () {

    int q;
    cin >> q;
    vector<vector<int>> queries;

    while (q--) {
        int q0, q1;
        cin >> q0 >> q1;
        queries.push_back({q0,q1});
    }

    vector<int> ans = freqQuery(queries);

    for (int x: ans) cout << x << endl;
}