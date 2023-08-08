#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    int y = stoi(today.substr(0, 4));
    int m = stoi(today.substr(5, 2));
    int d = stoi(today.substr(8, 2));
    if(d == 28) {
        d = 1;
        if (m == 12) {
            y += 1;
            m = 1;
        }
        else {
            m += 1;
        }
    }
    else d += 1;

    for(int i=0; i<privacies.size(); i++) {
        string pri = privacies[i];
        char type = pri[pri.size()-1];
        int term = 0;
        int _y = stoi(pri.substr(0, 4));
        int _m = stoi(pri.substr(5, 2));
        int _d = stoi(pri.substr(8, 2));

        for(int k=0; k<terms.size(); k++) {
            if(terms[k][0] == type) {
                if(terms[k].size() == 3) term = terms[k][2] - '0';
                else if(terms[k].size() == 4) term = stoi(terms[k].substr(2, 2));
                else term = stoi(terms[k].substr(2, 3));
                break;
            }
        }
        int plus_y = term / 12;
        int plus_m = term % 12;
        int up_y;
        while ((_m + plus_m) > 12) {
            plus_m -= 12;
            plus_y += 1;
        }
        _m += plus_m;
        _y += plus_y;

        bool flag = false;
        if(_y < y) {
            flag = true;
        }
        else if(_y == y) {
            if(_m < m) flag = true;
            else if (_m == m) {
                if(_d < d ) flag = true;
            }
        }

        if(flag) answer.push_back(i+1);
    }
    return answer;
}