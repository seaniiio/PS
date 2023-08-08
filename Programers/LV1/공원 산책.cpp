#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer;
    int width = park[0].size();
    int length = park.size();
    for(int i=0; i<length; i++) {
        for(int j=0; j<width; j++) {
            if(park[i][j] == 'S') {
                answer.push_back(i);
                answer.push_back(j);

                cout << answer[0] << ' ' << answer[1] << '\n';
                break;
            }
        }
    }

    for(int k=0; k<routes.size(); k++) {
        bool flag = true;
        string route = routes[k];
        int go = route[2] - '0';
        if(route[0] == 'S') {
            if(answer[0] + go <= length - 1) {
                for(int i=answer[0]; i<answer[0] + go; i++) {
                    if(park[i][answer[1]] == 'X') {
                        flag = false;
                        break;
                    }
                }
                if(flag) answer[0] += go; cout << "S " << answer[0] << '\n';
            }
        }
        else if(route[0] == 'W') {
            if(answer[1] - go >= 0) {
                for(int i=answer[1]; i<answer[1] - go; i--) {
                    if(park[answer[0]][i] == 'X') {
                        flag = false;
                        break;
                    }
                }
                if(flag) answer[1] -= go; cout << "W " << answer[1] << '\n';

            }
        }
        else if(route[0] == 'N') {
            if(answer[0] - go >= 0) {
                for(int i = answer[0]; i<answer[0] - go; i--) {
                    if(park[i][answer[1]] == 'X') {
                        flag = false;
                        break;
                    }
                }
                if(flag) answer[0] -= go; cout << "N " << answer[0] << '\n';

            }
        }
        else if(route[0] == 'E') {
            cout << answer[1] + go << ' ' << width - 1 << '\n';
            if(answer[1] + go <= width - 1) {
                for(int i=answer[1]; i<answer[1] + go; i++) {
                    if(park[answer[0]][i] == 'X') {
                        flag = false;
                        break;
                    }
                }
                if(flag) answer[1] += go; cout << "E " << answer[1] << '\n';


            }
        }
    }
    return answer;
}


int main() {
    vector<string> park;
    park.push_back("OSO"); park.push_back("OOO"); park.push_back("OXO"); park.push_back("OOO");
    vector<string> routes;
    routes.push_back("E 2"); routes.push_back("S 3"); routes.push_back("W 1");


    vector<int> v = solution(park, routes);
    for(int i=0; i<v.size(); i++) {
        cout << v[i] << ' ';
    }
}