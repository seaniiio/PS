#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n; cin >> n;
    int* time_arr = new int[n];
    for(int i=0; i<n; i++) {
        int k; cin >> k;
        time_arr[i] = k;
    }
    int total_time = 0;
    sort(time_arr, time_arr + n);
    for(int i=0; i<n; i++) {
        total_time += time_arr[i] * (n - i);
    }
    cout << total_time;
}