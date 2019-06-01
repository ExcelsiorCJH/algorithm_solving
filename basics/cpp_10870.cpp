// https://www.acmicpc.net/problem/10870
// ppt 참고
#include <iostream>
#include <functional>
using namespace std;

int main(){

    int n;
    cin >> n;
    
    function<int(int)> f = [&](int n){
        if (n <= 1) return n;
        else return f(n-1) + f(n-2);
    };
    
    cout << f(n) << '\n';

    return 0;
}