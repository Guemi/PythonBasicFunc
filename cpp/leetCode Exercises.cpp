#include <iostream>
using namespace std;
/***        REDUCE A NUMBER TO ZERO ****/
class Solution {
public:
    int numberOfSteps (int num) {
        int counter {};
        do{
            if(num%2 == 0){
                num = num/2;
            }
            else{
                num--;
            }
        counter++;
        }while(num>0);
        return counter;    
    }  
};
int main(){
    int in_test {};
    Solution s1;
    cout<<"In value -> ";
    cin>>in_test;
    cout<<s1.numberOfSteps(in_test);
    return 0;
}