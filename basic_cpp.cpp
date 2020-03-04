#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n = 0;
    cin>>n;
    int *array0 = new int[n];
    for (int z=0; z<n; z++){
        cin >> array0 [z];
    }
    //cin>> *array0 ;
    for(int i=0;i<n;i++){
        cout<<array0[n-1-i]<<" ";
    }
    return 0;
}
