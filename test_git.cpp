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
        int intRev {};
        if((x >= -2147483648) && (x <= 2147483647)){
            IntStr = to_string(abs(x));
            if(x != abs(x)){
                isSigned = true;
            }else{
                isSigned = false;
            }
            std::reverse(IntStr.begin(),IntStr.end());
            intRev = std::stoi(IntStr);
            if(isSigned){
                intRev = intRev * (-1);
            }

            
        }else{
            cout<<" ----------";
            return 0;
        }

        // for(auto num : IntStr){
        //     cout<<num<<" ";
        // }
        return intRev;
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