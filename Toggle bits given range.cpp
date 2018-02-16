#problem: http://practice.geeksforgeeks.org/problems/toggle-bits-given-range/0
#Solution:
#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv) {
    int t;
    int N,L,R;
    cin>>t;// test cases
    for(int i=0;i<t;i++)
    {
        cin>>N>>L>>R;
        for(int i=L-1;i<R;i++)
        {
            N^=1<<i;
        }
        cout<<N<<endl;
    }
    return 0;
}
