//Git Example
#include <iostream>
#include <vector>
#include <string>
#include<algorithm> 
using namespace std;

class Solution {
public:
    int reverse(int x) {
        string IntStr {}; 
        bool isSigned = false;
        long long intRev {};
        intRev = llabs(x);
        IntStr = to_string(intRev);
        if(x != intRev){
            isSigned = true;
        }else{
            isSigned = false;
        }
        std::reverse(IntStr.begin(),IntStr.end());
        intRev = std::stoll(IntStr);    
        if(isSigned){
            intRev = intRev * (-1);
        }
        if((intRev >= INT_MIN) && (intRev <= INT_MAX)){
            return intRev;
        }
        return 0;
    }
};

int main(){
    int valor_in {};
    Solution s1;
    cout<<"In value -> ";
    cin>>valor_in;
    cout<<s1.reverse(valor_in);


    

    return 0;
}
