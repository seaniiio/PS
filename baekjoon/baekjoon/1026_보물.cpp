#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n; cin >> n;
    int* arr1 = new int[n];
    int* arr2 = new int[n];
    for(int i=0; i<n; i++) {
        int k; cin >> k;
        arr1[i] = k;
    }
    for(int i=0; i<n; i++) {
        int k; cin >> k;
        arr2[i] = k;
    }
    sort(arr1, arr1+n);
    sort(arr2, arr2+n, greater<int>());
    int sum = 0;
    for(int i=0; i<n; i++) {
        sum += arr1[i] * arr2[i];
    }
    cout << sum;
}