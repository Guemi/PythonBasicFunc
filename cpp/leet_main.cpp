class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        int i {1}, n = A.size()-1, temp {};
        if(A.size() > 3 && A[0] < A[1] && A[n] < A[n-1]){
            // cout<<"Last item at: "<<n<<endl;
            temp = A[0];
            while(A[i] > temp && i <= n){
                // cout<<A[i]<<" > "<<temp<<" para i = "<<i<<endl;
                temp = A[i];
                i++;
            }
            while(A[i] < temp && i <= n){
                // cout<<A[i]<<" < "<<temp<<" para i = "<<i<<endl;
                temp = A[i];
                i++;
            }
            // cout<<i<<endl;
            if(i-1 == n) return true;
        }
        return false;
        
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

string boolToString(bool input) {
    return input ? "True" : "False";
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> A = stringToIntegerVector(line);
        
        bool ret = Solution().validMountainArray(A);

        string out = boolToString(ret);
        cout << out << endl;
    }
    return 0;
}