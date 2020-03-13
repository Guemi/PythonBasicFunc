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