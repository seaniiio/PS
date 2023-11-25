#include <iostream>
using namespace std;

int n, m;
bool visited[9] = {false, };
int nums[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
int result[9] = {0, };

void DFS(int lv) {
    if(lv == m) { // 재귀 종료조건
        for(int i=0; i<m; i++) {
            cout << result[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for(int i=0; i<n; i++) {
        if(visited[i] == false) {
            visited[i] = true;
            result[lv] = nums[i];
            DFS(lv + 1);
            visited[i] = false;
        }
    }
}

int main() {
    cin >> n >> m;
    DFS(0);
}