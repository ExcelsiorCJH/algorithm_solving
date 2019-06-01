// https://www.acmicpc.net/problem/11720
#include <iostream>
using namespace std;

int main(){

    int n;
    scanf("%d", &n);

    int sum = 0;  // 초기값 0 설정 필수!
    for(int i=0; i<n; ++i){
        int x;
        scanf("%1d", &x);
        sum += x;
    }

    cout << sum << '\n';

    return 0;
}