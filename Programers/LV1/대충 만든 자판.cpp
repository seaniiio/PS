#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    for(int i=0; i<targets.size(); i++) {
        int count = 0;
        bool not_found = false;
        for(int j=0; j<targets[i].size(); j++) {
            int m = 101;
            bool find = false;
            char target = targets[i][j];
            for(int k=0; k<keymap.size(); k++) {
                for(int l=0; l<keymap[k].size(); l++) {
                    if(keymap[k][l] == target) {
                        int find_target = keymap[k].find(target);
                        find = true;
                        m = min(m, find_target + 1);
                    }
                }
            }
            if(find) count += m;
            else {
                not_found = true;
                break;
            }
        }
        if(not_found) {
            answer.push_back(-1);
        } else {
            answer.push_back(count);
        }
    }

    return answer;
}