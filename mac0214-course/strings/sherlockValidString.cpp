#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'isValid' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string isValid(string s) {
    map<char,int> charToFreq;
    map<int,unordered_set<char>> freqToChars;
    
    for (char c: s) charToFreq[c]++;

    map<char,int>::iterator it1;
    for (it1 = charToFreq.begin(); it1 != charToFreq.end(); it1++) 
        freqToChars[it1->second].insert(it1->first);

    int numFreqs = freqToChars.size();

    if (numFreqs == 1) return "YES";
    else if (numFreqs == 2) {
        map<int,unordered_set<char>>::iterator it2;
        int freqs[2]; int i = 0;
        
        for (it2 = freqToChars.begin(); it2 != freqToChars.end(); it2++) {
            freqs[i] = it2->first; 
            i++;
        }

        int maxFreq = max(freqs[0],freqs[1]);
        int minFreq = min(freqs[0],freqs[1]);

        if (freqToChars[maxFreq].size() == 1 && maxFreq-minFreq == 1) 
            return "YES";
        else if (minFreq == 1 && freqToChars[minFreq].size() == 1) return "YES";
        else return "NO";
    } else return "NO";
}
    
// Testing:
int main() {
    string inp;
    cin >> inp;

    cout << isValid(inp);
}